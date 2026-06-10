import heapq
import matplotlib.pyplot as plt
import numpy as np

# Heuristic Function (Manhattan Distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Search Algorithm
def a_star(maze, start, goal):
    rows = len(maze)
    cols = len(maze[0])

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    visited = []

    while open_set:
        current = heapq.heappop(open_set)[1]
        visited.append(current)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            return path[::-1], visited

        x, y = current

        neighbors = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1)
        ]

        for nx, ny in neighbors:
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:

                tentative_g = g_score[current] + 1

                if (nx, ny) not in g_score or tentative_g < g_score[(nx, ny)]:
                    came_from[(nx, ny)] = current
                    g_score[(nx, ny)] = tentative_g
                    f_score[(nx, ny)] = tentative_g + heuristic((nx, ny), goal)

                    heapq.heappush(
                        open_set,
                        (f_score[(nx, ny)], (nx, ny))
                    )

    return None, visited


# Console Visualization
def print_maze(maze, path, visited, start, goal):
    rows = len(maze)
    cols = len(maze[0])

    print("\nMaze Visualization:\n")

    for i in range(rows):
        for j in range(cols):

            if (i, j) == start:
                print("S", end=" ")

            elif (i, j) == goal:
                print("G", end=" ")

            elif path and (i, j) in path:
                print("*", end=" ")

            elif (i, j) in visited:
                print("o", end=" ")

            elif maze[i][j] == 1:
                print("#", end=" ")

            else:
                print(".", end=" ")

        print()


# Plot Visualization
def plot_maze(maze, path, start, goal):
    grid = np.array(maze)

    plt.figure(figsize=(6, 6))
    plt.imshow(grid, cmap="gray_r")

    if path:
        x = [p[1] for p in path]
        y = [p[0] for p in path]
        plt.plot(x, y, marker='o', linewidth=2, label="Path")

    plt.scatter(start[1], start[0], marker='s', s=150, label="Start")
    plt.scatter(goal[1], goal[0], marker='*', s=200, label="Goal")

    plt.title("Maze Solver using A* Search")
    plt.legend()
    plt.grid(True)
    plt.show()


# ---------------- MAIN PROGRAM ----------------

maze = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path, visited = a_star(maze, start, goal)

if path:
    print("Shortest Path Found!\n")
    print("Path:")
    print(path)

    print_maze(maze, path, visited, start, goal)

    plot_maze(maze, path, start, goal)

else:
    print("Goal is unreachable!")