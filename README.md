# A* pathfinding algorithm with visualization

## Getting started

The following repository consists of 3 files: <br>
- algorithm.py - file with algorithm and Node class that represents nodes in algorithm. <br>
- visualization.py - file responsible for creating a window and drawing output onto this window. It also provides main function that runs whole program. <br>
- constant.py - file with constants.

## Prerequisites

You will need following technologies: <br>
- python 3.10
- pygame

## Installation

It's important to download src directory as a whole. Downloading files one by one may make program unusable, because of this import statement:

```python
from src.algorithm import *
```
If you decide to download them one by one, or you need only one file then make sure to correct imports.

## Controls
After successful installation you will probably want to run the program. You can do it by running main function in visualization.py file. Here are controls which may be helpful when trying to interact with the program: <br>
- mouse left button - drawing obstacles, choosing start point or end point.
- mouse right button - removing obstacles, start point or end point. Can be used to clean the grid, but "c" button will get this job done better.
- spacebar - running algorithm if start and end points exist.
- c button - clearing the whole grid.

For information about what a specific color means checkout constant.py file.