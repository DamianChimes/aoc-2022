# Day 6: Tuning Trouble

def problem_1(f):
    signal = f.read()
    marker = []

    for i, char in enumerate(signal):
        marker.append(char)
        marker = marker[-4:]

        if len(set(marker))==4:
            print('Found unique set:', marker)
            break

    return (i+1)


    return result

def problem_2(f, num_unq):
    signal = f.read()
    marker = []
    
    for i, char in enumerate(signal):
        marker.append(char)
        marker = marker[-num_unq:]

        if len(set(marker))==14:
            print('Found unique set:', marker)
            break

    return (i+1)

# Problem 1
with open('day/6/input.txt', 'r') as f:
    result = problem_1(f)
    print('Problem 1:', result)

# Problem 2
with open('day/6/input.txt', 'r') as f:
    result = problem_2(f, 14)
    print('Problem 2:', result)