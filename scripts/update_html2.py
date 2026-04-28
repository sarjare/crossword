import json

# Define the python hints mapped by the exact answer word
python_hints = {
    "BACKUPS": """word = "Bpauskc"
result = ""
for i in range(len(word)):
    if i % 2 == 0:
        result += word[i]
for i in range(len(word)):
    if i % 2 != 0:
        result += word[i]
print(result)""",
    
    "ANTIVIRUS": """word = "avitnorus"
result = ""
for i in range(len(word)-1, -1, -2):
    result += word[i]
for i in range(len(word)-2, -1, -2):
    result += word[i]
print(result)""",
    
    "THREATACTOR": """word = "Trhaet Aotcr"
result = ""
for i in range(0, len(word), 2):
    result += word[i]
for i in range(1, len(word), 2):
    result += word[i]
print(result)""",
    
    "DARKWEB": """word = "DWaerk b"
result = ""
for i in range(len(word)):
    if i < len(word)//2:
        result += word[i]
for i in range(len(word)-1, len(word)//2 - 1, -1):
    result += word[i]
print(result)""",
    
    "SPAM": """word = "Smap"
result = ""
for i in range(0, len(word), 2):
    result += word[i]
for i in range(1, len(word), 2):
    result += word[i]
print(result)""",
    
    "DATABREACH": """word = "Daat Brehca"
result = ""
for i in range(len(word)):
    if i % 3 != 0:
        result += word[i]
for i in range(len(word)):
    if i % 3 == 0:
        result += word[i]
print(result)""",
    
    "SPYWARE": """word = "Sypawre"
result = ""
for i in range(len(word)-1, -1, -2):
    result += word[i]
for i in range(len(word)-2, -1, -2):
    result += word[i]
print(result)""",
    
    "ENCRYPTION": """word = "Enrcyptoin"
result = ""
for i in range(len(word)):
    if i % 2 == 0:
        result += word[i]
for i in range(len(word)):
    if i % 2 != 0:
        result += word[i]
print(result)""",
    
    "VPN": """word = "VPN"
result = ""
for i in range(len(word)):
    result += chr(ord(word[i]) + i)
print(result)""",
    
    "BOTNET": """word = "Btonet"
result = ""
for i in range(1, len(word), 2):
    result += word[i]
for i in range(0, len(word), 2):
    result += word[i]
print(result)""",
    
    "CYBERSECURITY": """word = "Cybresuciryt"
result = ""
for i in range(0, len(word), 2):
    result += word[i]
for i in range(1, len(word), 2):
    result += word[i]
print(result)""",
    
    "SPOOFING": """word = "Sopofnig"
result = ""
for i in range(len(word)):
    if i % 2 == 0:
        result += word[i]
for i in range(len(word)):
    if i % 2 != 0:
        result += word[i]
print(result)""",
    
    "INSIDERTHREAT": """word = "Insdier Thraet"
result = ""
for i in range(len(word)):
    if word[i] != " ":
        result += word[i]
print(result[:7] + " " + result[7:])""",
    
    "AUTHENTICATION": """word = "Auhteitacntion"
result = ""
for i in range(0, len(word), 2):
    result += word[i]
for i in range(1, len(word), 2):
    result += word[i]
print(result)""",
    
    "PASSWORD": """word = "Psaowrsd"
result = ""
for i in range(len(word)):
    if i % 2 == 0:
        result += word[i]
for i in range(len(word)):
    if i % 2 != 0:
        result += word[i]
print(result)""",
    
    "VULNERABILITY": """word = "Vunelarbility"
result = ""
for i in range(0, len(word), 2):
    result += word[i]
for i in range(1, len(word), 2):
    result += word[i]
print(result)""",
    
    "RANSOMWARE": """word = "Rnasomawre"
result = ""
for i in range(len(word)-1, -1, -1):
    result += word[i]
print(result)""",
    
    "MALWARE": """word = "Malwrae"
result = ""
for i in range(1, len(word), 2):
    result += word[i]
for i in range(0, len(word), 2):
    result += word[i]
print(result)""",
    
    "FIREWALL": """word = "Fireawll"
result = ""
for i in range(len(word)):
    if i != 4:
        result += word[i]
print(result)""",
    
    "VIRUS": """word = "Vrius"
result = ""
for i in range(len(word)):
    if i % 2 == 0:
        result += word[i]
for i in range(len(word)):
    if i % 2 != 0:
        result += word[i]
print(result)""",
    
    "PASSKEY": """word = "Psaesky"
result = ""
for i in range(len(word)):
    if i % 2 == 0:
        result += word[i]
for i in range(len(word)):
    if i % 2 != 0:
        result += word[i]
print(result)""",
    
    "HACKER": """word = "Hakc er"
result = ""
for ch in word:
    if ch != " ":
        result += ch
print(result)""",
    
    "PHISHING": """word = "Pihsihng"
result = ""
for i in range(len(word)):
    if i % 2 == 0:
        result += word[i]
for i in range(len(word)):
    if i % 2 != 0:
        result += word[i]
print(result)""",
    
    "PRIVACY": """word = "Prvica y"
result = ""
for ch in word:
    if ch != " ":
        result += ch
print(result)"""
}

