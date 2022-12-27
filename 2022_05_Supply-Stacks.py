# Day 5: Supply Stacks
from collections import defaultdict

def problem_1(f):

    # First we have to read the crate allocations
    start_stacks = True
    stacks = {}

    while start_stacks:
        line = f.readline()
        # Once we hit numbers, the set-up is complete
        if '1' in line:
            start_stacks = False

        # For each character, keep a running count - add new items at the start
        for idx, char in enumerate(line):
            if char.isalpha():
                stack_id = idx//4 + 1
                stacks.setdefault(stack_id, []).insert(0, char)

    for procedure in f.readlines():
        if len(procedure)==1:
            continue
        
        actions = procedure.split()
        num_moves, start, end = int(actions[1]), int(actions[3]), int(actions[5])

        for _ in range(num_moves):
            crate = stacks[start].pop()
            stacks[end].append(crate)

    return stacks

def problem_2(f):

    # First we have to read the crate allocations
    start_stacks = True
    stacks = {}

    while start_stacks:
        line = f.readline()
        # Once we hit numbers, the set-up is complete
        if '1' in line:
            start_stacks = False

        # For each character, keep a running count - add new items at the start
        for idx, char in enumerate(line):
            if char.isalpha():
                stack_id = idx//4 + 1
                stacks.setdefault(stack_id, []).insert(0, char)

    for procedure in f.readlines():
        if len(procedure)==1:
            continue
        
        actions = procedure.split()
        num_crates, start, end = int(actions[1]), int(actions[3]), int(actions[5])

        # Instead of 1 by 1, move all 'num_crates' crates to the end of the new location
        stacks[end] += stacks[start][-num_crates:]
        stacks[start] = stacks[start][:-num_crates]

    return stacks

# Problem 1
with open('day/5/input.txt', 'r') as f:
    result = problem_1(f)
    print('Problem 1:', ''.join([result[i][-1] for i in sorted(result.keys())]))

# Problem 2
with open('day/5/input.txt', 'r') as f:
    result = problem_2(f)
    print('Problem 2:', ''.join([result[i][-1] for i in sorted(result.keys())]))