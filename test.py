import json

questions = [
    { "id": 2, "dir": 'across', "x": 1, "y": 1, "len": 7, "ans": "BACKUPS" },
    { "id": 12, "dir": 'across', "x": 0, "y": 11, "len": 9, "ans": "ANTIVIRUS" },
    { "id": 15, "dir": 'across', "x": 10, "y": 14, "len": 11, "ans": "THREATACTOR" },
    { "id": 16, "dir": 'across', "x": 10, "y": 16, "len": 7, "ans": "DARKWEB" },
    { "id": 17, "dir": 'across', "x": 17, "y": 16, "len": 4, "ans": "SPAM" },
    { "id": 20, "dir": 'across', "x": 13, "y": 18, "len": 10, "ans": "DATABREACH" },
    { "id": 22, "dir": 'across', "x": 10, "y": 21, "len": 7, "ans": "SPYWARE" },
    { "id": 23, "dir": 'across', "x": 4, "y": 23, "len": 10, "ans": "ENCRYPTION" },

    { "id": 1, "dir": 'down', "x": 12, "y": 0, "len": 3, "ans": "VPN" },
    { "id": 2, "dir": 'down', "x": 1, "y": 1, "len": 6, "ans": "BOTNET" },
    { "id": 3, "dir": 'down', "x": 3, "y": 1, "len": 13, "ans": "CYBERSECURITY" },
    { "id": 4, "dir": 'down', "x": 0, "y": 6, "len": 8, "ans": "SPOOFING" },
    { "id": 5, "dir": 'down', "x": 10, "y": 5, "len": 13, "ans": "INSIDERTHREAT" },
    { "id": 6, "dir": 'down', "x": 15, "y": 7, "len": 14, "ans": "AUTHENTICATION" },
    { "id": 7, "dir": 'down', "x": 7, "y": 8, "len": 8, "ans": "PASSWORD" },
    { "id": 8, "dir": 'down', "x": 12, "y": 7, "len": 13, "ans": "VULNERABILITY" },
    { "id": 9, "dir": 'down', "x": 19, "y": 6, "len": 10, "ans": "RANSOMWARE" },
    { "id": 10, "dir": 'down', "x": 14, "y": 11, "len": 7, "ans": "MALWARE" },
    { "id": 11, "dir": 'down', "x": 4, "y": 10, "len": 8, "ans": "FIREWALL" },
    { "id": 13, "dir": 'down', "x": 17, "y": 11, "len": 5, "ans": "VIRUS" },
    { "id": 14, "dir": 'down', "x": 13, "y": 13, "len": 7, "ans": "PASSKEY" },
    { "id": 18, "dir": 'down', "x": 7, "y": 16, "len": 6, "ans": "HACKER" },
    { "id": 19, "dir": 'down', "x": 11, "y": 18, "len": 8, "ans": "PHISHING" },
    { "id": 21, "dir": 'down', "x": 15, "y": 20, "len": 7, "ans": "PRIVACY" }
]

grid = {}
errors = []

for q in questions:
    for i in range(q['len']):
        x = q['x'] + (i if q['dir'] == 'across' else 0)
        y = q['y'] + (0 if q['dir'] == 'across' else i)
        char = q['ans'][i]
        
        if (x, y) in grid:
            if grid[(x, y)] != char:
                errors.append(f"Conflict at ({x}, {y}): '{grid[(x, y)]}' vs '{char}' for {q['ans']}")
        else:
            grid[(x, y)] = char

for y in range(25):
    for x in range(25):
        print(grid.get((x, y), ' '), end='')
    print()

if errors:
    print("ERRORS:", errors)
else:
    print("No conflicts!")
