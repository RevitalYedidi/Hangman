# Hangman
Python Hangman game


The player is asked to enter: 1- Path to file with words, 2- Position (index) for word in file. Depending on the input from the player, the secret word for the game will be selected.
The "hangman" mode will be displayed to the player according to the number of his failed attempts.
Under "hangman", the secret word will be displayed in outline for each letter in the word.

In each round the player will type one character.
If the character is invalid (two or more characters and / or is not an English letter, or guessed it in the past), an "X" will be printed on the screen, the list of previously guessed letters will be printed and the player will have to enter another character until he types correctly.

After each correct guess, the secret word will be displayed in underlined for each letter in the word.
In case of a failed guess - will be printed to the player ":(" and below it the current state of the "hangman".
End of the game:
  If the player guesses the whole word correctly - it will appear: WIN.
  If the player guesses six failed attempts - will appear: LOSE.
