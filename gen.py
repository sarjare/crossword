import random

words = [
    ("BACKUPS", 2, "Extra copies of computer files that can be used to restore lost or damaged data."),
    ("ANTIVIRUS", 12, "Computer programs that can block, detect, and remove viruses and other malware."),
    ("THREATACTOR", 15, "An individual, group, or organization that conducts or intends to conduct harmful cyber activities."),
    ("DARKWEB", 16, "Part of the internet that isn't indexed by search engines."),
    ("SPAM", 17, "Unsolicited emails sent to many addresses."),
    ("DATABREACH", 20, "The unauthorized movement or disclosure of sensitive information, something companies like Dell Technologies work to prevent."),
    ("SPYWARE", 22, "Software that is secretly installed into an information system without user knowledge."),
    ("ENCRYPTION", 23, "Converting data into a form that cannot be easily understood by unauthorized users, widely used in Dell's security solutions."),
    ("VPN", 1, "A mechanism for creating a secure connection between a device and a network."),
    ("BOTNET", 2, "A collection of computers compromised and controlled across a network."),
    ("CYBERSECURITY", 3, "The protection of digital information and systems, a key focus area for Dell Technologies."),
    ("SPOOFING", 4, "Faking the sending address of a transmission to gain illegal access."),
    ("INSIDERTHREAT", 5, "A cybersecurity risk that originates from within an organization."),
    ("AUTHENTICATION", 6, "A process used to verify a user's identity, important in Zero Trust models used by Dell."),
    ("PASSWORD", 7, "A string of characters used to authenticate an identity."),
    ("VULNERABILITY", 8, "A flaw or weakness in a system that could be exploited."),
    ("RANSOMWARE", 9, "Malware that denies access to data until a ransom is paid, which Dell's recovery solutions help handle."),
    ("MALWARE", 10, "Software that disrupts or damages systems by performing unauthorized actions."),
    ("FIREWALL", 11, "Software designed to block unauthorized access to a network."),
    ("VIRUS", 13, "A program that can replicate itself and spread harm."),
    ("PASSKEY", 14, "A modern, more secure alternative to passwords for user authentication."),
    ("HACKER", 18, "An unauthorized user attempting to gain access to a system."),
    ("PHISHING", 19, "A method of tricking users into revealing sensitive information through fake messages or websites."),
    ("PRIVACY", 21, "The ability of individuals to control how their personal information is used.")
]

# Sort words by length descending
words.sort(key=lambda x: len(x[0]), reverse=True)

import json
from collections import defaultdict

GRID_SIZE = 40  # Max size for generating, we can crop later

