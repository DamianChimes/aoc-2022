# Day 1: Calorie Counting

def problem_1(f):
    elf_calories = 0
    group_calories = []
    for line in f.readlines():
        if line == '\n':
            group_calories.append(elf_calories)
            elf_calories = 0
            continue
        
        elf_calories += int(line)
    group_calories.append(elf_calories) # Ensure last group is captured

    return group_calories

def problem_2(group_calories, top_n=3):
    return sorted(group_calories, reverse=True)[:top_n]

# Read file
with open('day/1/input.txt') as f:
    group_calories = problem_1(f)

# Problem 1
print('Maximum single calories:', max(group_calories))

# Problem 2
print('Sum of top-3 elf calories:', sum(problem_2(group_calories, 3)))

# End
