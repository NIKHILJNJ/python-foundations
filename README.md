# 🐍 Python Foundations

Core Python programming labs and algorithmic logic patterns, built during CodeWithHarry's 12-hour Python course. Includes 5+ custom functional programs per chapter, plus two hands-on projects, developed natively on Ubuntu Linux.

## What's Covered

| Chapter | Topic |
|---|---|
| 1 | Modules, Comments & Pip |
| 2 | Variables and Datatypes |
| 3 | Strings |
| 4 | List and Tuples |
| 5 | Dictionary & Sets |
| 6 | Conditional Expressions |
| 7 | Loops in Python |
| 8 | Functions & Recursions |
| 9 | File I/O |
| 10 | Object Oriented Programming |
| 11 | Inheritance & More on OOPs |
| 12 | Advanced Python 1 |
| 13 | Advanced Python 2 |

## Projects

### 🪨📄✂️ Rock Paper Scissors
`ROCK PAPPER SCISSORS PROJECT/game.py`

A command-line Rock Paper Scissors game against the computer, with unlimited replayable rounds. Started from the handbook's Snake-Water-Gun exercise, but reworked around the classic rock/paper/scissors theme instead — with numeric input (1/2/3), a dictionary mapping numbers to move names, and explicit win/lose/draw messages handling all 9 possible outcomes.

**Concepts used:** `random.choice()`, `if`/`elif`/`else` branching across all outcome combinations, dictionaries for number-to-move mapping, input validation, a `while` loop for replayability.

**Possible improvements:** track a running score across rounds, add a "best of N" mode, refactor the win/lose messages into a single reusable function.

### 🎯 The Perfect Guess
`THE PERFECT GUESS/GUESS_GAME.py`

A number-guessing game reworked as a proper `GuessGame` class rather than a plain script — the constructor takes the user's guess, generates a random target between 0 and 1000, and reports back how close the guess was across five tiers (far / somewhat close / very close / extremely close / nailed it), based on absolute distance from the target. Also includes replayability via a `while` loop.

The file keeps my first attempt at the closeness logic (commented out at the bottom) — an earlier percentage-based approach that worked fine conceptually but didn't fit a problem where the target is a fixed value rather than a ratio. Left it in as a record of the iteration.

> The two more advanced, API-integrated projects from the handbook — **Jarvis (voice-activated assistant)** and the **Auto-Reply AI Chatbot** — live in a separate repository, since they lean more on external APIs and automation than core language fundamentals.

## Author

**Nikhil Jain**
Learning in public, with a regular commit habit.
