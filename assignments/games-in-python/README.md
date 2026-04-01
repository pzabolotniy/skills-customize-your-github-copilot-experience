

# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic Hangman word-guessing game in Python. Practice string manipulation, loops, conditionals, and random selection while creating an interactive game.

## 📝 Tasks

### 🛠️ Game Setup

#### Description
Set up the basic structure for your Hangman game. Define a list of possible words and randomly select one for the player to guess.

#### Requirements
Completed program should:

- Define a list of at least 5 possible words
- Randomly select one word as the secret word
- Initialize variables to track guessed letters and remaining attempts


### 🛠️ Gameplay Loop

#### Description
Implement the main game loop where the player guesses letters, and the game updates and displays progress.

#### Requirements
Completed program should:

- Display the current progress (e.g., _ _ t h o n)
- Accept user input for letter guesses
- Track and display incorrect guesses remaining
- Update the game state after each guess


### 🛠️ Game End & Messages

#### Description
Handle the end of the game, displaying appropriate messages for a win or loss.

#### Requirements
Completed program should:

- End the game when the word is fully guessed or attempts run out
- Display a congratulatory message if the player wins
- Display the correct word and a message if the player loses

---
**Example Output:**
```
Word: _ _ _ _ _ _
Guesses left: 6
Guess a letter: a
Word: _ a _ _ _ a _
Guesses left: 6
...
Congratulations! You guessed the word: hangman
```

