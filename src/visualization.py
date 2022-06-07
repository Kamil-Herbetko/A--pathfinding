from algorithm import *


def make_grid(rows: int, cols: int, width: int, height: int) -> list[list[Node]]:
    """This function makes a grid (2D list) of nodes that algorithm will be operating on."""
    width_of_node = width // cols
    height_of_node = height // rows

    return [
        [
            Node(j, i, width_of_node, height_of_node, rows, cols) for i in range(0, cols)
        ] for j in range(0, rows)
    ]


def draw_grid(win: pygame.Surface, rows: int, cols: int, width: int, height: int) -> None:
    """This function draws a grid of lines that will serve as separators for nodes."""
    width_of_node = width // cols
    height_of_node = height // rows

    for i in range(rows):
        dist = i * height_of_node
        pygame.draw.line(win, GREY, (0, dist), (width, dist))

    for j in range(cols):
        dist = j * width_of_node
        pygame.draw.line(win, GREY, (dist, 0), (dist, height))


def draw(win: pygame.Surface, grid: list[list[Node]], rows: int, cols: int, width: int, height: int) -> None:
    """This function is responsible for drawing everything on the screen."""
    win.fill(WHITE)

    for row in grid:
        for node in row:
            pygame.draw.rect(win, node.color, (node.x, node.y, node.width, node.height))

    draw_grid(win, rows, cols, width, height)
    pygame.display.update()


def get_clicked_pos(pos: tuple[int, int], rows: int, cols: int, width: int, height: int) -> tuple[int, int]:
    """This function takes mouse position and returns coordinates of a node above which mouse is hovering."""
    width_of_node = width // cols
    height_of_node = height // rows
    x, y = pos

    return x // width_of_node, y // height_of_node


def main() -> None:
    """Main function for running everything."""
    pygame.display.set_caption("A* pathfinding with visualization.")
    grid: list[list[Node]] = make_grid(ROWS, COLUMNS, WIDTH, HEIGHT)
    start = None
    end = None

    run = True
    started = False  # This variable represents whether algorithm started running or not.
    while run:
        draw(WIN, grid, ROWS, COLUMNS, WIDTH, HEIGHT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key is pygame.K_SPACE and not started and start and end:
                    for row in grid:
                        for node in row:
                            if not node.border:
                                node.update_neighbours(grid)

                    # Running algorithm and finding shortest path.
                    started = True
                    algorithm(lambda: draw(WIN, grid, ROWS, COLUMNS, WIDTH, HEIGHT), grid, start, end)

                if event.key is pygame.K_c:
                    start = None
                    end = None
                    started = False
                    grid = make_grid(ROWS, COLUMNS, WIDTH, HEIGHT)

        if not started:
            if pygame.mouse.get_pressed()[0]:
                row, col = get_clicked_pos(pygame.mouse.get_pos(), ROWS, COLUMNS, WIDTH, HEIGHT)
                node = grid[row][col]

                # Using lazy evaluation in if statement in order to make one less if.
                if not start and node is not end and node.set_state(ORANGE):
                    start = node

                elif not end and node is not start and node.set_state(TURQUOISE):     # Same as above.
                    end = node

                elif node is not start and node is not end:
                    node.set_state(BLACK)

            elif pygame.mouse.get_pressed()[2]:
                row, col = get_clicked_pos(pygame.mouse.get_pos(), ROWS, COLUMNS, WIDTH, HEIGHT)
                node = grid[row][col]
                node.set_state(WHITE)

                if node is start:
                    start = None

                if node is end:
                    end = None

    pygame.quit()


if __name__ == '__main__':
    main()
