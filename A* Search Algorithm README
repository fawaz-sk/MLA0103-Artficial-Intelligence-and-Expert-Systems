START
Create a priority queue.
Insert the start node.

WHILE priority queue is not empty DO
    Remove node with smallest f(n).

    IF node is goal THEN
        Display total path cost.
        STOP.
    END IF

    FOR each neighbouring node DO
        Calculate:
            g(n) = path cost
            h(n) = heuristic value
            f(n) = g(n) + h(n)
        Insert neighbour into priority queue.
    END FOR
END WHILE

STOP
