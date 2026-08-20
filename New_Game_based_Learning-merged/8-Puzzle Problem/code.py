from collections import deque

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

queue = deque([(start, [])])
visited = set()

while queue:
    state, path = queue.popleft()

    if state == goal:
        print("Puzzle Solved!")
        print("Number of Moves:", len(path))
        for step in path:
            print(step)
        break

    if state in visited:
        continue

    visited.add(state)
    zero = state.index(0)

    for move in moves[zero]:
        new_state = list(state)
        new_state[zero], new_state[move] = new_state[move], new_state[zero]
        new_state = tuple(new_state)

        if new_state not in visited:
            queue.append((new_state, path + [new_state]))
