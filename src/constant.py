import pygame

# Dimensions:
WIDTH = 800                     # Width of a window
HEIGHT = 800                    # Height of a window
ROWS = 50                       # Number of rows
COLUMNS = 50                    # Number of columns

# Colours:
RED = (255, 0, 0)               # Has already been visited
GREEN = (0, 255, 0)             # Is in a priority queue, so it is pending to be visited
WHITE = (255, 255, 255)         # Haven't been visited yet
BLACK = (0, 0, 0)               # Defines an obstacle for algorithm
PURPLE = (128, 0, 128)          # Shortest path
ORANGE = (255, 165, 0)          # Start node
GREY = (128, 128, 128)          # Lines of the grid
TURQUOISE = (64, 224, 208)      # End node

# Window:
WIN = pygame.display.set_mode((WIDTH, HEIGHT))      # Window with set width and height
