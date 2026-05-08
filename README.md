# Cyber Verse: Cybersecurity Crossword

Welcome to **Cyber Verse**, a real-time, competitive cybersecurity crossword challenge designed for training and tournament play.

## 🚀 Game Overview
Cyber Verse is a high-stakes "decryption" simulation where teams compete to solve a complex grid of cybersecurity terms. The platform features real-time scoring, live leaderboards, and a cyberpunk-inspired interface.

## 📜 Rules for Participants

### 1. The Mission
Your team's objective is to successfully decrypt the entire grid by identifying all cybersecurity terms based on the provided clues.

### 2. Scoring System
- **Successful Decryption**: Each correctly identified word awards **100 points**.
- **Failed Attempts**: Every incorrect submission incurs a penalty (default: **-2 points**). Accuracy matters!
- **Completion**: The mission is complete only when all cells in the grid are correctly filled.

### 3. The Hint System
- If you are stuck on a particularly difficult node, a **Hint** button will appear after a certain number of failed attempts (default: 10).
- **Hint Penalty**: Activating a hint deducts **60 points** from your score.
- **Python Decryption**: Hints are provided as Python code snippets. You must logically parse the code to extract the correct answer.

### 4. Integrity & Anti-Cheat
- **Tab Tracking**: The system monitors focus. Frequently switching tabs or leaving the game window may be flagged by the Overseer.
- **Real-Time Sync**: Your progress is synchronized instantly with the Overseer's console.

### 5. Winning the Challenge
The winner is determined by:
1. **Total Score**: High accuracy and minimal hint usage.
2. **Time Taken**: In the event of a score tie, the team that completed the mission faster wins.

## 🛠 Tech Stack
- **Frontend**: HTML5, Vanilla JavaScript, CSS (Tailwind).
- **Backend**: Firebase Firestore (Real-time synchronization).
- **Icons**: Lucide-react.

## 👨‍💻 Administrative Controls
Administrators (Overseers) have a dedicated panel to:
- Reset the session for all teams.
- Launch the mission globally.
- Adjust scoring rules and penalties in real-time.
- Monitor live team progress and "Kick" suspicious users.

---
*Good luck, Agents. The network is counting on you.*
