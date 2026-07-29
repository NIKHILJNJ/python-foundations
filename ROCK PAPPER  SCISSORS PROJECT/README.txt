# Rock Paper Scissors 🪨📄✂️

A simple command-line Rock Paper Scissors game written in Python. Play against
the computer, with unlimited rounds until you choose to stop.

## How it works

- You pick Rock, Paper, or Scissors by entering a number.
- The computer picks randomly using Python's `random` module.
- The winner is decided using standard Rock Paper Scissors rules:
  - Rock beats Scissors
  - Scissors beats Paper
  - Paper beats Rock
- After each round, you're asked whether you want to play again.

## How to run

```bash
python rock_paper_scissors.py
```

## Example session

```
Enter 1 for ROCK, 2 for PAPER, 3 for SCISSORS: 2
You win! Your choice is PAPER and computer's is ROCK
Play again? (y/n): y

Enter 1 for ROCK, 2 for PAPER, 3 for SCISSORS: 1
It's a draw! Your choice is ROCK and computer's is ROCK
Play again? (y/n): n

Thanks for playing!
```

## Concepts used

- `random.choice()` for the computer's move
- `if` / `elif` / `else` conditional logic for all 9 possible outcomes
- Dictionaries for mapping numbers to move names
- Input validation (rejects anything outside 1, 2, 3)
- A `while` loop for replayability

## Possible improvements

- [ ] Track and display a running score across rounds
- [ ] Add a "best of N rounds" mode
- [ ] Refactor the win/lose messages into a single reusable function
