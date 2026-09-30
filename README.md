# Hangman Game (Python)

## Overview

A command-line Hangman game written in Python. The game picks a secret word, and the player has to guess it one letter at a time. Each wrong guess costs one attempt, and the player has 6 attempts in total. Guess the whole word before the attempts run out to win and see a celebratory ASCII art. After each round, the player can choose to play again.

## Features

- Terminal-based, single-player gameplay
- Secret word displayed as blanks (`_ _ _ _ _`) and revealed letter by letter
- 6 attempts per game; only wrong guesses reduce attempts
- Input validation:
  - Only a single alphabetic character is accepted
  - Already guessed letters are rejected without costing an attempt
  - Input is case-insensitive
- ASCII art shown on winning
- Win/lose messages, with the secret word revealed when the player loses
- "Play again?" option after every game

## Technologies / Tools Used

- **Language:** Python 3.6+
- **Standard library:** `random` (imported in the code)
- **Tools:** Any terminal / command prompt; any text editor or IDE (VS Code, PyCharm, IDLE, etc.)

No third-party packages are required.

## Installation & Running the Project

1. **Install Python 3.6 or higher** from [python.org](https://www.python.org/downloads/). Verify the installation:
   ```bash
   python --version
   ```
2. **Get the code:** clone the repository or download the file.
   ```bash
   git clone <your-repository-url>
   cd <repository-folder>
   ```
3. **Run the game:**
   ```bash
   python hangman.py
   ```
   (Use `python3 hangman.py` on macOS/Linux if `python` points to Python 2.)
4. **Play:** type one letter at a time and press Enter. When the game ends, type `yes` to play again or `no` to quit.

> Replace `hangman.py` with the actual name of your script file.

## How to Play

- A secret word is already set in the game.
- Guess one letter at a time.
- Correct letters are revealed in their positions.
- Wrong letters cost one attempt (6 attempts total).
- Guess the full word before attempts run out to win.

## Instructions for Testing

The project is tested manually by running the game and checking each scenario below. The secret word is 'hakla'.

| # | Scenario | Input | Expected Result |
|---|----------|-------|-----------------|
| 1 | Correct guess | 'h' | Prints 'Correct!' and reveals 'h _ _ _ _'|
| 2 | Wrong guess | 'z' | Prints 'Wrong! Attempts left: 5' |
| 3 | Repeated letter | 'h', then 'h' again | Prints 'You already guessed that letter.'; attempts unchanged |
| 4 | Multiple characters | 'ab' | Prints 'Please enter a single letter.'; attempts unchanged |
| 5 | Non-letter input | '5' or '@' | Prints 'Please enter a single letter.' |
| 6 | Uppercase input | 'H' | Treated the same as 'h' |
| 7 | Win the game | h', 'a', 'k', 'l' | Word fully revealed, win message and ASCII art shown, prompts to play again |
| 8 | Lose the game | 6 wrong letters (e.g. 'b', 'c', 'd', 'e', 'f', 'g') | Prints 'GAME OVER!!!', prompts to play again |
| 9 | Play again (yes) | 'yes' | A new game starts |
| 10 | Play again (no) | 'no' | Prints 'Thanks for playing! Goodbye.' and exits (the secret word is also shown after a loss) |

**Tip:** To test different words easily, change the value of 'word' inside the 'hangman()' function.

## Project Structure

'''
.
├── hangman.py    # Game source code
└── README.md     # Project documentation
'''
