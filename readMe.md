# TicTacToe AI

## Overview

This Python program implements a simple Tic-Tac-Toe game using the Pygame library. The game allows the user to play against an AI opponent with a graphical user interface.

## Dependencies

- Python 3.x
- Pygame

## How to Run

1. Ensure you have Python 3.x installed on your system.
2. Install the Pygame library:

   ```bash
   pip install pygame
   ```

3. Run the program:

   ```bash
   python runner.py
   ```

## Game Features

- **Player Selection:** Choose to play as X or O.
- **Graphical User Interface:** A graphical interface using Pygame for a better user experience.
- **AI Opponent:** Play against a simple AI opponent that makes moves using the minimax algorithm.
- **Game Board:** A 3x3 game board displayed on the screen.
- **Game Over Detection:** Detects when the game is over, either in a win, loss, or tie scenario.
- **Play Again Option:** After a game is over, there's an option to play again.

## How to Play

1. Run the program.
2. Choose to play as X or O.
3. Make your moves by clicking on the desired position on the game board.
4. The AI opponent will make its moves.
5. The game will declare a winner, show a tie, or end with a user-defined outcome.
6. Optionally, play again to start a new game.

## File Structure

- `tictactoe.py`: Contains the Tic-Tac-Toe game logic.
- `OpenSans-Regular.ttf`: Font file for text rendering.
- `runner.py`: The main program file that initializes the game and handles user input.

## Credits

- Pygame Library: [https://www.pygame.org/](https://www.pygame.org/)
- Font: OpenSans-Regular.ttf (Included in the project)

## License

This project is licensed under the [MIT License](LICENSE).
