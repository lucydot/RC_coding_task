# RC coding task - TicTacToe

Coding task for the RC pair programming interview. I have selected the TicTacToe game as it seems comfortably in my wheelhouse and time is of the essence..

*Before your interview, write a program that lets two humans play a game of Tic Tac Toe. The interface can be terminal-based or a full GUI. Players should be able to take turns making moves, and the program should report the outcome of the game. During your interview, you'll pair on extending the game in a way of your choosing. For example, you might add support for a computer player to your game, starting with random moves and then making the AI smarter if you have time.*


## Notes

- I've not used any agential AI or AI auto-complete
- I used Claude lightly, in a similar way to a search engine
- I also used StackOverflow
- I've spent about half a day on this; my commits to this repo indicate how the code evolved
- I've left a few in-line comments regarding design decisions
- I started generalising to other grid sizes, this is done on this branch

## Potential new functionality / improvements

I'm listing ideas here as they occur to me:

- Implement a computer player
- Support for two people playing remotely through Github or similar
- Create a fun sonified (sound based) version!
- Find a cleverer way of determining win state using knowledge of the latest move
- Work out when a game is drawn ahead of the board being full
- Generalise the grid so that it can be another shape: a rectangle? a star?!
- Generalise the grid to higher dimensions
