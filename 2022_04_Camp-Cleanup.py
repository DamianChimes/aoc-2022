# Day 4: Camp Cleanup

def problem_1(f):
    num_contained = 0
    assignments = f.read().split()
    for assignment in assignments:
            part_a, part_b = get_assignments(assignment)

            if len(part_a.difference(part_b))==0 or len(part_b.difference(part_a))==0:
                num_contained +=1

    return num_contained

def get_assignments(id_num):
    part_a, part_b = id_num.split(',')
    part_a = {x for x in range(int(part_a.split('-')[0]), int(part_a.split('-')[1])+1)}
    part_b = {x for x in range(int(part_b.split('-')[0]), int(part_b.split('-')[1])+1)}

    return part_a, part_b

def problem_2(f):
    num_overlap = 0
    assignments = f.read().split()
    for assignment in assignments:
            part_a, part_b = get_assignments(assignment)

            if len(part_a & part_b) > 0:
                num_overlap +=1

    return num_overlap

# Problem 1
with open('day/4/input.txt', 'r') as f:
    result = problem_1(f)
    print('Problem 1:', result) # 530 correct. 577 too high

# Problem 2
with open('day/4/input.txt', 'r') as f:
    result = problem_2(f)
    print('Problem 2:', result)