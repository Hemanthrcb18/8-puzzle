from heapq import heappush, heappop

START = (
    (2, 8, 3),
    (1, 6, 4),
    (7, 0, 5)
)

GOAL = (
    (1, 2, 3),
    (8, 0, 4),
    (7, 6, 5)
)

def manhattan(state):
    distance = 0

    for i in range(3):
        for j in range(3):

            value = state[i][j]

            if value != 0:

                for x in range(3):
                    for y in range(3):

                        if GOAL[x][y] == value:
                            distance += abs(i - x) + abs(j - y)

    return distance


def get_neighbors(state):

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                row, col = i, j

    moves = [(1,0),(-1,0),(0,1),(0,-1)]

    neighbors = []

    for dr, dc in moves:

        nr = row + dr
        nc = col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:

            temp = [list(r) for r in state]

            temp[row][col], temp[nr][nc] = \
                temp[nr][nc], temp[row][col]

            neighbors.append(tuple(tuple(r) for r in temp))

    return neighbors


def print_state(state):

    for row in state:
        print(*row)

    print()


def astar():

    pq = []

    h = manhattan(START)

    heappush(pq, (h, 0, START, [START]))

    visited = set()

    while pq:

        f, g, current, path = heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        print("Expanding State:")
        print_state(current)

        if current == GOAL:

            print("GOAL FOUND\n")

            print("Solution Path:\n")

            for step, state in enumerate(path):

                print("Step", step)
                print_state(state)

            print("Total Moves =", len(path)-1)
            print("Nodes Expanded =", len(visited))
            return

        for neighbor in get_neighbors(current):

            if neighbor not in visited:

                new_g = g + 1
                new_h = manhattan(neighbor)

                heappush(
                    pq,
                    (new_g + new_h,
                     new_g,
                     neighbor,
                     path + [neighbor])
                )

astar()