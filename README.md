BINGO DUEL v10 — Talking CPU Edition
 A fun, terminal-based BINGO game where you face off against a cheeky AI opponent!

Built entirely with Python standard functions only —
no imports, no external libraries, under 100 lines of code.

🕹️ Gameplay Overview

Play a fast-paced game of BINGO against the computer!
Each player (you and the CPU) gets a 5×5 grid of random numbers (1–25).
Turns alternate:

The CPU calls a number first.

If that number appears on your board, it’s marked with a 🔵.

Then you call a number — if the CPU has it, it’s marked too.

Every time a row, column, or diagonal is completely marked, you earn a letter in BINGO.

The first to complete all five lines (B-I-N-G-O) wins! 🏆

🤖 Talking CPU

The AI opponent isn’t just smart — it’s got attitude!
It reacts to your moves, celebrates its wins, and panics when you’re about to win:

💻 CPU calls: 12
🔥 You completed a line!
CPU: 😠 "You’re too good!"

✨ Features

✅ Fully playable single-player mode

✅ Smart AI that targets its best scoring moves

✅ Emoji-based visuals for easy readability

✅ Talking CPU reactions for personality

✅ Clean 5×5 board display with progress tracker (BINGO: BI---)

✅ Graceful error handling (invalid inputs won’t crash the game)

✅ 100% no-import code, <100 lines total

💻 How to Play

Run the script in your terminal:

python bingo_duel.py


Enter a seed word to generate your unique board (or press Enter for default).

Watch the CPU call numbers — then enter your own between 1–25.

Keep track of your progress via the BINGO bar on top.

First to complete 5 lines wins! 🎉

🧠 Tech & Constraints
Constraint	Status
No external imports	✅
Under 100 lines	✅
Error handling	✅
Readable structure	✅
Terminal UI only	✅

📁 File Structure
bingo_duel_v10/
├── bingo_duel.py       # Main game script
└── README.md           # Project description

🧑‍💻 Author
Kicha
Created as part of the Code Olympics Challenge 🥇
Constraint: No Imports | 100 Lines | Fully Playable Game
