# Day 2: Rock-Paper-Scissors

def problem_1(f):
    # Rock: 1, Paper: 2, Scissors: 3
    round_results = []
    for round in f.readlines():
        moves = round.split()
        opp_move, my_move = ('A','B','C').index(moves[0]), ('X', 'Y', 'Z').index(moves[1])
        outcome = my_move - opp_move

        # The modulo enables corrections for 0 - 2
        round_score = (my_move+1) + ((outcome+1) % 3) * 3
        round_results.append(round_score)

    return round_results

def problem_2(f):
    round_results = []
    for round in f.readlines():
        plan = round.split()
        opp_move, outcome = ('A','B','C').index(plan[0]), ('X', 'Y', 'Z').index(plan[1])
        my_move = (opp_move + (outcome-1)) % 3

        round_score = (my_move+1) + outcome*3
        round_results.append(round_score)

    return round_results

with open('day/2/input.txt', 'r') as f:
    round_results_1 = problem_1(f)

with open('day/2/input.txt', 'r') as f:
    round_results_2 = problem_2(f)

# Problem 1:
print('Round 1:', sum(round_results_1))

# Problem 2:
print('Round 2:', sum(round_results_2)) #11800 WRONG

# End