def try_place(word_info):
    best_placements = []
    word, id_, hint = word_info
    
    if not placed_words:
        return [(str(words[0]), 'across', GRID_SIZE//2, GRID_SIZE//2)]
        
    for placed in placed_words:
        p_word, p_dir, p_x, p_y = placed['word'], placed['dir'], placed['x'], placed['y']
        p_len = len(p_word)
        
        # Check intersections
        for i, char in enumerate(word):
            for j, p_char in enumerate(p_word):
                if char == p_char:
                    # Potential intersection
                    if p_dir == 'across':
                        # New word will be down
                        new_dir = 'down'
                        new_x = p_x + j
                        new_y = p_y - i
                    else:
                        # New word will be across
                        new_dir = 'across'
                        new_x = p_x - i
                        new_y = p_y + j
                        
                    # Validate boundary
                    if new_x >= 0 and new_x + (len(word) if new_dir == 'across' else 0) < GRID_SIZE and \
                       new_y >= 0 and new_y + (len(word) if new_dir == 'down' else 0) < GRID_SIZE:
                        
                        # Validate collisions and adjacency
                        valid = True
                        intersections = 0
                        for k, c in enumerate(word):
                            test_x = new_x + (k if new_dir == 'across' else 0)
                            test_y = new_y + (k if new_dir == 'down' else 0)
                            
                            # Check cell
                            if (test_x, test_y) in grid_chars:
                                if grid_chars[(test_x, test_y)] != c:
                                    valid = False; break
                                intersections += 1
                                continue
                                
                            # Check adjacency
                            if new_dir == 'across':
                                if (test_x, test_y-1) in grid_chars or (test_x, test_y+1) in grid_chars:
                                    valid = False; break
                            else:
                                if (test_x-1, test_y) in grid_chars or (test_x+1, test_y) in grid_chars:
                                    valid = False; break
                        
                        # Check ends
                        if new_dir == 'across':
                            if (new_x-1, new_y) in grid_chars or (new_x+len(word), new_y) in grid_chars:
                                valid = False
                        else:
                            if (new_x, new_y-1) in grid_chars or (new_x, new_y+len(word)) in grid_chars:
                                valid = False
                                
                        if valid:
                            # Score based on intersections to make it tight
                            best_placements.append((intersections, new_dir, new_x, new_y))

    if best_placements:
        best_placements.sort(key=lambda x: x[0], reverse=True)
        return [(word_info, p[1], p[2], p[3]) for p in best_placements[:5]]
    return []

# Generate a few layouts and pick the one that fits all words or most words and is smallest
best_layout = None
best_placed_count = 0
best_area = float('inf')

for attempt in range(50):
    grid_chars = {}
    placed_words = []
    
    # Randomize order a bit for variety
    current_words = words.copy()
    random.shuffle(current_words)
    current_words.sort(key=lambda x: len(x[0]), reverse=True)
    
    # Place first word in middle
    first = current_words[0]
    placed_words.append({
        'word': first[0], 'id': first[1], 'hint': first[2],
        'dir': 'across', 'x': GRID_SIZE//2, 'y': GRID_SIZE//2
    })
    for i, c in enumerate(first[0]):
        grid_chars[(GRID_SIZE//2 + i, GRID_SIZE//2)] = c
        
    for word_info in current_words[1:]:
        placements = try_place(word_info)
        if placements:
            # Pick a random good placement
            _, p_dir, p_x, p_y = random.choice(placements)
            placed_words.append({
                'word': word_info[0], 'id': word_info[1], 'hint': word_info[2],
                'dir': p_dir, 'x': p_x, 'y': p_y
            })
            for i, c in enumerate(word_info[0]):
                grid_chars[(p_x + (i if p_dir == 'across' else 0), p_y + (i if p_dir == 'down' else 0))] = c
                
    if len(placed_words) > best_placed_count:
        best_placed_count = len(placed_words)
        best_layout = placed_words
        # Calculate area
        min_x = min(p['x'] for p in placed_words)
        max_x = max(p['x'] + (len(p['word']) if p['dir'] == 'across' else 1) for p in placed_words)
        min_y = min(p['y'] for p in placed_words)
        max_y = max(p['y'] + (len(p['word']) if p['dir'] == 'down' else 1) for p in placed_words)
        best_area = (max_x - min_x) * (max_y - min_y)
    elif len(placed_words) == best_placed_count:
        min_x = min(p['x'] for p in placed_words)
        max_x = max(p['x'] + (len(p['word']) if p['dir'] == 'across' else 1) for p in placed_words)
        min_y = min(p['y'] for p in placed_words)
        max_y = max(p['y'] + (len(p['word']) if p['dir'] == 'down' else 1) for p in placed_words)
        area = (max_x - min_x) * (max_y - min_y)
        if area < best_area:
            best_area = area
            best_layout = placed_words

print(f"Placed {best_placed_count}/{len(words)} words in best layout.")

if best_layout:
    min_x = min(p['x'] for p in best_layout)
    min_y = min(p['y'] for p in best_layout)
    max_x = max(p['x'] + (len(p['word']) if p['dir'] == 'across' else 1) for p in best_layout)
    max_y = max(p['y'] + (len(p['word']) if p['dir'] == 'down' else 1) for p in best_layout)
    
    print(f"Grid size: {max_x - min_x}x{max_y - min_y}")
    
    out_json = []
    # Note: original code from HTML was: code: "some js..."
    # We will just generate some sample code for each based on the word
    for p in best_layout:
        out_json.append({
            'id': p['id'],
            'dir': p['dir'],
            'x': p['x'] - min_x,
            'y': p['y'] - min_y,
            'len': len(p['word']),
            'ans': p['word'],
            'code': f"// System module {p['word']} check\\nfunction execute_{p['word'].lower()}() {{\\n  return activate_protocol('{p['id']}');\\n}}",
            'hint': p['hint']
        })
        
    with open('best_layout.json', 'w') as f:
        json.dump({'w': max_x-min_x, 'h': max_y-min_y, 'q': out_json}, f, indent=2)
