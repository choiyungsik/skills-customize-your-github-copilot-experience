# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic Hangman game in Python using strings, loops, conditionals, and user input. Students will practice selecting words, tracking player guesses, and ending the game correctly based on the result.

## 📝 Tasks

### 🛠️ Word Selection and Guessing

#### Description
Create a game that chooses a secret word and lets the player guess letters one at a time.

#### Requirements
Completed program should:

- Store a list of words and randomly choose one for each round
- Display the hidden word as underscores, such as `_ _ _ _`
- Accept a letter guess from the player
- Reveal matching letters in the correct positions
- Prevent duplicate guesses and show feedback for repeated input

### 🛠️ Game Flow and Win/Loss Rules

#### Description
Add the full game logic to track progress, remaining attempts, and whether the player has won or lost.

#### Requirements
Completed program should:

- Track the number of incorrect guesses remaining
- Update the display after each guess
- End the game when the word is fully guessed or the player runs out of attempts
- Display a clear win or loss message at the end
- Include a simple replay option or restart flow if desired