# Write JS formatted questions array
with open("c:/Users/sarjare/.gemini/antigravity/scratch/crosssword/best_layout.json", "r") as f:
    best = json.load(f)

# generate new QUESTIONS with pythonHints
start_cells = {}
for q in best['q']:
    k = (q['x'], q['y'])
    if k not in start_cells:
        start_cells[k] = []
    start_cells[k].append(q)

sorted_cells = sorted(start_cells.keys(), key=lambda p: (p[1], p[0]))
cell_numbering = {cell: i+1 for i, cell in enumerate(sorted_cells)}

js_questions = []
for q in best['q']:
    cell = (q['x'], q['y'])
    num = cell_numbering[cell]
    unique_id = f"'{num}{q['dir'][0].upper()}'"
    hint_code = python_hints.get(q['ans'].replace(' ', ''), "")
    escaped_hint_code = hint_code.replace("`", "\`").replace("$", "\\$")
    
    js_questions.append(f"""{{
    id: {unique_id},
    display_id: {num},
    dir: '{q['dir']}',
    x: {q['x']},
    y: {q['y']},
    len: {q['len']},
    ans: "{q['ans']}",
    hint: "{q['hint']}",
    pythonHint: `{escaped_hint_code}`
}}""")

questions_js = "const QUESTIONS = [\n  " + ",\n  ".join(js_questions) + "\n];"

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CYBER VERSE | Crossword Control</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&family=Orbitron:wght@400;700&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        body {{
            background-color: #020617; 
            color: #00ff41;
            font-family: 'Fira Code', monospace;
            overflow-x: hidden;
            min-height: 100vh;
        }}
        .orbitron {{ font-family: 'Orbitron', sans-serif; }}
        
        .cyber-grid {{ 
            background-image: 
                radial-gradient(rgba(6, 182, 212, 0.15) 1px, transparent 0),
                radial-gradient(rgba(0, 255, 65, 0.1) 1px, transparent 0); 
            background-size: 24px 24px, 12px 12px;
            background-position: 0 0, 6px 6px;
            opacity: 0.8; 
        }}
        .scanline {{ 
            width: 100%; height: 3px; 
            background: linear-gradient(to right, transparent, rgba(6, 182, 212, 0.5), rgba(0, 255, 65, 0.5), transparent);
            position: fixed; top: 0; z-index: 100; pointer-events: none; 
            animation: scan 4s linear infinite; 
            box-shadow: 0 0 15px rgba(6, 182, 212, 0.5);
        }}
        @keyframes scan {{ 0% {{ top: -10px; }} 100% {{ top: 100%; }} }}

        .cyber-card {{
            background: rgba(10, 15, 30, 0.9);
            border: 1px solid #06b6d4;
            box-shadow: 0 0 15px rgba(6, 182, 212, 0.15);
            backdrop-filter: blur(8px);
        }}
        .terminal-input {{
            background: transparent;
            border: none;
            border-bottom: 2px solid #06b6d4;
            outline: none;
            color: #06b6d4;
        }}
        .terminal-input:focus {{
            border-bottom: 2px solid #00ff41;
            color: #00ff41;
        }}
        .glitch {{ animation: glitch 1s linear infinite; }}
        @keyframes glitch {{
            2%, 64% {{ transform: translate(2px, 0) skew(0deg); text-shadow: 2px 0 0 #06b6d4, -1px 0 0 #00ff41; }}
            4%, 60% {{ transform: translate(-2px, 0) skew(0deg); text-shadow: -2px 0 0 #06b6d4, 1px 0 0 #00ff41; }}
            62% {{ transform: translate(0, 0) skew(5deg); }}
        }}
        ::-webkit-scrollbar {{ width: 5px; }}
        ::-webkit-scrollbar-thumb {{ background: #06b6d4; }}
        .hidden-view {{ display: none !important; }}
        
        .grid-container {{
            display: grid;
            grid-template-columns: repeat(23, minmax(0, 1fr));
            gap: 1px;
            background: rgba(6, 182, 212, 0.2);
            border: 1px solid #06b6d4;
            padding: 1px;
        }}
        .grid-cell {{
            aspect-ratio: 1/1;
            background: #020617;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: clamp(8px, 1.2vw, 14px);
            font-weight: bold;
            color: white;
            transition: all 0.2s;
        }}
        .grid-cell.active {{
            background: rgba(6, 182, 212, 0.15) !important;
            cursor: pointer;
        }}
        .grid-cell.active:hover {{
            background: rgba(6, 182, 212, 0.3) !important;
        }}
        .grid-cell.solved {{
            background: rgba(0, 255, 65, 0.25) !important;
            color: #00ff41;
            text-shadow: 0 0 5px #00ff41;
        }}
        .grid-cell.selected {{
            border: 1px solid #00ff41;
            background: rgba(6, 182, 212, 0.5) !important;
            color: #00ff41;
        }}

        .clue-list-item {{
            cursor: pointer;
            transition: all 0.2s;
            border-left: 2px solid transparent;
        }}
        .clue-list-item:hover {{
            background: rgba(6, 182, 212, 0.1);
            border-left: 2px solid #06b6d4;
        }}
        .clue-list-item.selected {{
            background: rgba(6, 182, 212, 0.2);
            border-left: 2px solid #00ff41;
            color: #00ff41;
        }}
        .clue-list-item.solved {{
            opacity: 0.5;
            text-decoration: line-through;
            color: #00ff41;
        }}
    </style>
</head>
<body class="p-4 md:p-8 flex flex-col relative">
    <div class="scanline"></div>
    <div class="cyber-grid fixed inset-0 pointer-events-none -z-10"></div>

    <div id="game-container" class="max-w-7xl mx-auto w-full flex-grow flex flex-col z-10">
        <!-- Persistent Header -->
        <header class="flex flex-col md:flex-row justify-between items-center mb-6 border-b border-cyan-900 pb-4">
            <div>
                <h1 class="text-3xl font-bold orbitron glitch tracking-widest text-cyan-400">CYBER<span class="text-green-400">VERSE</span></h1>
                <p class="text-xs text-cyan-700 mt-1 uppercase tracking-widest">Crossword Defense Protocol</p>
            </div>
            
            <div id="live-stats" class="hidden flex gap-8 text-center mt-4 md:mt-0">
                <div class="bg-slate-900 bg-opacity-50 p-2 px-4 rounded border border-cyan-900">
                    <div class="text-xl orbitron text-green-400" id="stat-score">0</div>
                    <div class="text-[10px] uppercase text-green-700">Credits</div>
                </div>
                <div class="bg-slate-900 bg-opacity-50 p-2 px-4 rounded border border-cyan-900">
                    <div class="text-xl orbitron text-cyan-400" id="timer">00:00</div>
                    <div class="text-[10px] uppercase text-cyan-700">Uptime</div>
                </div>
                <div class="bg-slate-900 bg-opacity-50 p-2 px-4 rounded border border-cyan-900">
                    <div class="text-xl orbitron text-yellow-400" id="stat-team">---</div>
                    <div class="text-[10px] uppercase text-yellow-700">Link ID</div>
                </div>
            </div>

            <div class="flex gap-4 items-center mt-4 md:mt-0">
                <button onclick="surrenderGame()" id="surrender-btn" class="hidden-view text-[10px] border border-red-900 px-3 py-1 hover:bg-red-900 hover:text-white transition-all font-bold orbitron text-red-500 mr-2">SUBMIT EARLY</button>
                <button onclick="openAdmin()" class="text-[10px] border border-cyan-900 px-3 py-1 hover:bg-cyan-900 hover:text-cyan-400 transition-all font-bold orbitron text-cyan-700">OVERSEER</button>
            </div>
        </header>

        <!-- 1. LANDING/REGISTRATION VIEW -->
        <div id="view-auth" class="flex flex-col items-center justify-center flex-grow space-y-8 animate-in fade-in">
            <div class="text-center space-y-2">
                <i data-lucide="terminal-square" class="w-16 h-16 text-cyan-400 mx-auto mb-4 font-bold animate-pulse"></i>
                <h2 class="text-4xl orbitron text-cyan-400 drop-shadow-md">AGENT REGISTRATION</h2>
                <p class="text-cyan-600">Enter your credentials to decrypt the network grid.</p>
            </div>
            <div class="cyber-card p-8 w-full max-w-md space-y-6 rounded-xl">
                <div>
                    <label class="block text-[10px] font-bold tracking-widest uppercase mb-1 text-cyan-600">Team Name</label>
                    <input type="text" id="reg-team" class="terminal-input w-full p-2 text-xl uppercase" placeholder="ENTER TEAM NAME">
                </div>
                <div class="grid grid-cols-2 gap-4">
                    <div>
                        <label class="block text-[10px] font-bold tracking-widest uppercase mb-1 text-cyan-600">Operative 01</label>
                        <input type="text" id="reg-p1" class="terminal-input w-full p-2 text-sm uppercase" placeholder="ALIAS">
                    </div>
                    <div>
                        <label class="block text-[10px] font-bold tracking-widest uppercase mb-1 text-cyan-600">Operative 02</label>
                        <input type="text" id="reg-p2" class="terminal-input w-full p-2 text-sm uppercase" placeholder="ALIAS">
                    </div>
                </div>
                <button onclick="startGame()" class="w-full py-4 bg-cyan-700 text-black orbitron font-bold text-lg hover:bg-cyan-400 transition-all shadow-[0_0_15px_rgba(6,182,212,0.4)] rounded">INITIALIZE UPLINK</button>
                <p class="text-[10px] text-center text-red-400 hidden font-bold" id="reg-error">Error: Please fill all fields.</p>
                <div class="bg-cyan-900 bg-opacity-20 p-2 rounded border border-cyan-800 text-[10px] text-center text-cyan-500 mt-2">
                    <i data-lucide="alert-circle" class="w-3 h-3 inline mr-1"></i>Connecting will require full screen mode. Escaping full screen will flag your session.
                </div>
            </div>
        </div>

        <!-- 2. MAIN GAME VIEW -->
        <div id="view-game" class="hidden-view flex-grow flex flex-col pointer-events-none opacity-50 transition-opacity duration-1000" style="filter: blur(5px);">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 flex-grow min-h-0">
                
                <!-- Left Panel -->
                <div class="lg:col-span-3 space-y-4 flex flex-col h-full pointer-events-auto min-h-0">
                    <div class="cyber-card p-5 flex flex-col rounded-xl flex-shrink-0 relative overflow-hidden">
                        <div class="absolute top-0 right-0 p-2 opacity-10 pointer-events-none"><i data-lucide="crosshair" class="w-16 h-16"></i></div>
                        <h3 class="orbitron text-cyan-400 mb-3 border-b border-cyan-900 pb-2 flex justify-between uppercase">
                            <span>DECRYPT NODE</span>
                            <span id="active-attempts" class="text-[10px] font-bold text-yellow-500 pt-1"></span>
                        </h3>
                        
                        <div id="active-q-container" class="hidden">
                            <p class="text-[11px] font-bold text-cyan-500 mb-1 tracking-widest bg-cyan-900 bg-opacity-30 inline-block px-2 py-0.5 rounded" id="active-q-type"></p>
                            <p class="text-sm text-cyan-100 mb-4 h-16 overflow-y-auto" id="active-q-hint"></p>
                            
                            <!-- Python Code Hint Area -->
                            <div id="active-q-python" class="hidden mb-4 p-2 bg-[#020617] border border-cyan-700 rounded text-[10px] font-mono text-cyan-300 overflow-x-auto whitespace-pre"></div>
                            
                            <input type="text" id="ans-input" class="terminal-input w-full p-2 text-xl font-bold uppercase tracking-widest mb-3 bg-black bg-opacity-30 rounded border border-cyan-900" placeholder="KEY...">
                            
                            <div class="flex gap-2">
                                <button onclick="submitAnswer()" class="flex-grow py-3 bg-cyan-900 hover:bg-cyan-700 text-cyan-400 hover:text-white orbitron font-bold border border-cyan-500 transition-all text-xs rounded tracking-widest">CRACK CIPHER</button>
                                <button id="hint-btn" onclick="takeHint()" class="hidden py-3 px-4 bg-yellow-900 bg-opacity-50 hover:bg-yellow-800 text-yellow-500 hover:text-yellow-300 orbitron font-bold border border-yellow-700 transition-all text-xs rounded tracking-widest" title="Get Hint (-10 Points)">HINT (-10)</button>
                            </div>
                            
                            <p id="ans-feedback" class="text-[10px] mt-2 text-center h-4 text-red-500 font-bold uppercase tracking-widest"></p>
                        </div>
                        <div id="no-q-container" class="text-center py-10 text-cyan-900 opacity-70">
                            <i data-lucide="lock" class="w-10 h-10 mx-auto mb-3"></i>
                            <p class="text-[10px] uppercase font-bold tracking-widest">Select a node from the grid or list</p>
                        </div>
                    </div>

                    <div class="cyber-card p-4 flex-grow flex flex-col overflow-hidden rounded-xl">
                        <h3 class="orbitron text-cyan-500 mb-2 text-xs border-b border-cyan-900 pb-2 flex items-center gap-2 tracking-widest"><i data-lucide="activity" class="w-4 h-4"></i> LIVE FEED</h3>
                        <div class="overflow-y-auto flex-grow text-xs space-y-1 pr-2 custom-scrollbar" id="live-scoreboard-list"></div>
                    </div>
                </div>

                <!-- Middle Panel: Crossword Grid -->
                <div class="lg:col-span-6 flex flex-col items-center justify-start pointer-events-auto h-full min-h-0 bg-black bg-opacity-40 p-4 rounded-xl border border-cyan-900 border-opacity-50 overflow-auto custom-scrollbar">
                    <div id="grid-root" class="grid-container w-full h-auto"></div>
                </div>

                <!-- Right Panel: Clues List -->
                <div class="lg:col-span-3 cyber-card flex flex-col pointer-events-auto overflow-hidden rounded-xl min-h-0">
                    <h3 class="orbitron text-cyan-400 p-3 bg-cyan-900 bg-opacity-20 border-b border-cyan-900 text-xs flex justify-between items-center tracking-widest">
                        <span><i data-lucide="list" class="w-4 h-4 inline mr-1"></i> INTERCEPTED LOGS</span>
                    </h3>
                    <div class="overflow-y-auto flex-grow custom-scrollbar p-3 space-y-4">
                        <div>
                            <h4 class="text-green-500 font-bold text-xs orbitron mb-2 uppercase tracking-widest sticky top-0 bg-[#020617] bg-opacity-95 py-1 z-10 border-b border-green-900">ACROSS</h4>
                            <div id="clues-across" class="space-y-1 text-xs text-cyan-100"></div>
                        </div>
                        <div>
                            <h4 class="text-green-500 font-bold text-xs orbitron mb-2 uppercase tracking-widest sticky top-0 bg-[#020617] bg-opacity-95 py-1 z-10 border-b border-green-900">DOWN</h4>
                            <div id="clues-down" class="space-y-1 text-xs text-cyan-100"></div>
                        </div>
                    </div>
                </div>

            </div>
        </div>

        <!-- 3. ADMIN VIEW -->
        <div id="view-admin" class="hidden-view space-y-6">
            <div class="flex justify-between items-end border-b border-cyan-900 pb-4">
                <h2 class="text-3xl orbitron text-cyan-400">OVERSEER CONSOLE</h2>
                <div class="space-x-2">
                    <button onclick="closeAdmin()" class="px-6 py-2 text-xs border border-cyan-500 text-cyan-400 hover:bg-cyan-900 hover:text-white transition-all font-bold tracking-widest rounded">EXIT</button>
                </div>
            </div>
            
            <div class="cyber-card overflow-hidden overflow-x-auto rounded-xl">
                <table class="w-full text-left text-xs whitespace-nowrap">
                    <thead class="bg-cyan-900 bg-opacity-30 orbitron text-[10px] text-cyan-400">
                        <tr>
                            <th class="p-4 rounded-tl-lg">SCORE</th>
                            <th class="p-4">TEAM NAME</th>
                            <th class="p-4">AGENTS</th>
                            <th class="p-4">TIME</th>
                            <th class="p-4">SOLVED</th>
                            <th class="p-4">FLAGS (ESC)</th>
                            <th class="p-4 rounded-tr-lg">ACTIONS</th>
                        </tr>
                    </thead>
                    <tbody id="admin-table-body" class="divide-y divide-cyan-900 border-t border-cyan-900 text-cyan-100"></tbody>
                </table>
            </div>
        </div>

    </div>

    <!-- Modals -->
    <div id="modal-overlay" class="fixed inset-0 bg-black bg-opacity-95 z-50 hidden flex flex-col items-center justify-center p-4">
        <div class="cyber-card max-w-lg w-full p-8 text-center rounded-xl border-cyan-400" id="modal-box">
            <i data-lucide="alert-triangle" class="w-12 h-12 text-yellow-500 mx-auto mb-4" id="modal-icon"></i>
            <h2 id="modal-title" class="text-3xl orbitron mb-4 text-cyan-400 glow">ALERT</h2>
            <p id="modal-body" class="mb-8 font-mono text-sm text-cyan-300 whitespace-pre-line"></p>
            <button onclick="closeModal()" class="px-8 py-3 border-2 border-green-500 text-green-400 hover:bg-green-500 hover:text-black transition-all orbitron uppercase tracking-widest text-xs font-bold rounded shadow-[0_0_15px_rgba(0,255,65,0.3)]">ACKNOWLEDGE</button>
        </div>
    </div>

    <script>
        {questions_js}

        const ADMIN_PASS = "admin123";
        const GRID_W = 23;
        const GRID_H = 25;
        
        let db = JSON.parse(localStorage.getItem('cyber_crossword_db') || '{{ "teams": [] }}');
        
        let state = {{
            teamId: null, 
            activeQ: null,
            timerInterval: null
        }};

        const saveDB = () => localStorage.setItem('cyber_crossword_db', JSON.stringify(db));

        window.onload = () => {{
            lucide.createIcons();
            populateCluesList();
            
            const sessionData = sessionStorage.getItem('cyber_active_session');
            if(sessionData) {{
                state.teamId = parseInt(sessionData);
                if(db.teams[state.teamId] && !db.teams[state.teamId].submitted) {{
                    resumeGame();
                }} else {{
                    state.teamId = null;
                    sessionStorage.removeItem('cyber_active_session');
                }}
            }}
        }};

        const populateCluesList = () => {{
            const across = QUESTIONS.filter(q => q.dir === 'across').sort((a,b) => a.display_id - b.display_id);
            const down = QUESTIONS.filter(q => q.dir === 'down').sort((a,b) => a.display_id - b.display_id);
            
            const renderList = (arr, containerId) => {{
                document.getElementById(containerId).innerHTML = arr.map(q => `
                    <div id="clue-${{q.id}}" class="clue-list-item p-2 rounded mb-1 flex items-start gap-2" onclick="selectQuestion('${{q.id}}')">
                        <span class="font-bold text-cyan-500 mt-0.5">${{q.display_id}}.</span>
                        <span class="leading-tight">${{q.hint}}</span>
                    </div>
                `).join('');
            }};
            
            renderList(across, 'clues-across');
            renderList(down, 'clues-down');
        }};

        window.openAdmin = () => {{
            const pass = prompt("Enter Overseer Passcode:");
            if (pass === ADMIN_PASS) {{
                if(document.fullscreenElement) document.exitFullscreen();
                renderAdminTable();
                showView('view-admin');
            }} else if (pass !== null) {{
                alert("ACCESS DENIED");
            }}
        }};

        window.closeAdmin = () => {{
            if(state.teamId !== null) showView('view-game');
            else showView('view-auth');
        }};

        window.startGame = () => {{
            const t = document.getElementById('reg-team').value.trim();
            const p1 = document.getElementById('reg-p1').value.trim();
            const p2 = document.getElementById('reg-p2').value.trim();
            
            if(!t || !p1 || !p2) {{
                document.getElementById('reg-error').classList.remove('hidden');
                return;
            }}

            const newTeam = {{
                id: Date.now(),
                name: t,
                agent1: p1,
                agent2: p2,
                score: 0,
                time: 0,
                flags: 0,
                solved: [],
                hintsUsed: [],
                attempts: {{}},
                submitted: false
            }};

            db.teams.push(newTeam);
            state.teamId = db.teams.length - 1;
            saveDB();
            sessionStorage.setItem('cyber_active_session', state.teamId);

            enterFullscreen().then(() => {{ resumeGame(); }}).catch(err => {{ resumeGame(); }});
        }};

        window.resumeGame = () => {{
            const team = db.teams[state.teamId];
            document.getElementById('stat-team').innerText = team.name.toUpperCase();
            document.getElementById('stat-score').innerText = team.score;
            document.getElementById('live-stats').classList.remove('hidden');
            document.getElementById('surrender-btn').classList.remove('hidden-view');
            
            showView('view-game');
            updateCluesUI();
            
            setTimeout(() => {{
                const gameView = document.getElementById('view-game');
                gameView.style.filter = 'blur(0px)';
                gameView.style.opacity = '1';
                gameView.classList.remove('pointer-events-none');
            }}, 500);

            renderGrid();
            startTimer();
            refreshScoreboard();
        }};

        window.surrenderGame = () => {{
            if(confirm("Are you sure you want to surrender? Your current score and time will be recorded as final.")) {{
                const team = db.teams[state.teamId];
                team.submitted = true;
                saveDB();
                
                clearInterval(state.timerInterval);
                state.teamId = null;
                sessionStorage.removeItem('cyber_active_session');
                
                showModal("MISSION COMPLETED", `Final Score: ${{team.score}}\\nSolved: ${{team.solved.length}} / ${{QUESTIONS.length}}\\nAwait further commands from Overseer.`);
                
                setTimeout(() => {{ location.reload(); }}, 3000);
            }}
        }};

        const enterFullscreen = () => {{
            const elem = document.documentElement;
            if (elem.requestFullscreen) return elem.requestFullscreen();
            if (elem.webkitRequestFullscreen) return elem.webkitRequestFullscreen();
            return Promise.resolve();
        }};

        document.addEventListener('fullscreenchange', (event) => {{
            if (!document.fullscreenElement && state.teamId !== null && document.getElementById('view-game').classList.contains('hidden-view') === false) {{
                db.teams[state.teamId].flags += 1;
                saveDB();
                showModal("PROTOCOL BREACH", "Full screen exit detected. Incident has been logged and flagged on the Overseer console.");
            }}
        }});

        window.startTimer = () => {{
            if(state.timerInterval) clearInterval(state.timerInterval);
            state.timerInterval = setInterval(() => {{
                const team = db.teams[state.teamId];
                team.time += 1;
                saveDB();
                updateTimerDisplay(team.time);
                if(team.time % 5 === 0) refreshScoreboard();
            }}, 1000);
        }};

        const updateTimerDisplay = (t) => {{
            const m = Math.floor(t / 60).toString().padStart(2, '0');
            const s = (t % 60).toString().padStart(2, '0');
            document.getElementById('timer').innerText = `${{m}}:${{s}}`;
        }};

        window.renderGrid = () => {{
            const root = document.getElementById('grid-root');
            const team = db.teams[state.teamId];
            root.innerHTML = '';
            
            for(let i=0; i<GRID_H*GRID_W; i++) {{
                const x = i % GRID_W;
                const y = Math.floor(i / GRID_W);
                
                // Get ALL questions that overlap this cell
                const overlappingQuestions = QUESTIONS.filter(q => q.dir === 'across' ? (y===q.y && x>=q.x && x<q.x+q.len) : (x===q.x && y>=q.y && y<q.y+q.len));
                const startMatch = QUESTIONS.find(q => q.x===x && q.y===y); // Starting label is just the first one
                
                let html = `<div class="grid-cell" id="cell-${{x}}-${{y}}">`;
                
                if(overlappingQuestions.length > 0) {{
                    // Determine if ANY overlapping question is solved
                    const solvedQ = overlappingQuestions.find(q => team.solved.includes(q.id));
                    
                    // The clickable question is the one currently active, or just default to the first one
                    const mainQ = (state.activeQ && overlappingQuestions.some(q => q.id === state.activeQ.id)) ? state.activeQ : overlappingQuestions[0];
                    const isSelected = state.activeQ && mainQ.id === state.activeQ.id;
                    
                    let letter = '';
                    if(solvedQ) {{
                        letter = solvedQ.dir === 'across' ? solvedQ.ans[x - solvedQ.x] : solvedQ.ans[y - solvedQ.y];
                    }}
                    
                    let classes = "active";
                    if(solvedQ) classes += " solved";
                    if(isSelected) classes += " selected";
                    
                    // We call selectQuestion with mainQ.id. 
                    // However, if the cell clicks two words, standard behavior highlights across first, down second on double click.
                    // For simplicity, just highlight mainQ
                    html = `<div class="grid-cell ${{classes}}" id="cell-${{x}}-${{y}}" onclick="selectQuestion('${{mainQ.id}}')">
                        ${{startMatch ? `<span style="position:absolute; top:0px; left:2px; font-size:clamp(6px, 0.8vw, 10px); color:#06b6d4;">${{startMatch.display_id}}</span>` : ''}}
                        <span>${{letter}}</span>
                    </div>`;
                }} else {{
                    html += `</div>`;
                }}
                
                root.innerHTML += html;
            }}
        }};

        window.selectQuestion = (qid) => {{
            const team = db.teams[state.teamId];
            if(team.solved.includes(qid)) return; 
            
            const q = QUESTIONS.find(x => x.id === qid);
            state.activeQ = q;
            
            document.getElementById('no-q-container').classList.add('hidden');
            document.getElementById('active-q-container').classList.remove('hidden');
            document.getElementById('active-q-type').innerText = `NODE [${{q.display_id}}] ${{q.dir.toUpperCase()}} // (${{q.len}} LETTERS)`;
            document.getElementById('active-q-hint').innerText = q.hint;
            
            checkHintVisibility();
            
            const inp = document.getElementById('ans-input');
            inp.value = '';
            inp.focus();
            document.getElementById('ans-feedback').innerText = '';
            
            renderGrid();
            updateCluesUI();
        }};

        const checkHintVisibility = () => {{
            const team = db.teams[state.teamId];
            const q = state.activeQ;
            if(!q) return;

            // Optional initialize
            if(!team.hintsUsed) team.hintsUsed = [];

            const attempts = team.attempts[q.id] || 0;
            document.getElementById('active-attempts').innerText = `Attempts: ${{attempts}}`;
            
            const btn = document.getElementById('hint-btn');
            const pythonBox = document.getElementById('active-q-python');

            if(team.hintsUsed.includes(q.id)) {{
                // Hint already revealed
                btn.classList.add('hidden');
                pythonBox.classList.remove('hidden');
                pythonBox.innerText = q.pythonHint || "No script available for this node.";
            }} else {{
                pythonBox.classList.add('hidden');
                pythonBox.innerText = "";
                // Show hint button after 2 attempts
                if(attempts >= 2) {{
                    btn.classList.remove('hidden');
                }} else {{
                    btn.classList.add('hidden');
                }}
            }}
        }};

        window.takeHint = () => {{
            const team = db.teams[state.teamId];
            const q = state.activeQ;
            if(!q) return;

            if(!team.hintsUsed) team.hintsUsed = [];

            if(!team.hintsUsed.includes(q.id)) {{
                team.score -= 10;
                document.getElementById('stat-score').innerText = team.score;
                team.hintsUsed.push(q.id);
                saveDB();
                checkHintVisibility();
                
                document.getElementById('ans-feedback').className = "text-[10px] mt-2 h-4 text-yellow-500 font-bold uppercase tracking-widest";
                document.getElementById('ans-feedback').innerText = "HINT ACTIVATED. PENALTY: -10 PTS.";
                setTimeout(() => {{
                    document.getElementById('ans-feedback').innerText = "";
                }}, 3000);
            }}
        }};

        const updateCluesUI = () => {{
            const team = db.teams[state.teamId];
            QUESTIONS.forEach(q => {{
                const el = document.getElementById(`clue-${{q.id}}`);
                if(!el) return;
                
                el.classList.remove('selected', 'solved');
                
                if(team.solved.includes(q.id)) {{
                    el.classList.add('solved');
                }} else if(state.activeQ && state.activeQ.id === q.id) {{
                    el.classList.add('selected');
                    el.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
                }}
            }});
        }};

        window.submitAnswer = () => {{
            if(!state.activeQ) return;
            const team = db.teams[state.teamId];
            const q = state.activeQ;
            const inp = document.getElementById('ans-input').value.trim().toUpperCase().replace(/\s/g, '');
            const ans = q.ans.toUpperCase().replace(/\s/g, '');
            
            if(!inp) return;

            const attempts = team.attempts[q.id] || 0;
            team.attempts[q.id] = attempts + 1;
            
            if(inp === ans) {{
                team.solved.push(q.id);
                team.score += 50; 
                document.getElementById('stat-score').innerText = team.score;
                document.getElementById('ans-feedback').className = "text-[10px] mt-2 h-4 text-green-400 font-bold uppercase tracking-widest";
                document.getElementById('ans-feedback').innerText = "DECRYPTION SUCCESSFUL.";
                
                setTimeout(() => {{
                    state.activeQ = null;
                    document.getElementById('active-q-container').classList.add('hidden');
                    document.getElementById('no-q-container').classList.remove('hidden');
                    renderGrid();
                    updateCluesUI();
                    refreshScoreboard();
                    checkWinCondition();
                }}, 1000);
            }} else {{
                team.score -= 5; 
                document.getElementById('stat-score').innerText = team.score;
                document.getElementById('ans-feedback').className = "text-[10px] mt-2 h-4 text-red-500 font-bold uppercase tracking-widest animate-pulse";
                document.getElementById('ans-feedback').innerText = "ACCESS DENIED. PENALTY: -5 PTS.";
                document.getElementById('ans-input').value = '';
                
                checkHintVisibility(); // Update attempts and hint button
            }}
            
            saveDB();
        }};
        
        const checkWinCondition = () => {{
            const team = db.teams[state.teamId];
            if(team.solved.length >= QUESTIONS.length) {{
                team.submitted = true;
                saveDB();
                clearInterval(state.timerInterval);
                state.teamId = null;
                sessionStorage.removeItem('cyber_active_session');
                showModal("MISSION ACCOMPLISHED", `Grid fully decrypted.\\nFinal Score: ${{team.score}}\\nTime: ${{document.getElementById('timer').innerText}}\\n\\nAwait further commands.`);
            }}
        }};

        const refreshScoreboard = () => {{
            const list = document.getElementById('live-scoreboard-list');
            list.innerHTML = '';
            
            const sorted = [...db.teams].sort((a,b) => b.score - a.score || a.time - b.time);
            
            sorted.forEach((t, i) => {{
                // Skip if not started or something, but we show everyone. Or skip submitted? No, show all.
                const m = Math.floor(t.time / 60).toString().padStart(2, '0');
                const s = (t.time % 60).toString().padStart(2, '0');
                const timeStr = `${{m}}:${{s}}`;
                
                const isMe = state.teamId !== null && db.teams[state.teamId] && db.teams[state.teamId].id === t.id;
                
                list.innerHTML += `
                    <div class="flex justify-between items-center p-2 rounded border mb-1 ${{isMe ? 'bg-cyan-900 border-cyan-500 bg-opacity-30' : 'border-cyan-900 border-opacity-30'}} transition-all">
                        <div class="truncate max-w-[50%]">
                            <span class="font-bold text-cyan-600 mr-1">${{i+1}}.</span>
                            <span class="uppercase tracking-widest text-white font-bold text-[10px]">${{t.name}}</span>
                        </div>
                        <div class="text-right flex-shrink-0">
                            <span class="text-green-400 font-bold">${{t.score}}</span> <span class="text-cyan-900 mx-1">|</span> <span class="text-cyan-600">${{timeStr}}</span>
                            ${{t.submitted ? `<span class="ml-1 text-yellow-500 font-bold text-[8px]">[DONE]</span>` : ''}}
                        </div>
                    </div>
                `;
            }});
        }};

        // --- UTILS ---
        window.showView = (vId) => {{
            ['view-auth', 'view-game', 'view-admin'].forEach(id => {{
                document.getElementById(id).classList.add('hidden-view');
            }});
            document.getElementById(vId).classList.remove('hidden-view');
        }};

        window.showModal = (t, b) => {{
            document.getElementById('modal-title').innerText = t;
            document.getElementById('modal-body').innerText = b;
            document.getElementById('modal-overlay').classList.remove('hidden');
        }};

        window.closeModal = () => document.getElementById('modal-overlay').classList.add('hidden');

        // --- ADMIN FUNCTIONS ---
        window.renderAdminTable = () => {{
            const body = document.getElementById('admin-table-body');
            body.innerHTML = '';
            
            db.teams.forEach((t, i) => {{
                const m = Math.floor(t.time / 60).toString().padStart(2, '0');
                const s = (t.time % 60).toString().padStart(2, '0');
                
                body.innerHTML += `
                    <tr class="hover:bg-cyan-900 hover:bg-opacity-20 transition-colors">
                        <td class="p-4 text-green-400 font-bold">${{t.score}}</td>
                        <td class="p-4 text-cyan-100 font-bold uppercase tracking-widest">${{t.name}}</td>
                        <td class="p-4 text-cyan-600 uppercase text-[10px]">${{t.agent1}} & ${{t.agent2}}</td>
                        <td class="p-4 font-mono text-cyan-300">${{m}}:${{s}}</td>
                        <td class="p-4 text-cyan-500">${{t.solved.length}} / ${{QUESTIONS.length}}</td>
                        <td class="p-4 ${{t.flags > 0 ? 'text-red-500 font-bold' : 'text-cyan-700'}}">${{t.flags}}</td>
                        <td class="p-4 space-x-3">
                            <button onclick="adminResetTime(${{i}})" class="text-yellow-500 hover:text-yellow-400 transition-colors" title="Reset Time"><i data-lucide="rotate-ccw" class="w-4 h-4"></i></button>
                            <button onclick="adminRemoveTeam(${{i}})" class="text-red-500 hover:text-red-400 transition-colors" title="Remove"><i data-lucide="trash-2" class="w-4 h-4"></i></button>
                        </td>
                    </tr>
                `;
            }});
            lucide.createIcons();
        }};
        
        window.adminResetTime = (i) => {{
            if(confirm("Reset team timer to zero?")) {{
                db.teams[i].time = 0;
                saveDB();
                renderAdminTable();
            }}
        }};

        window.adminRemoveTeam = (i) => {{
            if(confirm("Delete this team completely?")) {{
                db.teams.splice(i, 1);
                
                if(state.teamId === i) {{
                    state.teamId = null;
                    sessionStorage.removeItem('cyber_active_session');
                }} else if (state.teamId > i) {{
                    state.teamId--;
                    sessionStorage.setItem('cyber_active_session', state.teamId);
                }}
                
                saveDB();
                renderAdminTable();
            }}
        }};

    </script>
</body>
</html>
"""

# Write to the file
with open("c:/Users/sarjare/.gemini/antigravity/scratch/crosssword/index.html", "w") as f:
    f.write(html)
