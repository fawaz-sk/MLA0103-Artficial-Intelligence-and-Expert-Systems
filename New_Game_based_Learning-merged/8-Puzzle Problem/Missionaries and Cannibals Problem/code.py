from collections import deque

start = (3, 3, 1)
goal = (0, 0, 0)

moves = [
    (1, 0),
    (2, 0),
    (0, 1),
    (0, 2),
    (1, 1)
]

queue = deque([(start, [])])
visited = set()

def valid(state):
    m, c, boat = state

    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    if m > 0 and m < c:
        return False

    rm = 3 - m
    rc = 3 - c

    if rm > 0 and rm < rc:
        return False

    return True

while queue:
    state, path = queue.popleft()

    if state == goal:
        print("Solution Found")
        for step in path:
            print(step)
        break

    if state in visited:
        continue

    visited.add(state)

    m, c, boat = state

    for dm, dc in moves:
        if boat == 1:
            new_state = (m - dm, c - dc, 0)
        else:
            new_state = (m + dm, c + dc, 1)

        if valid(new_state) and new_state not in visited:
            queue.append((new_state, path + [new_state]))
