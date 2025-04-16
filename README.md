This project implements elements of the traditional Ayoyal Board game
The game is implemented in python
The board is represented as a single list of 14 elements:
Indices 0-5: Player 1's pits.
Index 6: Player 1's store.
Indices 7-12: Player 2's pits.
Index 13: Player 2's store.

A `Player` class is used to store player-specific information, such as name and player number.

The `Ayoayo` class contains all the game logic, including:
Distributing seeds in a circular manner.
Granting extra turns when the last seed lands in the player's store.
Capturing seeds from the opponent's pits when the last seed lands in the player's own empty pit.
Checking for game-ending conditions and determining the winner.

the game is played interactively on the terminal

Ensure you have python installed on your machine to be able to run the file
I have make the file excecutable so running it should be easier
