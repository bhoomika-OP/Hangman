# Problem Statement

Learning Python often feels boring when it's just syntax and print statements. Most beginners forget concepts quickly because there is nothing to actually use them for. A simple game, on the other hand, gives a reason to use loops, conditionals, functions, and string handling all in one place, and it's something you can actually show people afterward.

This project is a command-line Hangman game. The word is fixed in the code, and the player has to guess it letter by letter within a limited number of attempts. It is small enough to build in a short time but still touches on real programming logic like tracking game state, validating user input, and handling win/lose conditions.

## Scope of the Project

- A single-player, text-based Hangman game that runs in the terminal.
- The secret word is set inside the code (already chosen the by programmer).
- Covers one full game loop: guessing, checking win/loss, and replaying, as per player's wish.
- Does not include a GUI, scoring system, difficulty levels, or a word bank as the focus is on getting the core game logic right.

## Target Users

- Beginners learning Python who want a small project to practice functions, loops, and conditionals.
- Anyone who wants a quick, no-setup terminal game to kill time.
- Students needing a simple project to demonstrate basic programming concepts (functions, string operations, control flow) for coursework or a presentation.

## High-Level Features

- Displays the secret word as underscores and reveals correct letters in their position.
- Accepts one letter at a time from the player and checks it against the word.
- Rejects invalid input (more than one character, non-letters, or a letter already guessed).
- Tracks remaining attempts and ends the game after 6 wrong guesses.
- Shows a win message with ASCII art when the player guesses the full word.
- Reveals the word and shows a "Game Over" message if the player runs out of attempts.
- Lets the player restart the game or exit after each round.
