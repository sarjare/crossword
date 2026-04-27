import json

questions = [
    { "id": 2, "dir": 'across', "ans": "BACKUPS", "x": 1, "y": 1 },
    { "id": 12, "dir": 'across', "ans": "ANTIVIRUS", "x": 0, "y": 11 },
    { "id": 15, "dir": 'across', "ans": "THREATACTOR", "x": 10, "y": 14 },
    { "id": 16, "dir": 'across', "ans": "DARKWEB", "x": 10, "y": 16 },
    { "id": 17, "dir": 'across', "ans": "SPAM", "x": 17, "y": 16 },
    { "id": 20, "dir": 'across', "ans": "DATABREACH", "x": 13, "y": 18 },
    { "id": 22, "dir": 'across', "ans": "SPYWARE", "x": 10, "y": 21 },
    { "id": 23, "dir": 'across', "ans": "ENCRYPTION", "x": 4, "y": 23 },

    { "id": 1, "dir": 'down', "ans": "VPN", "x": 12, "y": 0 },
    { "id": 2, "dir": 'down', "ans": "BOTNET", "x": 1, "y": 1 },
    { "id": 3, "dir": 'down', "ans": "CYBERSECURITY", "x": 3, "y": 1 },
    { "id": 4, "dir": 'down', "ans": "SPOOFING", "x": 0, "y": 6 },
    { "id": 5, "dir": 'down', "ans": "INSIDERTHREAT", "x": 10, "y": 5 },
    { "id": 6, "dir": 'down', "ans": "AUTHENTICATION", "x": 15, "y": 7 },
    { "id": 7, "dir": 'down', "ans": "PASSWORD", "x": 7, "y": 8 },
    { "id": 8, "dir": 'down', "ans": "VULNERABILITY", "x": 12, "y": 7 },
    { "id": 9, "dir": 'down', "ans": "RANSOMWARE", "x": 19, "y": 6 },
    { "id": 10, "dir": 'down', "ans": "MALWARE", "x": 14, "y": 11 },
    { "id": 11, "dir": 'down', "ans": "FIREWALL", "x": 4, "y": 10 },
    { "id": 13, "dir": 'down', "ans": "VIRUS", "x": 17, "y": 11 },
    { "id": 14, "dir": 'down', "ans": "PASSKEY", "x": 13, "y": 13 },
    { "id": 18, "dir": 'down', "ans": "HACKER", "x": 7, "y": 16 },
    { "id": 19, "dir": 'down', "ans": "PHISHING", "x": 11, "y": 18 },
    { "id": 21, "dir": 'down', "ans": "PRIVACY", "x": 15, "y": 20 }
]

from z3 import *

s = Solver()

x_vars = {}
y_vars = {}

for q in questions:
    x_vars[q['id'], q['dir']] = Int(f"x_{q['id']}_{q['dir']}")
    y_vars[q['id'], q['dir']] = Int(f"y_{q['id']}_{q['dir']}")
    x = x_vars[q['id'], q['dir']]
    y = y_vars[q['id'], q['dir']]
    s.add(x >= 0, x <= 25)
    s.add(y >= 0, y <= 25)

s.add(x_vars[2, 'across'] == x_vars[2, 'down'])
s.add(y_vars[2, 'across'] == y_vars[2, 'down'])

def cells(q):
    x = x_vars[q['id'], q['dir']]
    y = y_vars[q['id'], q['dir']]
    for i in range(len(q['ans'])):
        yield (x + (i if q['dir'] == 'across' else 0), 
               y + (i if q['dir'] == 'down' else 0), 
               q['ans'][i])

# Add intersection constraints
# For every pair of words, if they span overlapping coordinates, they MUST have the same char.
# Also, they are only allowed to overlap if the characters match. If they don't match, they cannot overlap.
for i in range(len(questions)):
    for j in range(i+1, len(questions)):
        q1 = questions[i]
        q2 = questions[j]
        # We assume words can only intersect if their directions are orthogonal
        if q1['dir'] != q2['dir']:
            for i1, char1 in enumerate(q1['ans']):
                c1_x = x_vars[q1['id'], q1['dir']] + (i1 if q1['dir'] == 'across' else 0)
                c1_y = y_vars[q1['id'], q1['dir']] + (i1 if q1['dir'] == 'down' else 0)
                
                for i2, char2 in enumerate(q2['ans']):
                    c2_x = x_vars[q2['id'], q2['dir']] + (i2 if q2['dir'] == 'across' else 0)
                    c2_y = y_vars[q2['id'], q2['dir']] + (i2 if q2['dir'] == 'down' else 0)
                    
                    if char1 != char2:
                        s.add(Or(c1_x != c2_x, c1_y != c2_y))
        else:
            # Parallel words cannot overlap
            for i1, char1 in enumerate(q1['ans']):
                c1_x = x_vars[q1['id'], q1['dir']] + (i1 if q1['dir'] == 'across' else 0)
                c1_y = y_vars[q1['id'], q1['dir']] + (i1 if q1['dir'] == 'down' else 0)
                for i2, char2 in enumerate(q2['ans']):
                    c2_x = x_vars[q2['id'], q2['dir']] + (i2 if q2['dir'] == 'across' else 0)
                    c2_y = y_vars[q2['id'], q2['dir']] + (i2 if q2['dir'] == 'down' else 0)
                    s.add(Or(c1_x != c2_x, c1_y != c2_y))


