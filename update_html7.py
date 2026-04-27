import json
import shutil

python_hints = {
    "BACKUPS": """word = "Bpauskc"\nresult = ""\nfor i in range(len(word)):\n    if i % 2 == 0:\n        result += word[i]\nfor i in range(len(word)):\n    if i % 2 != 0:\n        result += word[i]\nprint(result)""",
    "ANTIVIRUS": """word = "avitnorus"\nresult = ""\nfor i in range(len(word)-1, -1, -2):\n    result += word[i]\nfor i in range(len(word)-2, -1, -2):\n    result += word[i]\nprint(result)""",
    "THREATACTOR": """word = "Trhaet Aotcr"\nresult = ""\nfor i in range(0, len(word), 2):\n    result += word[i]\nfor i in range(1, len(word), 2):\n    result += word[i]\nprint(result)""",
    "DARKWEB": """word = "DWaerk b"\nresult = ""\nfor i in range(len(word)):\n    if i < len(word)//2:\n        result += word[i]\nfor i in range(len(word)-1, len(word)//2 - 1, -1):\n    result += word[i]\nprint(result)""",
    "SPAM": """word = "Smap"\nresult = ""\nfor i in range(0, len(word), 2):\n    result += word[i]\nfor i in range(1, len(word), 2):\n    result += word[i]\nprint(result)""",
    "DATABREACH": """word = "Daat Brehca"\nresult = ""\nfor i in range(len(word)):\n    if i % 3 != 0:\n        result += word[i]\nfor i in range(len(word)):\n    if i % 3 == 0:\n        result += word[i]\nprint(result)""",
    "SPYWARE": """word = "Sypawre"\nresult = ""\nfor i in range(len(word)-1, -1, -2):\n    result += word[i]\nfor i in range(len(word)-2, -1, -2):\n    result += word[i]\nprint(result)""",
    "ENCRYPTION": """word = "Enrcyptoin"\nresult = ""\nfor i in range(len(word)):\n    if i % 2 == 0:\n        result += word[i]\nfor i in range(len(word)):\n    if i % 2 != 0:\n        result += word[i]\nprint(result)""",
    "VPN": """word = "VPN"\nresult = ""\nfor i in range(len(word)):\n    result += chr(ord(word[i]) + i)\nprint(result)""",
    "BOTNET": """word = "Btonet"\nresult = ""\nfor i in range(1, len(word), 2):\n    result += word[i]\nfor i in range(0, len(word), 2):\n    result += word[i]\nprint(result)""",
    "CYBERSECURITY": """word = "Cybresuciryt"\nresult = ""\nfor i in range(0, len(word), 2):\n    result += word[i]\nfor i in range(1, len(word), 2):\n    result += word[i]\nprint(result)""",
    "SPOOFING": """word = "Sopofnig"\nresult = ""\nfor i in range(len(word)):\n    if i % 2 == 0:\n        result += word[i]\nfor i in range(len(word)):\n    if i % 2 != 0:\n        result += word[i]\nprint(result)""",
    "INSIDERTHREAT": """word = "Insdier Thraet"\nresult = ""\nfor i in range(len(word)):\n    if word[i] != " ":\n        result += word[i]\nprint(result[:7] + " " + result[7:])""",
    "AUTHENTICATION": """word = "Auhteitacntion"\nresult = ""\nfor i in range(0, len(word), 2):\n    result += word[i]\nfor i in range(1, len(word), 2):\n    result += word[i]\nprint(result)""",
    "PASSWORD": """word = "Psaowrsd"\nresult = ""\nfor i in range(len(word)):\n    if i % 2 == 0:\n        result += word[i]\nfor i in range(len(word)):\n    if i % 2 != 0:\n        result += word[i]\nprint(result)""",
    "VULNERABILITY": """word = "Vunelarbility"\nresult = ""\nfor i in range(0, len(word), 2):\n    result += word[i]\nfor i in range(1, len(word), 2):\n    result += word[i]\nprint(result)""",
    "RANSOMWARE": """word = "Rnasomawre"\nresult = ""\nfor i in range(len(word)-1, -1, -1):\n    result += word[i]\nprint(result)""",
    "MALWARE": """word = "Malwrae"\nresult = ""\nfor i in range(1, len(word), 2):\n    result += word[i]\nfor i in range(0, len(word), 2):\n    result += word[i]\nprint(result)""",
    "FIREWALL": """word = "Fireawll"\nresult = ""\nfor i in range(len(word)):\n    if i != 4:\n        result += word[i]\nprint(result)""",
    "VIRUS": """word = "Vrius"\nresult = ""\nfor i in range(len(word)):\n    if i % 2 == 0:\n        result += word[i]\nfor i in range(len(word)):\n    if i % 2 != 0:\n        result += word[i]\nprint(result)""",
    "PASSKEY": """word = "Psaesky"\nresult = ""\nfor i in range(len(word)):\n    if i % 2 == 0:\n        result += word[i]\nfor i in range(len(word)):\n    if i % 2 != 0:\n        result += word[i]\nprint(result)""",
    "HACKER": """word = "Hakc er"\nresult = ""\nfor ch in word:\n    if ch != " ":\n        result += ch\nprint(result)""",
    "PHISHING": """word = "Pihsihng"\nresult = ""\nfor i in range(len(word)):\n    if i % 2 == 0:\n        result += word[i]\nfor i in range(len(word)):\n    if i % 2 != 0:\n        result += word[i]\nprint(result)""",
    "PRIVACY": """word = "Prvica y"\nresult = ""\nfor ch in word:\n    if ch != " ":\n        result += ch\nprint(result)"""
}

