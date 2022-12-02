import numpy as np

from collections import defaultdict

# Input represents each elf's food calories
# Spaces separate each elf

file_loc = 'day/1/input.txt'     # To read the input file
dict_elves = defaultdict(list)   # To store each elves calories

# Part 1:
elf_num = 0

with open(file_loc, 'r') as f:
    for line in f.readlines():
        if line == '\n':
            elf_num += 1
            continue
        dict_elves[elf_num].append(int(line))

# To find the maximum calories, sum each elves calories and find the elf with the max
elf_calories = np.array([sum(dict_elves[i]) for i in dict_elves.keys()])
max_calories, max_elf = np.max(elf_calories), np.argmax(elf_calories)

print(f'Maximum calories are {max_calories} held by elf no. {max_elf}')
#print(max(dict_elves, key=sum(dict_elves.get)))

# Part 2:
top_3_calories = np.sort(elf_calories)[-3:].sum()
print(f'The total calories of the top-3 elves is: {top_3_calories}')
