import random

# Maze size
rows, cols = 10, 10  

# Each cell has walls: top, right, bottom, left
maze = [[{'visited': False, 'walls': [True, True, True, True]} for _ in range(cols)] for _ in range(rows)]

# Directions: (dy, dx) → up, right, down, left
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
opposite = [2, 3, 0, 1]  # Opposite wall index

def dfs(r, c):
    maze[r][c]['visited'] = True
    dirs = list(range(4))
    random.shuffle(dirs)  # Randomize path

    for d in dirs:
        nr, nc = r + directions[d][0], c + directions[d][1]

        # Check bounds and if not visited
        if 0 <= nr < rows and 0 <= nc < cols and not maze[nr][nc]['visited']:
            # Knock down wall between current and next cell
            maze[r][c]['walls'][d] = False
            maze[nr][nc]['walls'][opposite[d]] = False
            dfs(nr, nc)  # Recursive DFS

# Generate maze
dfs(0, 0)

# Print simple maze
for r in range(rows):
    # Top walls
    print("".join("+" + ("---" if maze[r][c]['walls'][0] else "   ") for c in range(cols)) + "+")
    # Side walls
    print("".join(("|" if maze[r][c]['walls'][3] else " ") + "   " for c in range(cols)) + "|")
# Bottom line
print("+" + "---+" * cols)
