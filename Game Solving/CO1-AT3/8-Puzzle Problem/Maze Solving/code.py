from collections import deque

maze = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)

rows = len(maze)
cols = len(maze[0])

queue = deque([(start, [start])])
visited = set([start])

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

while queue:
    position, path = queue.popleft()

    if position == goal:
        print("Shortest Path:")
        print(path)
        break

    r, c = position

    for dr, dc in directions:
        nr = r + dr
        nc = c + dc

        if (0 <= nr < rows and
            0 <= nc < cols and
            maze[nr][nc] == 0 and
            (nr, nc) not in visited):

            visited.add((nr, nc))
            queue.append(((nr, nc), path + [(nr, nc)]))
else:
    print("No Path Found")