# Add soft constraints to prefer the initial coordinates
original = {}
for q in questions:
    k = (q['id'], q['dir'])
    original[k] = (q['x'], q['y'])

for k, (x0, y0) in original.items():
    s.add(x_vars[k] >= x0 - 3, x_vars[k] <= x0 + 3)
    s.add(y_vars[k] >= y0 - 3, y_vars[k] <= y0 + 3)

# Add numbering constraint!
# A crossword numbers clues top-to-bottom, left-to-right.
# This means if id1 < id2, then either y1 < y2 or (y1 == y2 and x1 < x2).
ids_in_order = sorted(set([q['id'] for q in questions]))
for i in range(len(ids_in_order) - 1):
    id1 = ids_in_order[i]
    id2 = ids_in_order[i+1]
    
    # get coordinates for id1
    # could be across or down or both
    qs1 = [q for q in questions if q['id'] == id1]
    qs2 = [q for q in questions if q['id'] == id2]
    
    # The start square of id1 is x1, y1
    x1 = x_vars[qs1[0]['id'], qs1[0]['dir']]
    y1 = y_vars[qs1[0]['id'], qs1[0]['dir']]
    
    x2 = x_vars[qs2[0]['id'], qs2[0]['dir']]
    y2 = y_vars[qs2[0]['id'], qs2[0]['dir']]
    
    s.add(Or(y1 < y2, And(y1 == y2, x1 < x2)))

if s.check() == sat:
    print("SAT!")
    m = s.model()
    for q in questions:
        k = (q['id'], q['dir'])
        print(f"ID {q['id']} {q['dir']}: x={m[x_vars[k]].as_long()}, y={m[y_vars[k]].as_long()} (was {q['x']},{q['y']})")
else:
    print("UNSAT! Relaxing numbering constraint...")
    
    # Relax numbering constraint
    s2 = Solver()
    for k in x_vars:
        s2.add(x_vars[k] >= 0, x_vars[k] <= 30)
        s2.add(y_vars[k] >= 0, y_vars[k] <= 30)
    
    s2.add(x_vars[2, 'across'] == x_vars[2, 'down'])
    s2.add(y_vars[2, 'across'] == y_vars[2, 'down'])
    for i in range(len(questions)):
        for j in range(i+1, len(questions)):
            q1, q2 = questions[i], questions[j]
            if q1['dir'] != q2['dir']:
                for i1, char1 in enumerate(q1['ans']):
                    c1_x = x_vars[q1['id'], q1['dir']] + (i1 if q1['dir'] == 'across' else 0)
                    c1_y = y_vars[q1['id'], q1['dir']] + (i1 if q1['dir'] == 'down' else 0)
                    for i2, char2 in enumerate(q2['ans']):
                        c2_x = x_vars[q2['id'], q2['dir']] + (i2 if q2['dir'] == 'across' else 0)
                        c2_y = y_vars[q2['id'], q2['dir']] + (i2 if q2['dir'] == 'down' else 0)
                        if char1 != char2:
                            s2.add(Or(c1_x != c2_x, c1_y != c2_y))
            else:
                for i1, char1 in enumerate(q1['ans']):
                    c1_x = x_vars[q1['id'], q1['dir']] + (i1 if q1['dir'] == 'across' else 0)
                    c1_y = y_vars[q1['id'], q1['dir']] + (i1 if q1['dir'] == 'down' else 0)
                    for i2, char2 in enumerate(q2['ans']):
                        c2_x = x_vars[q2['id'], q2['dir']] + (i2 if q2['dir'] == 'across' else 0)
                        c2_y = y_vars[q2['id'], q2['dir']] + (i2 if q2['dir'] == 'down' else 0)
                        s2.add(Or(c1_x != c2_x, c1_y != c2_y))
                        
    # Try to enforce intersections if their bounding boxes overlap
    intersections = {
        ('ANTIVIRUS', 'SPOOFING'): ('I', 'I'),
        ('THREATACTOR', 'INSIDERTHREAT'): ('R', 'R'),
        ('THREATACTOR', 'AUTHENTICATION'): ('I', 'I'),
        ('PASSWORD', 'ANTIVIRUS'): ('R', 'R'),
        ('VULNERABILITY', 'THREATACTOR'): ('E', 'E'),
        ('MALWARE', 'THREATACTOR'): ('T', 'T')
    }
    # This might be tricky, let's just let it run.
    for k, (x0, y0) in original.items():
        s2.add(x_vars[k] >= x0 - 4, x_vars[k] <= x0 + 4)
        s2.add(y_vars[k] >= y0 - 4, y_vars[k] <= y0 + 4)
        
    s2.set("timeout", 5000)
    print("Checking relaxed...")
    if s2.check() == sat:
        print("SAT (relaxed)!")
        m = s2.model()
        for q in questions:
            k = (q['id'], q['dir'])
            print(f"ID {q['id']} {q['dir']}: x={m[x_vars[k]].as_long()}, y={m[y_vars[k]].as_long()} (was {q['x']},{q['y']})")
    else:
        print("Still UNSAT. The original coordinates might be extremely off.")
