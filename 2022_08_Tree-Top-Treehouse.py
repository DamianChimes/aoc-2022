# Day 8: Treetop Tree House
import numpy as np

def problem_1(f):
    lines = f.read().split('\n')
    grid = []
    for line in lines:
        row = [int(num) for num in line]
        grid.append(row)

    grid = np.array(grid)

    # To avoid double counting trees (eg. corners, top & left), creating a flag for each spot
    visible_tree = np.zeros(grid.shape)

    # Now we can compare heights for each direction

    # Assumption: Order of checks don't matter, so we can check all direction at once
    for idx in range(grid.shape[1]):
        for idy in range(grid.shape[0]):

            tree = grid[idy,idx]

            # Trees on the edge are automatically visible
            if (len(grid[:idy, idx]) == 0) or (len(grid[idy, :idx]) == 0):
                visible_tree[idy, idx] = 1
                continue

            if grid[idy:, idx].size == 1 or grid[idy, idx:].size == 1:
                visible_tree[idy, idx] = 1
                continue                

            # Note we only need to find visibility in one direction
            # Top:
            if tree > grid[:idy, idx].max():
                visible_tree[idy, idx] = 1
                continue
            # Left:
            if tree > grid[idy, :idx].max():
                visible_tree[idy, idx] = 1
                continue
            # Down:
            if tree > grid[(idy+1):, idx].max():
                visible_tree[idy, idx] = 1
            # Right:
            if tree > grid[idy, (idx+1):].max():
                visible_tree[idy, idx] = 1
    
    return visible_tree.sum()

def problem_2(f):
    lines = f.read().split('\n')
    grid = []
    for line in lines:
        row = [int(num) for num in line]
        grid.append(row)

    grid = np.array(grid)

    # Now we can compare heights for each direction
    max_scenic_score = 0

    # Assumption: Order of checks don't matter, so we can check all direction at once
    # For problem 2, we exclude the outer ring (visibility of 0 trees)
    for idx in range(1, grid.shape[1]-1):
        for idy in range(1, grid.shape[0]-1):
            scenic_score = 1
            tree = grid[idy,idx]

            # Top
            view_distances = np.where(grid[:(idy-1), idx] >= tree)[0]

            if len(view_distances) == 0: # No tree in view
                score = idy
            else:
                score = idy - max(view_distances)

            scenic_score *= score

            # Left
            view_distances = np.where(grid[idy, :(idx-1)] >= tree)[0]
            
            if len(view_distances) == 0: # No tree in view
                score = idx
            else:
                score = idx - max(view_distances)
            scenic_score *= score

            # Bottom
            view_distances = np.where(grid[(idy+1):, idx] >= tree)[0]
            if len(view_distances) == 0: # No tree in view
                score = grid.shape[0] - idy - 1
            else:
                score = min(view_distances) + 1
            scenic_score *= score

            # Right
            view_distances = np.where(grid[idy, (idx+1):] >= tree)[0]
            if len(view_distances) == 0: # No tree in view
                score = grid.shape[1] - idx - 1
            else:
                score = min(view_distances) + 1
            scenic_score *= score

            max_scenic_score = max(max_scenic_score, scenic_score)

    return max_scenic_score

# Problem 1
with open('day/8/input.txt', 'r') as f:
    result = problem_1(f)
    print('Problem 1:', result) # 868 too low | #9801 too high

# Problem 2
with open('day/8/input.txt', 'r') as f:
    result = problem_2(f)
    print('Problem 2:', result) #2460640 Too high # 604998 Too High