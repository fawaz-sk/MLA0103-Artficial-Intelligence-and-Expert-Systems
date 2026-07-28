START
Create a priority queue.
Insert the start node using heuristic value.

WHILE priority queue is not empty DO
    Remove node with smallest heuristic.
    Display node.

    IF node is goal THEN
        STOP.
    END IF

    Add neighbouring nodes using heuristic values.
END WHILE

STOP
