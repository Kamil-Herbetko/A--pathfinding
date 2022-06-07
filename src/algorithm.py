from typing import TypeAlias, Callable
from constant import *
from queue import PriorityQueue
node_type_alias: TypeAlias = 'Node'


class Node:
    """A class that represents graph nodes from the algorithm. It is used to track current color of a square in the
    visualization grid. I used slots for memory savings since we don't require declaring new attributes at run time
    or after class definition and we will be creating multiple instances of that class."""

    __slots__ = ("x", "y", "row", "col", "width", "height", "total_rows", "total_cols", "color", "neighbours", "border")

    def __init__(self, row: int, col: int, width: int, height: int, total_rows: int, total_cols: int):
        self.x = row * width
        self.y = col * height
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.total_rows = total_rows
        self.total_cols = total_cols
        self.border = row == 0 or col == 0 or row == total_rows - 1 or col == total_cols - 1
        self.color = BLACK if self.border else WHITE
        self.neighbours: list[node_type_alias] = []

    def get_pos(self) -> (int, int):
        """Returns position of an instance in a grid."""
        return self.row, self.col

    def get_state(self) -> tuple[int, int, int]:
        """Returns current state of a node, which is determined by its colour."""
        return self.color

    def set_state(self, color: tuple[int, int, int]) -> bool:
        """Sets current state of a node, which is determined by its colour if it isn't in the border."""
        if (0 < self.row < self.total_rows - 1) and (0 < self.col < self.total_cols - 1):
            self.color = color
            return True

        return False

    def update_neighbours(self, grid: list[list[node_type_alias]]) -> None:
        """Checks neighbours of a node and if they are not barriers it adds them to the neighbours list."""
        self.neighbours = []
        down = grid[self.row + 1][self.col]
        up = grid[self.row - 1][self.col]
        left = grid[self.row][self.col - 1]
        right = grid[self.row][self.col + 1]

        if down.color is not BLACK:
            self.neighbours.append(down)

        if up.color is not BLACK:
            self.neighbours.append(up)

        if left.color is not BLACK:
            self.neighbours.append(left)

        if right.color is not BLACK:
            self.neighbours.append(right)


def heuristic_function(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    """Function that calculates distance between 2 points using manhattan distance formula."""
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(path_history_dict: dict[Node: Node], current: Node, draw: Callable):
    while current in path_history_dict:
        current = path_history_dict[current]
        current.set_state(PURPLE)
        draw()


def algorithm(draw: Callable, grid: list[list[Node]], start: Node, end: Node) -> bool:
    """Function that runs the whole algorithm on a given grid, start node and end node."""
    count = 0
    priority_queue = PriorityQueue()
    priority_queue.put((0, count, start))
    came_from: dict[Node: Node] = {}

    g_score = {node: float("inf") for row in grid for node in row}
    f_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    f_score[start] = heuristic_function(start.get_pos(), end.get_pos())

    open_set = {start}

    while not priority_queue.empty():
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                pygame.quit()

        current: Node = priority_queue.get()[2]   # Extracting node from the first element in the queue
        open_set.remove(current)

        if current is end:
            reconstruct_path(came_from, end, draw)
            end.set_state(TURQUOISE)
            start.set_state(ORANGE)
            return True

        for neighbour in current.neighbours:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbour]:   # Checking if we found a better path to this node
                came_from[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + heuristic_function(neighbour.get_pos(), end.get_pos())

                if neighbour not in open_set:
                    count += 1
                    priority_queue.put((f_score[neighbour], count, neighbour))
                    open_set.add(neighbour)
                    neighbour.set_state(GREEN)
        draw()

        if current is not start:
            current.set_state(RED)

    return False
