def print_maze(maze):
    for row in maze:
        print("".join(row))
    print("-" * 20)

def dfs(maze, x, y):
    if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]):
        return False
    if maze[x][y] == '*' or maze[x][y] in ['+', '.']:
        return False
    if maze[x][y] == ' ':
        maze[x][y] = '.'

    print(f"x={x}, y={y}")
    print_maze(maze)

    if x == len(maze) - 1 or y == len(maze[0]) - 1:
        return True
    if dfs(maze, x, y + 1):
        return True
    if dfs(maze, x + 1, y):
        return True
    if dfs(maze, x, y - 1):
        return True
    if dfs(maze, x - 1, y):
        return True

    maze[x][y] = '+'
    return False

if __name__ == "__main__":
    maze = [
        list("********"),
        list("** * ***"),
        list("     ***"),
        list("* ******"),
        list("*     **"),
        list("***** **")
    ]

    dfs(maze, 2, 0)
    print("Final Maze:")
    print_maze(maze)
