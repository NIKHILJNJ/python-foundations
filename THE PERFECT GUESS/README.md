# Guess the Number

A simple Python command-line game where you try to guess a randomly generated number between 0 and 1000. After each guess, the game tells you how close you were.

## How It Works

1. The game picks a random target number between 0 and 1000.
2. You enter your guess.
3. Based on how far your guess is from the target, the game gives you feedback:

| Distance from target | Feedback              |
|-----------------------|------------------------|
| Exact match            | 🎯 You guessed it!    |
| > 250                  | Far from the target   |
| > 150                  | Somewhat close        |
| > 75                   | Very close            |
| > 25                   | Extremely close       |
| ≤ 25                   | Nailed it             |

4. After each round, you can choose to play again or quit.

## Requirements

- Python 3.x (no external libraries needed — uses only the built-in `random` module)

## Usage

Clone the repo and run the script:

```bash
python guess_game.py
```

You'll be prompted to enter a guess between 0 and 1000:

```
Enter your guess between 0 and 1000: 500
somewhat close from the target number The number was 612
Play again? (y/n): y
```

Enter `n` when prompted to stop playing.

## Code Structure

- `GuessGame` — a class that takes a user's guess, generates a random target, and prints feedback based on the distance between the two.
- A `while` loop drives the game, allowing repeated rounds until the user chooses to quit.

## Notes

- Each round generates a **new** random target number.
- Guesses are accepted as floats, so decimal input (e.g. `450.5`) is allowed.
- There is currently no input validation — entering a non-numeric value or a number outside 0–1000 will not be caught.

## Possible Improvements

- [ ] Add input validation (reject non-numeric input or values outside 0–1000)
- [ ] Track and display number of attempts per round
- [ ] Add a difficulty setting that adjusts the number range
- [ ] Keep the same target number across guesses within a round instead of generating a new one each guess

## License

Feel free to use, modify, and share this project.
