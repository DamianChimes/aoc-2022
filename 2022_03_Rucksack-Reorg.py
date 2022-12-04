# Day 3: Rucksack Reorganisation
import re
def problem_1(f):
    sum_priority = 0
    for rucksack in f.readlines():
        # Remove special characters
        rucksack_letters = re.sub('[^a-zA-Z]', '', rucksack)
        compartment1, compartment2 = rucksack_letters[:(len(rucksack_letters))//2], rucksack_letters[(len(rucksack_letters))//2:]

        item = list((set(compartment1) & set(compartment2)))[0]

        if item == item.upper():
            priority = ord(item)-64 + 26
        if item == item.lower():
            priority = ord(item)-96


        sum_priority += priority

    return sum_priority

def problem_2(f):
    sum_priority = 0

    rucksacks = f.read().split()
    for i in range(0, len(rucksacks), 3):
        ruck_1, ruck_2, ruck_3 = rucksacks[i:i+3]

        item = list((set(ruck_1) & set(ruck_2) & set(ruck_3)))[0]

        if item == item.upper():
            priority = ord(item)-64 + 26
        if item == item.lower():
            priority = ord(item)-96


        sum_priority += priority

    return sum_priority

# Problem 1
with open('day/3/input.txt', 'r') as f:
    print(problem_1(f))

# Problem 2
with open('day/3/input.txt', 'r') as f:
    print(problem_2(f))