import re

# Read the crossword grid data
with open("c:/Users/sarjare/.gemini/antigravity/scratch/crosssword/formatted_q.js", "r") as f:
    questions_js = f.read().split("\n\n")[0]

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
            background-color: #050505;
            color: #00ff41;
            font-family: 'Fira Code', monospace;
            overflow-x: hidden;
            min-height: 100vh;
        }}
        .orbitron {{ font-family: 'Orbitron', sans-serif; }}
        .cyber-card {{
            background: rgba(10, 10, 10, 0.9);
            border: 1px solid #00ff41;
            box-shadow: 0 0 15px rgba(0, 255, 65, 0.2);
        }}
        .terminal-input {{
            background: transparent;
            border: none;
            border-bottom: 2px solid #00ff41;
            outline: none;
            color: #00ff41;
        }}
        .glitch {{ animation: glitch 1s linear infinite; }}
        @keyframes glitch {{
            2%, 64% {{ transform: translate(2px, 0) skew(0deg); }}
            4%, 60% {{ transform: translate(-2px, 0) skew(0deg); }}
            62% {{ transform: translate(0, 0) skew(5deg); }}
        }}
        ::-webkit-scrollbar {{ width: 5px; }}
        ::-webkit-scrollbar-thumb {{ background: #00ff41; }}
        .hidden-view {{ display: none !important; }}
        
        .grid-container {{
            display: grid;
            grid-template-columns: repeat(23, minmax(0, 1fr));
            gap: 1px;
            background: #00ff4155;
            border: 1px solid #00ff41;
            padding: 1px;
        }}
        .grid-cell {{
            aspect-ratio: 1/1;
            background: #050505;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 10px;
            font-weight: bold;
            color: white;
            transition: all 0.2s;
        }}
        .grid-cell.active {{
            background: rgba(0,255,65,0.2) !important;
            cursor: pointer;
        }}
        .grid-cell.active:hover {{
            background: rgba(0,255,65,0.4) !important;
        }}
        .grid-cell.solved {{
            background: rgba(0,255,65,0.4) !important;
            color: #00ff41;
            text-shadow: 0 0 5px #00ff41;
        }}
        .grid-cell.selected {{
            border: 1px solid #00ff41;
            background: rgba(0,255,65,0.6) !important;
        }}
    </style>
</head>
<body class="p-4 md:p-8 flex flex-col">

    <div id="game-container" class="max-w-7xl mx-auto w-full flex-grow flex flex-col">
        <!-- Persistent Header -->
        <header class="flex flex-col md:flex-row justify-between items-center mb-6 border-b border-green-900 pb-4">
            <div>
                <h1 class="text-3xl font-bold orbitron glitch tracking-widest text-green-400">CYBER VERSE</h1>
                <p class="text-xs text-green-700 mt-1">CROSSWORD DEFENSE PROTOCOL</p>
            </div>
            
            <!-- Live Stats -->
            <div id="live-stats" class="hidden flex gap-8 text-center mt-4 md:mt-0">
                <div>
                    <div class="text-xl orbitron text-blue-400" id="stat-score">0</div>
                    <div class="text-[10px] uppercase text-blue-800">Score</div>
                </div>
                <div>
                    <div class="text-xl orbitron" id="timer">00:00</div>
                    <div class="text-[10px] uppercase text-green-800">Timer</div>
                </div>
                <div>
                    <div class="text-xl orbitron text-yellow-500" id="stat-team">---</div>
                    <div class="text-[10px] uppercase text-yellow-800">Team</div>
                </div>
            </div>

            <div class="flex gap-4 items-center mt-4 md:mt-0">
                <button onclick="openAdmin()" class="text-[10px] border border-green-900 px-2 py-1 hover:bg-green-900 transition-all">ADMIN</button>
            </div>
        </header>

        <!-- 1. LANDING/REGISTRATION VIEW -->
        <div id="view-auth" class="flex flex-col items-center justify-center flex-grow space-y-8 animate-in fade-in">
            <div class="text-center space-y-2">
                <i data-lucide="terminal" class="w-16 h-16 text-green-400 mx-auto mb-4 font-bold"></i>
                <h2 class="text-4xl orbitron text-green-400">AGENT REGISTRATION</h2>
                <p class="text-green-700">Enter your credentials to decrypt the network grid.</p>
            </div>
            <div class="cyber-card p-8 w-full max-w-md space-y-6">
                <div>
                    <label class="block text-xs uppercase mb-1 text-green-600">Team Name</label>
                    <input type="text" id="reg-team" class="terminal-input w-full p-2 text-xl uppercase" placeholder="ENTER TEAM NAME">
                </div>
                <div class="grid grid-cols-2 gap-4">
                    <div>
                        <label class="block text-xs uppercase mb-1 text-green-600">Agent 1</label>
                        <input type="text" id="reg-p1" class="terminal-input w-full p-2 text-sm uppercase" placeholder="NAME">
                    </div>
                    <div>
                        <label class="block text-xs uppercase mb-1 text-green-600">Agent 2</label>
                        <input type="text" id="reg-p2" class="terminal-input w-full p-2 text-sm uppercase" placeholder="NAME">
                    </div>
                </div>
                <button onclick="startGame()" class="w-full py-4 bg-green-600 text-black orbitron font-bold hover:bg-green-400 transition-all shadow-[0_0_15px_rgba(0,255,65,0.5)]">INITIALIZE UPLINK</button>
                <p class="text-[10px] text-center text-red-500 hidden" id="reg-error">Error: Please fill all fields.</p>
                <p class="text-[10px] text-center text-green-900 mt-2">Connecting will require full screen mode. Escaping full screen will flag your session.</p>
            </div>
        </div>

        <!-- 2. MAIN GAME VIEW -->
        <div id="view-game" class="hidden-view flex-grow flex flex-col pointer-events-none opacity-50 transition-opacity duration-1000" style="filter: blur(5px);">
            <div class="grid grid-cols-1 lg:grid-cols-4 gap-6 flex-grow">
                <!-- Left panel: Question input and Scoreboard -->
                <div class="lg:col-span-1 space-y-6 flex flex-col h-full pointer-events-auto">
                    <!-- Active Question Area -->
                    <div class="cyber-card p-6 flex flex-col">
                        <h3 class="orbitron text-green-400 mb-2 border-b border-green-900 pb-2 flex justify-between">
                            <span>DECRYPT NODE</span>
                            <span id="active-attempts" class="text-xs text-yellow-500"></span>
                        </h3>
                        
                        <div id="active-q-container" class="hidden">
                            <p class="text-xs text-green-500 mb-1" id="active-q-type"></p>
                            <p class="text-sm text-white mb-4" id="active-q-hint"></p>
                            
                            <input type="text" id="ans-input" class="terminal-input w-full p-2 text-lg uppercase tracking-widest mb-4" placeholder="ENTER DECRYPTION KEY">
                            <button onclick="submitAnswer()" class="w-full py-2 bg-green-900 hover:bg-green-700 text-white orbitron font-bold border border-green-500 transition-all text-xs">SUBMIT</button>
                            <p id="ans-feedback" class="text-xs mt-2 h-4 text-red-500"></p>
                        </div>
                        <div id="no-q-container" class="text-center py-8 text-green-900 opacity-50">
                            <i data-lucide="lock" class="w-8 h-8 mx-auto mb-2"></i>
                            <p class="text-[10px] uppercase">Select a node to decrypt</p>
                        </div>
                    </div>

                    <!-- Live Scoreboard -->
                    <div class="cyber-card p-4 flex-grow flex flex-col overflow-hidden">
                        <h3 class="orbitron text-blue-400 mb-2 text-xs border-b border-blue-900 pb-2">LIVE SCOREBOARD</h3>
                        <div class="overflow-y-auto flex-grow text-xs space-y-2 pr-2" id="live-scoreboard-list">
                            <!-- Populated dynamically -->
                        </div>
                    </div>
                </div>

                <!-- Right panel: Crossword Grid -->
                <div class="lg:col-span-3 flex items-center justify-center pointer-events-auto">
                    <div class="cyber-card p-6 w-full max-w-4xl">
                        <div id="grid-root" class="grid-container w-full h-auto"></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- 3. ADMIN VIEW -->
        <div id="view-admin" class="hidden-view space-y-6">
            <div class="flex justify-between items-end border-b border-green-900 pb-4">
                <h2 class="text-3xl orbitron text-yellow-500">OVERSEER CONSOLE</h2>
                <div class="space-x-2">
                    <button onclick="closeAdmin()" class="px-4 py-1 text-xs border border-gray-500 text-gray-500 hover:text-white">EXIT</button>
                </div>
            </div>
            
            <div class="cyber-card overflow-hidden overflow-x-auto">
                <table class="w-full text-left text-xs whitespace-nowrap">
                    <thead class="bg-green-900 bg-opacity-30 orbitron text-[10px] text-green-400">
                        <tr>
                            <th class="p-3">SCORE</th>
                            <th class="p-3">TEAM NAME</th>
                            <th class="p-3">AGENTS</th>
                            <th class="p-3">TIME</th>
                            <th class="p-3">SOLVED</th>
                            <th class="p-3">FLAGS (ESC)</th>
                            <th class="p-3">ACTIONS</th>
                        </tr>
                    </thead>
                    <tbody id="admin-table-body" class="divide-y divide-green-900 border-t border-green-900"></tbody>
                </table>
            </div>
        </div>

    </div>

    <!-- Modals -->
    <div id="modal-overlay" class="fixed inset-0 bg-black bg-opacity-95 z-50 hidden flex flex-col items-center justify-center p-4">
        <div class="cyber-card max-w-lg w-full p-8 text-center" id="modal-box">
            <i data-lucide="alert-triangle" class="w-12 h-12 text-yellow-500 mx-auto mb-4" id="modal-icon"></i>
            <h2 id="modal-title" class="text-2xl orbitron mb-4 text-green-400">ALERT</h2>
            <p id="modal-body" class="mb-6 font-mono text-sm text-gray-300"></p>
            <button onclick="closeModal()" class="px-8 py-2 border border-green-400 text-green-400 hover:bg-green-400 hover:text-black transition-all orbitron uppercase tracking-widest text-xs">ACKNOWLEDGE</button>
        </div>
    </div>

    <script>
        {questions_js}

        // --- GAME STATE ---
        const ADMIN_PASS = "admin123";
        const GRID_W = 23;
        const GRID_H = 25;
        
        // Use local storage to persist state across reloads/sessions in same browser
        let db = JSON.parse(localStorage.getItem('cyber_crossword_db') || '{{ "teams": [] }}');
        
        let state = {{
            teamId: null, // index in db.teams
            activeQ: null,
            timerInterval: null
        }};

        // Utility to save DB
        const saveDB = () => localStorage.setItem('cyber_crossword_db', JSON.stringify(db));

        // --- INIT & AUTH ---
        window.onload = () => {{
            lucide.createIcons();
            // Optional: If there's an active session in session storage, auto-login
            const sessionData = sessionStorage.getItem('cyber_active_session');
            if(sessionData) {{
                state.teamId = parseInt(sessionData);
                resumeGame();
            }}
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

            // Register new team
            const newTeam = {{
                id: Date.now(),
                name: t,
                agent1: p1,
                agent2: p2,
                score: 0,
                time: 0,
                flags: 0,
                solved: [],
                attempts: {{}}
            }};

            db.teams.push(newTeam);
            state.teamId = db.teams.length - 1;
            saveDB();
            sessionStorage.setItem('cyber_active_session', state.teamId);

            // Attempt fullscreen
            enterFullscreen().then(() => {{
                resumeGame();
            }}).catch(err => {{
                alert("Fullscreen required to play.");
                resumeGame(); // Proceed anyway if browser blocks, they will get flagged
            }});
        }};

        window.resumeGame = () => {{
            const team = db.teams[state.teamId];
            document.getElementById('stat-team').innerText = team.name.toUpperCase();
            document.getElementById('stat-score').innerText = team.score;
            document.getElementById('live-stats').classList.remove('hidden');
            
            showView('view-game');
            
            // "Unlock" animation
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

        // --- FULLSCREEN LOGIC ---
        const enterFullscreen = () => {{
            const elem = document.documentElement;
            if (elem.requestFullscreen) return elem.requestFullscreen();
            if (elem.webkitRequestFullscreen) return elem.webkitRequestFullscreen();
            return Promise.resolve();
        }};

        document.addEventListener('fullscreenchange', (event) => {{
            if (!document.fullscreenElement && state.teamId !== null && document.getElementById('view-game').classList.contains('hidden-view') === false) {{
                // Exited fullscreen while playing
                db.teams[state.teamId].flags += 1;
                saveDB();
                showModal("PROTOCOL BREACH", "Full screen exit detected. Incident has been logged and flagged on the Overseer console.");
            }}
        }});

        // --- GAMEPLAY ENGINE ---
        window.startTimer = () => {{
            if(state.timerInterval) clearInterval(state.timerInterval);
            state.timerInterval = setInterval(() => {{
                const team = db.teams[state.teamId];
                team.time += 1;
                saveDB();
                updateTimerDisplay(team.time);
                
                // Also update scoreboard every 5 seconds so they see others
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
                
                // Find if a cell belongs to any question
                const qMatch = QUESTIONS.find(q => q.dir === 'across' ? (y===q.y && x>=q.x && x<q.x+q.len) : (x===q.x && y>=q.y && y<q.y+q.len));
                const startMatch = QUESTIONS.find(q => q.x===x && q.y===y);
                
                let html = `<div class="grid-cell" id="cell-${{x}}-${{y}}">`;
                
                if(qMatch) {{
                    const solved = team.solved.includes(qMatch.id);
                    const isSelected = state.activeQ && state.activeQ.id === qMatch.id;
                    
                    let letter = '';
                    if(solved) {{
                        letter = qMatch.dir === 'across' ? qMatch.ans[x - qMatch.x] : qMatch.ans[y - qMatch.y];
                    }}
                    
                    let classes = "active";
                    if(solved) classes += " solved";
                    if(isSelected) classes += " selected";
                    
                    html = `<div class="grid-cell ${{classes}}" id="cell-${{x}}-${{y}}" onclick="selectQuestion('${{qMatch.id}}')">
                        ${{startMatch ? `<span style="position:absolute; top:1px; left:2px; font-size:6px; color:#06b6d4;">${{startMatch.display_id}}</span>` : ''}}
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
            if(team.solved.includes(qid)) return; // Already solved
            
            const q = QUESTIONS.find(x => x.id === qid);
            state.activeQ = q;
            
            document.getElementById('no-q-container').classList.add('hidden');
            document.getElementById('active-q-container').classList.remove('hidden');
            document.getElementById('active-q-type').innerText = `${{q.display_id}} ${{q.dir.toUpperCase()}} (${{q.len}} LETTERS)`;
            document.getElementById('active-q-hint').innerText = q.hint;
            
            const attempts = team.attempts[qid] || 0;
            document.getElementById('active-attempts').innerText = `Attempts: ${{attempts}}`;
            
            const inp = document.getElementById('ans-input');
            inp.value = '';
            inp.focus();
            document.getElementById('ans-feedback').innerText = '';
            
            renderGrid(); // Refresh to show selection
        }};

        window.submitAnswer = () => {{
            if(!state.activeQ) return;
            const team = db.teams[state.teamId];
            const q = state.activeQ;
            const inp = document.getElementById('ans-input').value.trim().toUpperCase().replace(/\s/g, '');
            const ans = q.ans.toUpperCase().replace(/\s/g, '');
            
            const attempts = team.attempts[q.id] || 0;
            team.attempts[q.id] = attempts + 1;
            
            if(inp === ans) {{
                // Correct
                team.solved.push(q.id);
                team.score += 50; // 50 points per word
                document.getElementById('stat-score').innerText = team.score;
                document.getElementById('ans-feedback').className = "text-xs mt-2 h-4 text-green-400";
                document.getElementById('ans-feedback').innerText = "DECRYPTION SUCCESSFUL.";
                
                setTimeout(() => {{
                    state.activeQ = null;
                    document.getElementById('active-q-container').classList.add('hidden');
                    document.getElementById('no-q-container').classList.remove('hidden');
                    renderGrid();
                    refreshScoreboard();
                    checkWinCondition();
                }}, 1000);
            }} else {{
                // Wrong
                team.score -= 5; // Penalty
                document.getElementById('stat-score').innerText = team.score;
                document.getElementById('ans-feedback').className = "text-xs mt-2 h-4 text-red-500 animate-pulse";
                document.getElementById('ans-feedback').innerText = "ACCESS DENIED. PENALTY: -5 PTS.";
                document.getElementById('active-attempts').innerText = `Attempts: ${{attempts + 1}}`;
            }}
            
            saveDB();
        }};
        
        const checkWinCondition = () => {{
            const team = db.teams[state.teamId];
            if(team.solved.length >= QUESTIONS.length) {{
                clearInterval(state.timerInterval);
                showModal("MISSION ACCOMPLISHED", `Grid fully decrypted.\\nFinal Score: ${{team.score}}\\nTime: ${{document.getElementById('timer').innerText}}\\n\\nAwait further commands.`);
            }}
        }};

        const refreshScoreboard = () => {{
            const list = document.getElementById('live-scoreboard-list');
            list.innerHTML = '';
            
            // Sort by score desc, time asc
            const sorted = [...db.teams].sort((a,b) => b.score - a.score || a.time - b.time);
            
            sorted.forEach((t, i) => {{
                // Only show Team Name
                const m = Math.floor(t.time / 60).toString().padStart(2, '0');
                const s = (t.time % 60).toString().padStart(2, '0');
                const timeStr = `${{m}}:${{s}}`;
                
                const isMe = state.teamId !== null && db.teams[state.teamId].id === t.id;
                
                list.innerHTML += `
                    <div class="flex justify-between items-center p-2 rounded border ${{isMe ? 'bg-blue-900 border-blue-500 bg-opacity-30' : 'border-gray-800'}}">
                        <div>
                            <span class="font-bold text-white mr-2">${{i+1}}.</span>
                            <span class="uppercase tracking-widest text-green-400 font-bold">${{t.name}}</span>
                        </div>
                        <div class="text-right">
                            <span class="text-blue-400">${{t.score}}</span> <span class="text-gray-500 mx-1">|</span> <span class="text-gray-400">${{timeStr}}</span>
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
                    <tr>
                        <td class="p-3 text-blue-400 font-bold">${{t.score}}</td>
                        <td class="p-3 text-green-400 font-bold uppercase">${{t.name}}</td>
                        <td class="p-3 text-gray-400 uppercase">${{t.agent1}} & ${{t.agent2}}</td>
                        <td class="p-3 font-mono">${{m}}:${{s}}</td>
                        <td class="p-3">${{t.solved.length}} / ${{QUESTIONS.length}}</td>
                        <td class="p-3 ${{t.flags > 0 ? 'text-red-500 font-bold' : 'text-gray-500'}}">${{t.flags}}</td>
                        <td class="p-3 space-x-2">
                            <button onclick="adminResetTime(${{i}})" class="text-yellow-500 hover:text-white" title="Reset Time"><i data-lucide="rotate-ccw" class="w-4 h-4"></i></button>
                            <button onclick="adminRemoveTeam(${{i}})" class="text-red-500 hover:text-white" title="Remove"><i data-lucide="trash-2" class="w-4 h-4"></i></button>
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
                saveDB();
                renderAdminTable();
            }}
        }};

    </script>
</body>
</html>
"""

# Write to correct workspace path
with open("c:/Users/sarjare/.gemini/antigravity/scratch/crosssword/index.html", "w") as f:
    f.write(html)
