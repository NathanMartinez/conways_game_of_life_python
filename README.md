# Conway's Game of Life

This is my Python implementation of Conway's Game of Life.

## Game Rules

The game takes place on a two-dimensional grid of cells, where each cell can be in one of two states: alive or dead. The game evolves in discrete time steps.

The state of a cell at each time step depends on the following rules:

1. Any live cell with fewer than two live neighbors dies, as if caused by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

These rules are applied simultaneously to all cells in the grid at each time step, creating a new generation of cells.

## Grid Visualization

The game grid is typically displayed graphically, with live cells represented by filled squares and dead cells represented by empty squares. The grid evolves over time as new generations are created based on the rules.

## Examples and Patterns

Conway's Game of Life exhibits a wide range of interesting patterns and behaviors. Some patterns, known as oscillators, repeat their configurations after a certain number of generations. Others, such as gliders, move across the grid indefinitely.

## More Information

For more information about Conway's Game of Life, you can visit the following links:

- [Wikipedia - Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
- [Stanford Encyclopedia of Philosophy - Conway's Game of Life](https://plato.stanford.edu/entries/cellular-automata/supplement2.html)

---

This markdown file provides a brief overview of Conway's Game of Life. Feel free to explore and experiment with different patterns and configurations in the game implementation.

This content was generated with the help of [ChatGPT](https://github.com/openai/chatgpt) by OpenAI.

## Key Features

- Interactive interface with customizable settings
- Random and predefined pattern generation
- Adjustable frames per second (FPS)
- Pause/play functionality
- Colorful visualization of cell states

## Installation

To run this implementation of Conway's Game of Life, follow these steps:

1. Clone the repository:

```shell
git clone https://github.com/NathanMartinez/conways_game_of_life_python
```

2. Install the dependencies. This implementation requires pygame and numpy. You can install them using pip:

- Windows:

```shell
pip install pygame numpy
```
- Mac and Linux:

```shell
pip3 install pygame numpy
```

3. Run the game:

- Windows:

```shell
python main.py
```
- Mac and Linux:

```shell
python3 main.py
```

## Controls

- Enable left-click functionality to toggle cells between the dead and alive states using the mouse.
- Use the left and right arrow keys to decrease or increase the frames per second (FPS) respectively.
- Press the spacebar to pause or resume the game.
- Press 'R' to generate a random board.
- Press 'C' to generate a checkerboard pattern.
- Press 'E' to generate an empty board.