with open("c:/Users/sarjare/.gemini/antigravity/scratch/crosssword/best_layout.json", "r") as f:
    best = json.load(f)

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
            margin: 0;
            display: flex;
            flex-direction: column;
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
            animation: scan 2s linear infinite; 
            box-shadow: 0 0 15px rgba(6, 182, 212, 0.5);
            display: none; 
        }}
        @keyframes scan {{ 0% {{ top: -10px; }} 100% {{ top: 100%; }} }}

        .cyber-card {{
            background: rgba(10, 15, 30, 0.8);
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
        ::-webkit-scrollbar {{ width: 5px; height: 5px; }}
        ::-webkit-scrollbar-thumb {{ background: #06b6d4; }}
        .hidden-view {{ display: none !important; }}
        
        /* Grid container comfy settings */
        .grid-container {{
            display: grid;
            grid-template-columns: repeat(23, minmax(0, 1fr));
            grid-template-rows: repeat(25, minmax(0, 1fr));
            gap: 1.5px;
            
            /* Restoring classic visualization */
            background: rgba(6, 182, 212, 0.2);
            border: 2px solid #06b6d4;
            padding: 2px;
            
            width: auto;
            height: auto;
            max-width: 100%;
            max-height: 100%;
            margin: 0 auto;
        }}
        .grid-cell {{
            /* Perfect squares using aspect ratio instead of stretching */
            width: min(3vw, 24px);
            height: min(3vw, 24px);
            background: #020617;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: min(1.5vw, 14px);
            font-weight: bold;
            color: white;
            transition: all 0.2s;
        }}
        
        @media (max-width: 1024px) {{
            .grid-container {{ max-height: 60vh; max-width: 100%; }}
            .grid-cell {{ width: min(4vw, 20px); height: min(4vw, 20px); font-size: 10px; }}
        }}
        
        .grid-cell.active {{
            background: rgba(6, 182, 212, 0.15) !important;
            cursor: pointer;
        }}
        .grid-cell.active:hover {{
            background: rgba(6, 182, 212, 0.3) !important;
            transform: scale(1.1);
            z-index: 10;
        }}
        .grid-cell.solved {{
            background: rgba(0, 255, 65, 0.25) !important;
            color: #00ff41;
            text-shadow: 0 0 5px #00ff41;
        }}
        .grid-cell.selected {{
            border: 2px solid #00ff41;
            background: rgba(6, 182, 212, 0.5) !important;
            color: #00ff41;
            transform: scale(1.1);
            z-index: 10;
            box-shadow: 0 0 10px rgba(0,255,65,0.4);
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
        
        .main-workspace {{
            height: calc(100vh - 100px); 
        }}
        
        /* Draggable Header Style */
        .cursor-move {{ cursor: grab; }}
        .cursor-move:active {{ cursor: grabbing; }}
    </style>
</head>
<body class="p-4 md:p-6 relative text-white">
    <div class="scanline" id="scanline"></div>
    <div class="cyber-grid fixed inset-0 pointer-events-none -z-10"></div>

    <!-- DRAGGABLE PROMPT POPUP -->
    <div id="decrypt-prompt" class="hidden absolute z-50 cyber-card rounded-xl shadow-[0_0_20px_rgba(6,182,212,0.5)] border-cyan-400 w-full max-w-sm flex flex-col bg-[#020617] bg-opacity-95 backdrop-blur-md" style="top: 25%; left: 50%; transform: translate(-50%, -50%);">
        <div id="decrypt-prompt-header" class="cursor-move border-b border-cyan-800 pb-2 flex justify-between items-center select-none bg-cyan-900 bg-opacity-20 p-3 rounded-t-xl hover:bg-opacity-40 transition-colors">
            <span class="orbitron text-xs text-cyan-400 font-bold tracking-widest flex items-center">
                <i data-lucide="move" class="w-4 h-4 mr-2 text-cyan-600"></i> UPLINK ACTIVE
            </span>
            <button onclick="closePrompt()" class="text-cyan-600 hover:text-white transition-colors"><i data-lucide="x" class="w-4 h-4"></i></button>
        </div>
        
        <div class="p-4 flex flex-col pt-2">
            <h3 class="orbitron text-cyan-500 mb-2 border-b border-cyan-900 pb-2 flex justify-between uppercase text-xs items-center">
                <span id="active-q-type" class="font-bold relative bottom-[1px]"></span>
                <span id="active-attempts" class="text-[10px] font-bold text-yellow-500 bg-yellow-900 bg-opacity-30 px-2 py-0.5 rounded"></span>
            </h3>
            
            <p class="text-sm text-cyan-100 mb-3 leading-tight font-bold" id="active-q-hint"></p>
            
            <div id="active-q-python" class="hidden mb-3 p-3 bg-[#0a0f1e] border border-cyan-800 rounded-md text-[10px] font-mono text-cyan-300 overflow-x-auto whitespace-pre shadow-inner"></div>
            
            <input type="text" id="ans-input" class="terminal-input w-full p-3 text-lg font-bold uppercase tracking-widest bg-black bg-opacity-50 rounded border border-cyan-700 focus:border-green-500 focus:shadow-[0_0_10px_rgba(0,255,65,0.2)] mb-3 transition-all" placeholder="DECRYPT KEY...">
            
            <div class="flex gap-2">
                <button onclick="submitAnswer()" class="flex-grow py-2.5 bg-cyan-800 hover:bg-cyan-600 text-white orbitron font-bold border border-cyan-500 transition-all text-xs rounded tracking-widest shadow-md">CRACK CIFER</button>
                <button id="hint-btn" onclick="takeHint()" class="hidden py-2.5 px-4 bg-yellow-900 bg-opacity-70 hover:bg-yellow-700 text-yellow-400 hover:text-white orbitron font-bold border border-yellow-500 transition-all text-xs rounded tracking-widest shadow-md" title="Get Hint (-10 Points)">HINT (-10)</button>
            </div>
            
            <p id="ans-feedback" class="text-[10px] h-3 text-center text-red-500 font-bold uppercase tracking-widest mt-2"></p>
        </div>
    </div>

    <!-- INSTRUCTIONS MODAL -->
    <div id="instructions-modal" class="fixed inset-0 bg-black bg-opacity-95 z-50 hidden flex flex-col items-center justify-center p-4">
        <div class="cyber-card max-w-2xl w-full p-8 rounded-xl border-blue-400">
            <div class="flex justify-between items-center mb-6">
                <h2 class="text-2xl orbitron text-blue-400 glow">MISSION PROTOCOLS</h2>
                <button onclick="closeInstructions()" class="text-gray-400 hover:text-white"><i data-lucide="x" class="w-6 h-6"></i></button>
            </div>
            <div class="space-y-4 font-mono text-sm text-cyan-100 leading-relaxed max-h-[60vh] overflow-y-auto custom-scrollbar pr-4">
                <p><span class="text-green-400 font-bold">1. OBJECTIVE:</span> Fully decrypt the network grid. Missing nodes carry specific clues related to cyber defense operations.</p>
                <p><span class="text-green-400 font-bold">2. SELECTION:</span> Click directly on any node in the grid, or select an intercepted log from the side panel to lock onto a target.</p>
                <p><span class="text-green-400 font-bold">3. DECRYPTION CONSOLE:</span> When a target is selected, a floating, draggable uplink console will appear. Type your answer to attempt decryption. There is no penalty for incorrect guesses.</p>
                <p><span class="text-green-400 font-bold">4. ASSISTANCE:</span> After 2 failed attempts on a single node, you may activate a HINT. This deducts <span class="text-yellow-500 font-bold">-10 credits</span> but provides the exact Python extraction script for the answer.</p>
                <p><span class="text-green-400 font-bold">5. FULLSCREEN:</span> Connection requires fullscreen. Pressing ESC to exit fullscreen will log a protocol breach flag on the Overseer's dash.</p>
            </div>
            <button onclick="closeInstructions()" class="mt-8 w-full py-3 border border-blue-500 text-blue-400 hover:bg-blue-900 hover:text-white transition-all orbitron uppercase tracking-widest text-xs font-bold rounded">ACKNOWLEDGE</button>
        </div>
    </div>

    <div id="game-container" class="max-w-[1400px] mx-auto w-full flex-grow flex flex-col z-10 h-full">
        <!-- Persistent Header -->
        <header class="flex flex-col md:flex-row justify-between items-center mb-4 border-b border-cyan-900 pb-3 flex-shrink-0">
            <div>
                <h1 class="text-2xl font-bold orbitron glitch tracking-widest text-cyan-400">CYBER<span class="text-green-400">VERSE</span></h1>
                <p class="text-[10px] text-cyan-700 mt-0.5 uppercase tracking-widest">Crossword Defense Protocol</p>
            </div>
            
            <div id="live-stats" class="hidden flex gap-6 text-center mt-3 md:mt-0">
                <div class="bg-slate-900 bg-opacity-50 p-2 px-3 rounded border border-cyan-900">
                    <div class="text-lg orbitron text-green-400" id="stat-score">0</div>
                    <div class="text-[9px] uppercase text-green-700">Credits</div>
                </div>
                <div class="bg-slate-900 bg-opacity-50 p-2 px-3 rounded border border-cyan-900">
                    <div class="text-lg orbitron text-cyan-400" id="timer">00:00</div>
                    <div class="text-[9px] uppercase text-cyan-700">Uptime</div>
                </div>
                <div class="bg-slate-900 bg-opacity-50 p-2 px-3 rounded border border-cyan-900">
                    <div class="text-lg orbitron text-yellow-400" id="stat-team">---</div>
                    <div class="text-[9px] uppercase text-yellow-700">Link ID</div>
                </div>
            </div>

            <div class="flex gap-2 items-center mt-3 md:mt-0 flex-wrap justify-center">
                <button onclick="openInstructions()" class="text-[10px] border border-green-800 px-3 py-1.5 hover:bg-green-900 hover:text-green-400 transition-all font-bold orbitron text-green-500 rounded">INSTRUCTIONS</button>
                <button onclick="surrenderGame()" id="surrender-btn" class="hidden-view text-[10px] border border-red-900 px-3 py-1.5 hover:bg-red-900 hover:text-white transition-all font-bold orbitron text-red-500 rounded">SUBMIT EARLY</button>
                <button onclick="openLeaderboard()" id="leaderboard-btn" class="hidden-view text-[10px] border border-blue-900 px-3 py-1.5 hover:bg-blue-900 hover:text-white transition-all font-bold orbitron text-blue-400 rounded">LEADERBOARD</button>
                <button onclick="goAdminLogin()" class="text-[10px] border border-cyan-900 px-3 py-1.5 hover:bg-cyan-900 hover:text-cyan-400 transition-all font-bold orbitron text-cyan-700 rounded">OVERSEER</button>
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
            </div>
        </div>

        <!-- 2. MAIN GAME VIEW -->
        <div id="view-game" class="hidden-view main-workspace flex flex-col lg:flex-row gap-6 pointer-events-none opacity-50 transition-opacity duration-1000 w-full" style="filter: blur(5px);">
            
            <div class="lg:w-2/3 flex flex-col gap-4 h-full pointer-events-auto min-h-0">
                <!-- TOP: Crossword Grid Area (Comfy Square Cells) -->
                <div class="cyber-card flex-grow p-4 md:p-6 rounded-xl flex flex-col items-center justify-center relative bg-black bg-opacity-50 border-opacity-60 overflow-hidden shadow-inner">
                    <h3 class="absolute top-0 left-0 bg-cyan-900 bg-opacity-80 px-4 py-1.5 text-xs m-3 rounded-br-lg font-bold tracking-widest border-b border-r border-cyan-500 shadow-md">
                        <i data-lucide="layout-grid" class="w-3 h-3 inline mr-1"></i> NETWORK ARCHITECTURE
                    </h3>
                    <div id="grid-root" class="grid-container m-auto mt-8 relative"></div>
                </div>
            </div>

            <!-- RIGHT PANEL: Question Logs (Side-by-Side) -->
            <div class="lg:w-1/3 cyber-card flex flex-col pointer-events-auto rounded-xl overflow-hidden h-full">
                <h3 class="orbitron text-cyan-400 p-3 bg-cyan-900 bg-opacity-30 border-b border-cyan-500 text-xs flex justify-between items-center tracking-widest flex-shrink-0 shadow-sm">
                    <span><i data-lucide="list" class="w-4 h-4 inline mr-1"></i> INTERCEPTED LOGS</span>
                </h3>
                <div class="overflow-y-auto flex-grow custom-scrollbar p-3">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div>
                            <h4 class="text-green-400 font-bold text-xs orbitron mb-2 uppercase tracking-widest sticky top-0 bg-[#0a0f1e] py-1 z-10 border-b border-green-800">ACROSS</h4>
                            <div id="clues-across" class="space-y-1 text-[11px] text-cyan-100 flex flex-col"></div>
                        </div>
                        <div>
                            <h4 class="text-green-400 font-bold text-xs orbitron mb-2 uppercase tracking-widest sticky top-0 bg-[#0a0f1e] py-1 z-10 border-b border-green-800">DOWN</h4>
                            <div id="clues-down" class="space-y-1 text-[11px] text-cyan-100 flex flex-col"></div>
                        </div>
                    </div>
                </div>
            </div>

        </div>

        <!-- 3. LEADERBOARD TAB VIEW -->
        <div id="view-leaderboard" class="hidden-view flex flex-col items-center justify-start w-full h-full max-w-4xl mx-auto space-y-6">
            <!-- (omitted contents perfectly same) -->
            <div class="w-full flex justify-between items-end border-b border-cyan-900 pb-4">
                <h2 class="text-3xl orbitron text-blue-400">GLOBAL LEADERBOARD</h2>
                <button onclick="closeLeaderboard()" class="px-6 py-2 text-xs border border-cyan-500 text-cyan-400 hover:bg-cyan-900 hover:text-white transition-all font-bold tracking-widest rounded">BACK TO GAME</button>
            </div>
            <div class="cyber-card w-full p-4 rounded-xl flex-grow overflow-hidden flex flex-col">
                <div class="overflow-y-auto flex-grow text-sm space-y-2 pr-2 custom-scrollbar" id="full-leaderboard-list"></div>
            </div>
        </div>

        <!-- 4. ADMIN LOGIN VIEW -->
        <div id="view-admin-login" class="hidden-view flex flex-col items-center justify-center flex-grow space-y-8 animate-in fade-in">
            <!-- ... -->
            <div class="cyber-card p-10 w-full max-w-md space-y-6 rounded-xl border-yellow-600 text-center">
                <i data-lucide="shield-alert" class="w-16 h-16 text-yellow-500 mx-auto mb-4 font-bold"></i>
                <h2 class="text-3xl orbitron text-yellow-500 mb-6 drop-shadow-md">OVERSEER LOGIN</h2>
                <input type="password" id="admin-pass-input" class="terminal-input w-full p-3 text-2xl text-center tracking-widest mb-4 border-yellow-700 text-yellow-500 focus:border-yellow-400 focus:text-yellow-400" placeholder="PASSCODE">
                <div class="flex gap-4">
                    <button onclick="closeAdminLogin()" class="flex-1 py-3 border border-gray-600 text-gray-400 orbitron border-opacity-50 hover:bg-gray-800 rounded">CANCEL</button>
                    <button onclick="submitAdminLogin()" class="flex-1 py-3 bg-yellow-700 text-black orbitron font-bold hover:bg-yellow-500 transition-all rounded">ACCESS</button>
                </div>
                <p class="text-[10px] text-red-500 hidden" id="admin-error">ACCESS DENIED. VERIFY PASSCODE.</p>
            </div>
        </div>

        <!-- 5. ADMIN VIEW -->
        <div id="view-admin" class="hidden-view space-y-6">
            <!-- ... -->
            <div class="flex justify-between items-end border-b border-cyan-900 pb-4">
                <h2 class="text-3xl orbitron text-yellow-500">OVERSEER CONSOLE</h2>
                <button onclick="closeAdmin()" class="px-6 py-2 text-xs border border-cyan-500 text-cyan-400 hover:bg-cyan-900 hover:text-white transition-all font-bold tracking-widest rounded">EXIT</button>
            </div>
            
            <div class="cyber-card overflow-hidden overflow-x-auto rounded-xl border-yellow-900 border-opacity-50">
                <table class="w-full text-left text-xs whitespace-nowrap">
                    <thead class="bg-yellow-900 bg-opacity-20 orbitron text-[10px] text-yellow-500">
                        <tr>
                            <th class="p-4">SCORE</th>
                            <th class="p-4">TEAM NAME</th>
                            <th class="p-4">AGENTS</th>
                            <th class="p-4">TIME</th>
                            <th class="p-4">SOLVED</th>
                            <th class="p-4">FLAGS</th>
                            <th class="p-4">ACTIONS</th>
                        </tr>
                    </thead>
                    <tbody id="admin-table-body" class="divide-y divide-yellow-900 border-t border-yellow-900 text-cyan-100"></tbody>
                </table>
            </div>
        </div>

    </div>

    <!-- Modals (General) -->
    <div id="modal-overlay" class="fixed inset-0 bg-black bg-opacity-95 z-[999] hidden flex flex-col items-center justify-center p-4">
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
            setupDraggable();
            
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
        
        // --- DRAG LOGIC ---
        const setupDraggable = () => {{
            const promptEl = document.getElementById('decrypt-prompt');
            const headerEl = document.getElementById('decrypt-prompt-header');
            let startX, startY, startLeft, startTop;

            headerEl.addEventListener('mousedown', (e) => {{
                startX = e.clientX;
                startY = e.clientY;
                
                const rect = promptEl.getBoundingClientRect();
                promptEl.style.transform = 'none';
                promptEl.style.left = `${{rect.left}}px`;
                promptEl.style.top = `${{rect.top}}px`;
                
                startLeft = parseInt(promptEl.style.left, 10);
                startTop = parseInt(promptEl.style.top, 10);

                document.addEventListener('mousemove', onDrag);
                document.addEventListener('mouseup', stopDrag);
            }});

            function onDrag(e) {{
                const dx = e.clientX - startX;
                const dy = e.clientY - startY;
                promptEl.style.left = `${{startLeft + dx}}px`;
                promptEl.style.top = `${{startTop + dy}}px`;
            }}
            function stopDrag() {{
                document.removeEventListener('mousemove', onDrag);
                document.removeEventListener('mouseup', stopDrag);
            }}
        }};
        
        window.closePrompt = () => {{
            document.getElementById('decrypt-prompt').classList.add('hidden');
            state.activeQ = null;
            renderGrid();
            updateCluesUI();
        }};
        
        window.openInstructions = () => document.getElementById('instructions-modal').classList.remove('hidden');
        window.closeInstructions = () => document.getElementById('instructions-modal').classList.add('hidden');

        // ... (remaining standard scripts)
        const populateCluesList = () => {{
            const across = QUESTIONS.filter(q => q.dir === 'across').sort((a,b) => a.display_id - b.display_id);
            const down = QUESTIONS.filter(q => q.dir === 'down').sort((a,b) => a.display_id - b.display_id);
            
            const renderList = (arr, containerId) => {{
                document.getElementById(containerId).innerHTML = arr.map(q => `
                    <div id="clue-${{q.id}}" class="clue-list-item p-1.5 rounded mb-1 flex items-start gap-1.5 leading-snug" onclick="selectQuestion('${{q.id}}')">
                        <span class="font-bold text-cyan-500">${{q.display_id}}.</span>
                        <span>${{q.hint}}</span>
                    </div>
                `).join('');
            }};
            
            renderList(across, 'clues-across');
            renderList(down, 'clues-down');
        }};

        window.goAdminLogin = () => {{
            document.getElementById('admin-error').classList.add('hidden');
            document.getElementById('admin-pass-input').value = '';
            showView('view-admin-login');
        }};

        window.closeAdminLogin = () => {{
            if(state.teamId !== null) showView('view-game');
            else showView('view-auth');
        }};

        window.submitAdminLogin = () => {{
            const val = document.getElementById('admin-pass-input').value;
            if(val === ADMIN_PASS) {{
                if(document.fullscreenElement) document.exitFullscreen();
                renderAdminTable();
                showView('view-admin');
            }} else {{
                document.getElementById('admin-error').classList.remove('hidden');
            }}
        }};

        window.closeAdmin = () => {{
            if(state.teamId !== null) showView('view-game');
            else showView('view-auth');
        }};

        window.openLeaderboard = () => {{
            refreshScoreboard();
            showView('view-leaderboard');
        }};

        window.closeLeaderboard = () => {{
            showView('view-game');
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
            document.getElementById('leaderboard-btn').classList.remove('hidden-view');
            
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
                
                const overlappingQuestions = QUESTIONS.filter(q => q.dir === 'across' ? (y===q.y && x>=q.x && x<q.x+q.len) : (x===q.x && y>=q.y && y<q.y+q.len));
                const startMatch = QUESTIONS.find(q => q.x===x && q.y===y); 
                
                let html = `<div class="grid-cell" id="cell-${{x}}-${{y}}">`;
                
                if(overlappingQuestions.length > 0) {{
                    const solvedQ = overlappingQuestions.find(q => team.solved.includes(q.id));
                    const mainQ = (state.activeQ && overlappingQuestions.some(q => q.id === state.activeQ.id)) ? state.activeQ : overlappingQuestions[0];
                    const isSelected = state.activeQ && mainQ.id === state.activeQ.id;
                    
                    let letter = '';
                    if(solvedQ) {{
                        letter = solvedQ.dir === 'across' ? solvedQ.ans[x - solvedQ.x] : solvedQ.ans[y - solvedQ.y];
                    }}
                    
                    let classes = "active";
                    if(solvedQ) classes += " solved";
                    if(isSelected) classes += " selected";
                    
                    html = `<div class="grid-cell ${{classes}}" id="cell-${{x}}-${{y}}" onclick="selectQuestion('${{mainQ.id}}')">
                        ${{startMatch ? `<span style="position:absolute; top:2px; left:2px; line-height:1; font-size:clamp(6px, 0.7vw, 10px); color:#06b6d4;">${{startMatch.display_id}}</span>` : ''}}
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
            
            const promptEl = document.getElementById('decrypt-prompt');
            
            // Only re-center the prompt if it is currently hidden (closed)
            // If it is already open, leave it exactly where the user dragged it!
            if (promptEl.classList.contains('hidden')) {{
                promptEl.style.transform = "translate(-50%, -50%)";
                promptEl.style.left = "50%";
                promptEl.style.top = "25%";
                promptEl.classList.remove('hidden');
            }}
            
            document.getElementById('active-q-type').innerText = `NODE: [${{q.display_id}} ${{q.dir}}]`;
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

            if(!team.hintsUsed) team.hintsUsed = [];

            const attempts = team.attempts[q.id] || 0;
            document.getElementById('active-attempts').innerText = `Attempts: ${{attempts}}`;
            
            const btn = document.getElementById('hint-btn');
            const pythonBox = document.getElementById('active-q-python');

            if(team.hintsUsed.includes(q.id)) {{
                btn.classList.add('hidden');
                pythonBox.classList.remove('hidden');
                pythonBox.innerText = q.pythonHint || "No script available for this node.";
            }} else {{
                pythonBox.classList.add('hidden');
                pythonBox.innerText = "";
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
                
                document.getElementById('ans-feedback').className = "text-[10px] h-3 text-yellow-500 font-bold uppercase tracking-widest";
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

            const scan = document.getElementById('scanline');
            scan.style.display = 'block';

            const attempts = team.attempts[q.id] || 0;
            team.attempts[q.id] = attempts + 1;
            
            if(inp === ans) {{
                team.solved.push(q.id);
                team.score += 50; 
                document.getElementById('stat-score').innerText = team.score;
                document.getElementById('ans-feedback').className = "text-[10px] h-3 text-green-400 font-bold uppercase tracking-widest";
                document.getElementById('ans-feedback').innerText = "DECRYPTION SUCCESSFUL.";
                
                setTimeout(() => {{
                    scan.style.display = 'none'; 
                    closePrompt();
                    checkWinCondition();
                }}, 1200);
            }} else {{
                document.getElementById('ans-feedback').className = "text-[10px] h-3 text-red-500 font-bold uppercase tracking-widest animate-pulse";
                document.getElementById('ans-feedback').innerText = "ACCESS DENIED. INCORRECT KEY.";
                document.getElementById('ans-input').value = '';
                
                checkHintVisibility(); 
                
                setTimeout(() => {{ scan.style.display = 'none'; }}, 1200);
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
            const list = document.getElementById('full-leaderboard-list');
            if(!list) return;
            list.innerHTML = '';
            
            const sorted = [...db.teams].sort((a,b) => b.score - a.score || a.time - b.time);
            
            sorted.forEach((t, i) => {{
                const m = Math.floor(t.time / 60).toString().padStart(2, '0');
                const s = (t.time % 60).toString().padStart(2, '0');
                const timeStr = `${{m}}:${{s}}`;
                
                const isMe = state.teamId !== null && db.teams[state.teamId] && db.teams[state.teamId].id === t.id;
                
                list.innerHTML += `
                    <div class="flex justify-between items-center p-3 rounded border mb-2 text-base ${{isMe ? 'bg-cyan-900 border-cyan-500 bg-opacity-30' : 'border-cyan-900 border-opacity-30'}} transition-all">
                        <div class="truncate max-w-[50%]">
                            <span class="font-bold text-cyan-600 mr-2">${{i+1}}.</span>
                            <span class="uppercase tracking-widest text-white font-bold">${{t.name}}</span>
                        </div>
                        <div class="text-right flex-shrink-0">
                            <span class="text-green-400 font-bold">${{t.score}}</span> <span class="text-cyan-900 mx-2">|</span> <span class="text-cyan-600">${{timeStr}}</span>
                            ${{t.submitted ? `<span class="ml-2 text-yellow-500 font-bold text-[10px]">[SUBMITTED]</span>` : ''}}
                        </div>
                    </div>
                `;
            }});
        }};

        // --- UTILS ---
        window.showView = (vId) => {{
            ['view-auth', 'view-game', 'view-admin', 'view-leaderboard', 'view-admin-login'].forEach(id => {{
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
                    <tr class="hover:bg-yellow-900 hover:bg-opacity-20 transition-colors">
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
                }} else if (state.teamId && state.teamId > i) {{
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

with open("c:/Users/sarjare/.gemini/antigravity/scratch/crosssword/index.html", "w") as f:
    f.write(html)
    
shutil.copy("c:/Users/sarjare/.gemini/antigravity/scratch/crosssword/index.html", "c:/Users/sarjare/.gemini/antigravity/scratch/cyber_mission_game/index.html")
