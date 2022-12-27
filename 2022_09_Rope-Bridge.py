# Day 9: Rope Bridge
import numpy as np

def problem_1(f):
    # Create a large gride to move in
    grid = np.zeros((500,500))
    idx_head = 250
    idy_head = 250
    idx_tail = 250
    idy_tail = 250

    grid[idy_tail, idx_tail] = 1

    for move in f.read().split('\n'):
        #print(move)
        direction, times = move.split()
        for _ in range(int(times)):
            # Move the Head
            if direction == 'U':
                idy_head -= 1
            elif direction == 'D':
                idy_head += 1
            elif direction == 'L':
                idx_head -= 1
            elif direction == 'R':
                idx_head += 1
            
            # Move the Tail if needed
            idy_tail, idx_tail = move_knot(idy_head, idx_head, idy_tail, idx_tail)

            # Update Tail location
            grid[idy_tail, idx_tail] = 1     

    return grid.sum()

def problem_2(f):
    # Create a large gride to move in
    grid = np.zeros((500,500))

    # Create knots indexed from 0 (Head) to 9 (Last)

    idx = dict()
    idy = dict()
    for i in range(10):
        idy[i] = 250
        idx[i] = 250

    grid[idy[9], idx[9]] = 1

    for move in f.read().split('\n'):
        #print(move)
        direction, times = move.split()
        for _ in range(int(times)):
            # Move the Head
            if direction == 'U':
                idy[0] -= 1
            elif direction == 'D':
                idy[0] += 1
            elif direction == 'L':
                idx[0] -= 1
            elif direction == 'R':
                idx[0] += 1

            # Simulate all tail moves:
            for i in range(1, 10):
                idy[i], idx[i] = move_knot(idy[i-1], idx[i-1], idy[i], idx[i])

            #print([f'{i}: ({idy[i]}, {idx[i]})' for i in range(10)])

            # Update Tail location
            grid[idy[9], idx[9]] = 1

    return grid.sum()

def move_knot(idy_first, idx_first, idy_last, idx_last):
    if abs(idy_first - idy_last) > 1:
        if abs(idx_first - idx_last) > 1:
            idx_last = (idx_first+idx_last)//2
        elif abs(idx_first - idx_last) > 0:
            idx_last = idx_first
        idy_last = (idy_first+idy_last)//2

    if abs(idx_first - idx_last) > 1:
        if abs(idy_first - idy_last) > 1:
            idy_last = (idy_first+idy_last)//2
        elif abs(idy_first - idy_last) > 0:
            idy_last = idy_first
        idx_last = (idx_first+idx_last)//2

    return idy_last, idx_last


# Problem 1
with open('day/9/input.txt', 'r') as f:
    result = problem_1(f)
    print('Problem 1:', result)

# Problem 2
with open('day/9/input.txt', 'r') as f:
    result = problem_2(f)
    print('Problem 2:', result) #2465.0 too low