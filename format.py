import json

with open("c:/Users/sarjare/.gemini/antigravity/scratch/crosssword/best_layout.json", "r") as f:
    data = json.load(f)

questions = data['q']

# Step 1: Assign top-to-bottom, left-to-right numbering for start cells
# Group questions by their start cell (x, y)
start_cells = {}
for q in questions:
    k = (q['x'], q['y'])
    if k not in start_cells:
        start_cells[k] = []
    start_cells[k].append(q)

# Sort start cells by Y then X
sorted_cells = sorted(start_cells.keys(), key=lambda p: (p[1], p[0]))

cell_numbering = {}
current_id = 1
for cell in sorted_cells:
    cell_numbering[cell] = current_id
    current_id += 1

# Now assign IDs to questions. Notice that we give each question a unique `q_id` for Javascript,
# but we display the `display_id` (the crossword number).
# Wait, if we give them unique IDs for JS, we can just use strings like "1A", "1D", "2A".
# That perfectly solves the intersection/same-number problem!
js_questions = []

for q in questions:
    cell = (q['x'], q['y'])
    num = cell_numbering[cell]
    display_id = num
    unique_id = f"'{num}{q['dir'][0].upper()}'"  # '1A' or '1D'
    
    js_questions.append(f"""{{
    id: {unique_id},
    display_id: {display_id},
    dir: '{q['dir']}',
    x: {q['x']},
    y: {q['y']},
    len: {q['len']},
    ans: "{q['ans']}",
    code: `{q['code']}`,
    hint: "{q['hint']}"
}}""")

js_array = "const QUESTIONS = [\n  " + ",\n  ".join(js_questions) + "\n];"

with open("c:/Users/sarjare/.gemini/antigravity/scratch/crosssword/formatted_q.js", "w") as f:
    f.write(js_array)
    f.write(f"\n\n// grid cols: {data['w']}, grid rows: {data['h']}\n")

