import copy
SIZE = 3

def main():
    initial = [
        [1, 2, 3],
        [0, 4, 6],
        [7, 5, 8]
    ]
    goal= [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    print_state(initial)
    print_state(goal)
    a_star(initial,goal)

def print_state(state):
    for i in range(SIZE):
        for j in range(SIZE):
            print(state[i][j], end=" ")
        print()

def calculate_hvalue_of_a_state(state1, state2):
    h = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if state1[i][j] != state2[i][j]:
                h += 1
    return h

def find_empty_space(state):
    for i in range(SIZE):
        for j in range(SIZE):
            if state[i][j] == 0:
                return i, j

def left_move(state):
    new_state = copy.deepcopy(state)

    for i in range(SIZE):
        for j in range(SIZE):
            if new_state[i][j] == 0 and j > 0:
                new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
                return new_state

    return None  # No left move possible

def right_move(state):
    new_state = copy.deepcopy(state)

    for i in range(SIZE):
        for j in range(SIZE-1):
            if new_state[i][j] == 0 and j<SIZE-1:
                new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]
                return new_state

    return None  # No right move possible

def up_move(state):
    new_state = copy.deepcopy(state)

    for i in range(SIZE):
        for j in range(SIZE):
            if new_state[i][j] == 0 and i>0:
                new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
                return new_state

    return None  # No up move possible

def down_move(state):
    new_state = copy.deepcopy(state)

    for i in range(SIZE):
        for j in range(SIZE):
            if new_state[i][j] == 0 and i<SIZE-1:
                new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
                return new_state

    return None  # No up move possible

def a_star(initial, goal):
    g = 0
    a = []
    b = []
    max_iterations=100
    while initial!= goal and g<max_iterations:
        f1, f2, f3, f4 = 0, 0, 0, 0
        g += 1

        state_1 = left_move(initial)
        if state_1 is not None:
            h1 = calculate_hvalue_of_a_state(goal, state_1)
            print("h1: ",h1)
            f1 = g + h1
            b.append(f1)

        state_2 = right_move(initial)
        if state_2 is not None:
            h2 = calculate_hvalue_of_a_state(goal, state_2)
            print("h2:",h2)
            f2 = g + h2
            b.append(f2)

        state_3 = up_move(initial)
        if state_3 is not None:
            h3 = calculate_hvalue_of_a_state(goal, state_3)
            print("h3:",h3)
            f3 = g + h3
            b.append(f3)

        state_4 = down_move(initial)
        if state_4 is not None:
            h4 = calculate_hvalue_of_a_state(goal, state_4)
            print("h4:",h4)
            f4 = g + h4
            b.append(f4)

        print("b: ",b)
        f = min(b)

        if f == f1:
            new_state = state_1
        elif f == f2:
            new_state = state_2
        elif f == f3:
            new_state = state_3
        elif f == f4:
            new_state = state_4

        a.append(copy.deepcopy(new_state))
        initial = copy.deepcopy(new_state)

        print("States:")
        for matrix in a:
            for row in matrix:
                print(row)
            print()

        b.clear()


if __name__ == "__main__":
    main()