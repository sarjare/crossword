import re

with open("c:/Users/sarjare/.gemini/antigravity/scratch/crosssword/formatted_q.js", "r") as f:
    questions_js = f.read().split("\n\n")[0]

html = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cyber Verse: The Codebreak Clash</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800&display=swap');
        :root { --neon-cyan: #06b6d4; --neon-red: #ef4444; --dark-bg: #020617; }
        body { font-family: 'JetBrains Mono', monospace; background-color: var(--dark-bg); color: #e2e8f0; overflow-x: hidden; }
        .cyber-grid { background-image: radial-gradient(var(--neon-cyan) 1px, transparent 0); background-size: 24px 24px; opacity: 0.05; }
        .glass-panel { background: rgba(15, 23, 42, 0.8); backdrop-filter: blur(12px); border: 1px solid rgba(6, 182, 212, 0.2); }
        .neon-text { text-shadow: 0 0 10px rgba(6, 182, 212, 0.5); }
        .grid-cell { aspect-ratio: 1/1; transition: all 0.2s ease; font-size: 10px; font-weight: bold; position: relative; }
        .custom-scrollbar::-webkit-scrollbar { width: 4px; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: var(--neon-cyan); border-radius: 10px; }
        .scanline { width: 100%; height: 2px; background: rgba(6, 182, 212, 0.05); position: fixed; top: 0; z-index: 100; pointer-events: none; animation: scan 6s linear infinite; }
        @keyframes scan { from { top: 0; } to { top: 100%; } }
    </style>
</head>
<body>
    <div class="scanline"></div>
    <div class="cyber-grid fixed inset-0 pointer-events-none"></div>
    <div id="notification-container" class="fixed top-20 right-4 z-[100] space-y-2 pointer-events-none"></div>

    <nav class="sticky top-0 z-50 glass-panel border-b border-cyan-900/40 px-4 py-3">
        <div class="max-w-7xl mx-auto flex justify-between items-center">
            <div class="flex items-center gap-3 cursor-pointer" onclick="router.navigate('landing')">
                <div class="p-2 bg-cyan-500/10 rounded border border-cyan-500/20"><i data-lucide="shield" class="text-cyan-400 w-5 h-5"></i></div>
                <div>
                    <h1 class="text-lg font-black tracking-tighter text-white uppercase">Cyber<span class="text-cyan-400">Verse</span></h1>
                    <p class="text-[10px] text-slate-500 uppercase tracking-widest">The Codebreak Clash</p>
                </div>
            </div>
            <div id="game-timer" class="text-cyan-400 font-bold font-mono text-lg bg-slate-950 px-4 py-1 rounded border border-cyan-900/50">00:00</div>
            <button onclick="router.navigate('admin')" class="text-slate-500 hover:text-cyan-400"><i data-lucide="settings" class="w-5 h-5"></i></button>
        </div>
    </nav>

    <main id="app-root" class="max-w-7xl mx-auto p-4 md:p-8 min-h-[calc(100vh-140px)]"></main>

    <footer class="glass-panel border-t border-cyan-900/20 p-3 fixed bottom-0 left-0 w-full z-40">
        <div class="max-w-7xl mx-auto flex justify-between items-center text-[10px] text-slate-600 uppercase tracking-widest">
            <div class="flex gap-4"><span><span class="w-2 h-2 inline-block bg-emerald-500 rounded-full mr-2"></span>Node_Active</span></div>
            <div id="footer-team-info" class="font-bold text-cyan-500"></div>
        </div>
    </footer>

    <script type="module">
        import { initializeApp } from 'https://www.gstatic.com/firebasejs/11.6.1/firebase-app.js';
        import { getFirestore, doc, setDoc, updateDoc, onSnapshot, collection, deleteDoc, increment } from 'https://www.gstatic.com/firebasejs/11.6.1/firebase-firestore.js';
        import { getAuth, signInAnonymously, onAuthStateChanged, signInWithCustomToken } from 'https://www.gstatic.com/firebasejs/11.6.1/firebase-auth.js';

        const firebaseConfig = typeof __firebase_config !== 'undefined' ? JSON.parse(__firebase_config) : { projectId: "demo" };
        const app = initializeApp(firebaseConfig);
        const auth = getAuth(app);
        const db = getFirestore(app);
        const appId = typeof __app_id !== 'undefined' ? __app_id : 'cyber-verse-dell-01';

        """ + questions_js + """

        const state = { user: null, view: 'landing', teamData: null, allTeams: [], gameState: { status: 'paused', startTime: 0 }, activeQ: null, showHint: false };

        const notify = (msg, type = "info") => {
            const container = document.getElementById('notification-container');
            const toast = document.createElement('div');
            toast.className = `p-4 rounded border flex items-center gap-3 animate-in slide-in-from-right-full pointer-events-auto ${type === 'success' ? 'bg-emerald-950 border-emerald-500 text-emerald-400' : type === 'error' ? 'bg-red-950 border-red-500 text-red-400' : 'bg-cyan-950 border-cyan-500 text-cyan-400'}`;
            toast.innerHTML = `<i data-lucide="${type==='success'?'check-circle':(type==='error'?'alert-circle':'info')}" class="w-5 h-5"></i><span>${msg}</span>`;
            container.appendChild(toast); lucide.createIcons();
            setTimeout(() => toast.remove(), 3000);
        };

        const router = {
            navigate: (v) => { state.view = v; render(); },
            updateGame: async (d) => await setDoc(doc(db, 'artifacts', appId, 'public', 'data', 'settings', 'gameState'), d, {merge:true}),
            resetAll: async () => { if(confirm('Wipe all team progress?')) { for(const t of state.allTeams) await deleteDoc(doc(db,'artifacts',appId,'public','data','teams',t.id)); } },
            purgeTeam: async (tid) => { if(confirm('Purge this team?')) await deleteDoc(doc(db,'artifacts',appId,'public','data','teams',tid)); }
        };
        window.router = router;

        const setupListeners = () => {
            onSnapshot(doc(db, 'artifacts', appId, 'public', 'data', 'settings', 'gameState'), (s) => { 
                if(s.exists()){ state.gameState = s.data(); render(); }
            });
            onSnapshot(collection(db, 'artifacts', appId, 'public', 'data', 'teams'), (s) => {
                state.allTeams = s.docs.map(d => ({ id: d.id, ...d.data() })).sort((a,b) => b.score - a.score);
                render();
            });
            onSnapshot(doc(db, 'artifacts', appId, 'public', 'data', 'teams', state.user.uid), (s) => {
                if(s.exists()){ 
                    state.teamData = s.data(); 
                    const info = document.getElementById('footer-team-info');
                    if (info) info.textContent = `${state.teamData.teamName} // CR: ${state.teamData.score}`;
                    render();
                }
            });
        };

        setInterval(() => {
            if(state.gameState.status === 'running' && state.gameState.startTime) {
                const elapsed = Math.floor((Date.now() - state.gameState.startTime) / 1000);
                const min = String(Math.floor(elapsed/60)).padStart(2,'0');
                const sec = String(elapsed%60).padStart(2,'0');
                const timerEl = document.getElementById('game-timer');
                if (timerEl) timerEl.textContent = `${min}:${sec}`;
            }
        }, 1000);

        window.joinTeam = async (e) => {
            e.preventDefault();
            const fd = new FormData(e.target);
            await setDoc(doc(db, 'artifacts', appId, 'public', 'data', 'teams', state.user.uid), {
                teamName: fd.get('teamName'), p1: fd.get('p1'), p2: fd.get('p2'),
                score: 0, solved: [], attempts: {}, startTime: Date.now()
            });
            window.router.navigate('game');
        };

        window.submitAnswer = async () => {
            if(!state.activeQ || !state.teamData) return;
            const input = document.getElementById('ans-input');
            const val = input.value.trim().toUpperCase().replace(/\s/g,'');
            const q = state.activeQ;
            const currentAtt = state.teamData.attempts[q.id] || 0;

            if(currentAtt >= 3) return notify("Access Denied: Node Locked", "error");

            if(val === q.ans.replace(/\s/g,'')) {
                const points = state.showHint ? 25 : 50;
                await updateDoc(doc(db, 'artifacts', appId, 'public', 'data', 'teams', state.user.uid), {
                    score: increment(points), solved: [...state.teamData.solved, q.id],
                    [`attempts.${q.id}`]: currentAtt + 1
                });
                notify(`Node Cracked: +${points} CR`, "success");
                state.activeQ = null; state.showHint = false; render();
            } else {
                const next = currentAtt + 1;
                await updateDoc(doc(db, 'artifacts', appId, 'public', 'data', 'teams', state.user.uid), { 
                    [`attempts.${q.id}`]: next,
                    score: next >= 3 ? increment(-10) : increment(0)
                });
                if(next >= 3) notify("FATAL: System Penalty Applied", "error");
                else notify(`Unauthorized: ${3-next} retries`, "error");
                input.value = "";
            }
        };

        window.takeHint = () => { if(!state.showHint) { state.showHint = true; notify("Hint Activated: Reward Reduced", "error"); render(); } };
        window.setActive = (id) => { state.activeQ = QUESTIONS.find(q => q.id === id); state.showHint = false; render(); };
        window.updateScore = async (tid, val) => await updateDoc(doc(db, 'artifacts', appId, 'public', 'data', 'teams', tid), {score: parseInt(val)});

        const views = {
            landing: () => `
                <div class="flex flex-col items-center justify-center py-24 text-center animate-in fade-in zoom-in duration-700">
                    <i data-lucide="terminal" class="w-20 h-20 text-cyan-400 mb-8 neon-text animate-pulse"></i>
                    <h2 class="text-6xl font-black mb-6 text-white uppercase italic">Infiltrate<span class="text-cyan-400">The_Grid</span></h2>
                    <p class="text-slate-400 max-w-lg mb-12 text-lg">Decrypt the code shards, navigate the matrix, and secure the leaderboards.</p>
                    <button onclick="router.navigate('lobby')" class="px-12 py-4 bg-cyan-600 hover:bg-cyan-500 text-white font-black rounded border-b-4 border-cyan-800 uppercase tracking-widest transition-all shadow-[0_0_20px_rgba(6,182,212,0.3)]">Establish Connection</button>
                </div>`,
            lobby: () => `
                <div class="max-w-md mx-auto glass-panel p-10 rounded-2xl animate-in fade-in slide-in-from-bottom-4">
                    <h3 class="text-xl font-black mb-8 text-cyan-400 uppercase tracking-widest border-b border-cyan-900/40 pb-4 flex items-center gap-2"><i data-lucide="users"></i> Crew_Entry</h3>
                    <form onsubmit="joinTeam(event)" class="space-y-6">
                        <div><label class="block text-[10px] uppercase font-bold text-slate-500 mb-2">Team_ID</label><input required name="teamName" class="w-full bg-slate-950 border border-slate-800 rounded p-4 text-white focus:border-cyan-500 outline-none" placeholder="NEURO_LINK" /></div>
                        <div class="grid grid-cols-2 gap-4">
                            <div><label class="block text-[10px] uppercase font-bold text-slate-500 mb-2">Op_01</label><input required name="p1" class="w-full bg-slate-950 border border-slate-800 rounded p-4 text-white focus:border-cyan-500 outline-none" placeholder="Alias" /></div>
                            <div><label class="block text-[10px] uppercase font-bold text-slate-500 mb-2">Op_02</label><input required name="p2" class="w-full bg-slate-950 border border-slate-800 rounded p-4 text-white focus:border-cyan-500 outline-none" placeholder="Alias" /></div>
                        </div>
                        <button type="submit" class="w-full py-4 bg-cyan-600 hover:bg-cyan-500 text-white font-black rounded uppercase transition-colors">Authorize Uplink</button>
                    </form>
                </div>`,
            game: () => {
                if(!state.teamData) return views.lobby();
                const running = state.gameState.status === 'running';
                return `
                <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
                    <div class="lg:col-span-3 space-y-6">
                        <div class="glass-panel p-6 rounded-xl space-y-4 border-l-4 border-l-cyan-500">
                            <div class="flex justify-between text-[10px] font-bold text-slate-500 uppercase tracking-widest"><span>Profile</span><span>Active</span></div>
                            <div class="text-xl font-black text-white truncate">${state.teamData.teamName}</div>
                            <div class="grid grid-cols-2 gap-3 text-center">
                                <div class="bg-slate-950 p-3 rounded border border-slate-900"><div class="text-[9px] text-slate-500 uppercase mb-1">Credits</div><div class="text-2xl font-black text-white">${state.teamData.score}</div></div>
                                <div class="bg-slate-950 p-3 rounded border border-slate-900"><div class="text-[9px] text-slate-500 uppercase mb-1">Nodes</div><div class="text-2xl font-black text-cyan-400">${state.teamData.solved.length}</div></div>
                            </div>
                        </div>
                        <div class="glass-panel p-6 rounded-xl">
                            <h4 class="text-[10px] uppercase font-black text-slate-500 mb-4 flex items-center gap-2"><i data-lucide="activity"></i> Ranking_Stream</h4>
                            <div class="space-y-3">
                                ${state.allTeams.slice(0,5).map((t,i) => `
                                    <div class="flex justify-between text-[11px] p-2 rounded ${t.id === state.user.uid ? 'bg-cyan-500/10 text-cyan-400 border border-cyan-500/30' : 'text-slate-400'}">
                                        <span class="truncate max-w-[100px]">${i+1}. ${t.teamName}</span><span class="font-bold">${t.score}</span>
                                    </div>`).join('')}
                            </div>
                        </div>
                    </div>
                    <div class="lg:col-span-9">
                        ${!running ? `<div class="glass-panel rounded-3xl h-[600px] flex flex-col items-center justify-center text-center p-12 border-2 border-dashed border-slate-800"><i data-lucide="lock" class="w-16 h-16 text-slate-700 mb-6"></i><h3 class="text-2xl font-black text-slate-500 uppercase tracking-widest">Grid_Locked</h3><p class="text-slate-600 mt-2 font-bold">Waiting for system administrator to release logic fragments.</p></div>` : `
                            <div class="grid grid-cols-1 xl:grid-cols-2 gap-8">
                                <div class="glass-panel p-4 rounded-3xl aspect-square relative overflow-hidden shadow-2xl">
                                    <div class="grid grid-cols-[23] grid-rows-[25] h-full w-full gap-[1px]">
                                        ${Array.from({length:575}).map((_,idx) => {
                                            const x = idx%23; const y = Math.floor(idx/23);
                                            const q = QUESTIONS.find(q => q.dir === 'across' ? (y===q.y && x>=q.x && x<q.x+q.len) : (x===q.x && y>=q.y && y<q.y+q.len));
                                            const start = QUESTIONS.find(q => q.x===x && q.y===y);
                                            const solved = q && state.teamData.solved.includes(q.id);
                                            const active = q && state.activeQ?.id === q.id;
                                            return `<div class="grid-cell border rounded-sm flex items-center justify-center relative ${q ? (solved?'bg-cyan-500/20 border-cyan-500 text-white shadow-[0_0_5px_cyan]':'bg-slate-800/60 border-slate-700 hover:border-cyan-500 cursor-pointer'):'border-transparent opacity-5'} ${active?'ring-1 ring-cyan-400 bg-slate-700':''}" ${q?`onclick="setActive('${q.id}')"`:''}>
                                                ${start?`<span class="absolute top-0 left-0.5 text-[6px] text-cyan-400 leading-none">${start.display_id}</span>`:''}
                                                ${solved?(q.dir==='across'?q.ans[x-q.x]:q.ans[y-q.y]):''}
                                            </div>`;
                                        }).join('')}
                                    </div>
                                </div>
                                <div class="glass-panel p-8 rounded-3xl flex flex-col animate-in slide-in-from-right-4">
                                    ${state.activeQ ? `
                                        <div class="flex flex-col h-full"><div class="flex justify-between items-start mb-6"><h4 class="text-cyan-400 font-black flex items-center gap-2 uppercase tracking-tighter"><i data-lucide="code"></i> Frag_${state.activeQ.display_id}</h4><span class="text-[10px] font-black text-cyan-500 bg-cyan-500/10 px-2 py-1 rounded">${3-(state.teamData.attempts[state.activeQ.id]||0)} RETRIES</span></div>
                                        <div class="bg-slate-950 p-6 rounded-xl font-mono text-xs border border-slate-800 text-cyan-300 mb-6 flex-grow overflow-auto custom-scrollbar">
                                            <pre class="whitespace-pre-wrap leading-relaxed">${state.showHint ? `// Dev Hint: ${state.activeQ.hint}\\n` : ''}${state.activeQ.code}</pre>
                                        </div>
                                        <div class="space-y-4">
                                            <input id="ans-input" class="w-full bg-slate-950 border border-slate-800 rounded p-4 text-white font-bold tracking-widest focus:border-cyan-500 outline-none uppercase" placeholder="DECRYPT_KEY..." />
                                            <div class="flex gap-3"><button onclick="submitAnswer()" class="flex-1 py-4 bg-cyan-600 hover:bg-cyan-500 text-white font-black rounded uppercase shadow-lg shadow-cyan-950">Crack</button>
                                            <button onclick="takeHint()" class="px-6 bg-slate-800 hover:bg-slate-700 text-slate-400 rounded"><i data-lucide="help-circle"></i></button></div>
                                        </div></div>
                                    ` : `<div class="h-full flex flex-col items-center justify-center opacity-30 italic text-sm uppercase tracking-[.3em]"><i data-lucide="monitor" class="w-12 h-12 mb-4"></i>Awaiting Node Access</div>`}
                                </div>
                            </div>
                        `}
                    </div>
                </div>`;
            },
            admin: () => `
                <div class="space-y-8 animate-in fade-in zoom-in">
                    <div class="glass-panel p-10 rounded-3xl flex justify-between items-center shadow-2xl">
                        <div><h3 class="text-3xl font-black text-white flex items-center gap-4 uppercase tracking-tighter"><i data-lucide="settings" class="text-cyan-500"></i> Overseer_Console</h3><p class="text-slate-500 text-xs mt-1 uppercase tracking-widest font-bold">Control Layer Active</p></div>
                        <div class="flex gap-4">
                            ${state.gameState.status === 'paused' ? `<button onclick="router.updateGame({status:'running', startTime:Date.now()})" class="px-8 py-3 bg-emerald-600 hover:bg-emerald-500 text-white font-black rounded uppercase shadow-lg shadow-emerald-950">Release Grid</button>` : `<button onclick="router.updateGame({status:'paused'})" class="px-8 py-3 bg-yellow-600 hover:bg-yellow-500 text-white font-black rounded uppercase shadow-lg shadow-yellow-950">Halt Grid</button>`}
                            <button onclick="router.resetAll()" class="px-4 py-3 bg-red-600 hover:bg-red-500 text-white font-black rounded uppercase"><i data-lucide="rotate-ccw"></i> Reset All</button>
                        </div>
                    </div>
                    <div class="glass-panel rounded-3xl overflow-hidden shadow-2xl">
                        <table class="w-full text-left"><thead class="bg-slate-950 text-slate-500 text-[10px] uppercase font-black tracking-widest border-b border-slate-800"><tr><th class="p-6">Operatives</th><th class="p-6">Progress</th><th class="p-6">Credits</th><th class="p-6">Actions</th></tr></thead>
                        <tbody class="divide-y divide-slate-900">
                            ${state.allTeams.map(t => `<tr><td class="p-6"><div class="text-white font-black">${t.teamName}</div><div class="text-[10px] text-slate-600 mt-1 uppercase">${t.p1} & ${t.p2}</div></td>
                                <td class="p-6"><div class="flex gap-1 flex-wrap max-w-[120px]">${QUESTIONS.map(q => `<div class="w-2 h-2 rounded-full ${t.solved.includes(q.id)?'bg-cyan-500 shadow-[0_0_5px_cyan]':'bg-slate-800'}"></div>`).join('')}</div></td>
                                <td class="p-6"><input type="number" value="${t.score}" onblur="updateScore('${t.id}',this.value)" class="w-20 bg-slate-950 border border-slate-800 rounded p-2 text-cyan-400 font-black outline-none focus:border-cyan-500" /></td>
                                <td class="p-6 text-center"><button onclick="router.purgeTeam('${t.id}')" class="text-slate-700 hover:text-red-500"><i data-lucide="trash-2"></i></button></td>
                            </tr>`).join('')}
                        </tbody></table>
                    </div>
                </div>`
        };

        const render = () => {
            const root = document.getElementById('app-root');
            if (root) root.innerHTML = (views[state.view] || views.landing)();
            lucide.createIcons();
            const inp = document.getElementById('ans-input'); if(inp) inp.focus();
        };

        const init = async () => {
            if (typeof __initial_auth_token !== 'undefined' && __initial_auth_token) await signInWithCustomToken(auth, __initial_auth_token);
            else {
                try {
                    await signInAnonymously(auth);
                } catch(e) {
                    console.log("Firebase not configured for demo. Running locally!");
                }
            }
            onAuthStateChanged(auth, (u) => { state.user = u; if(u) setupListeners(); });
        };

        document.addEventListener("visibilitychange", async () => {
            if(document.hidden && state.view === 'game' && state.teamData) {
                notify("PROTOCOL BREACH: Tab switch detected. Score Penalized.", "error");
                await updateDoc(doc(db, 'artifacts', appId, 'public', 'data', 'teams', state.user.uid), { score: increment(-10) });
            }
        });

        window.onload = init;
    </script>
</body>
</html>
"""

with open("c:/Users/sarjare/.gemini/antigravity/scratch/cyber_mission_game/index.html", "w") as f:
    f.write(html)
