# Part 1
encrypted_strategy_guide = 'day/2/input.txt'

opponent_move = {'A':'Rock', 'B': 'Paper', 'C': 'Scissors'}
my_move = {'X':'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
move_points = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
round_points = {'Loss': 0, 'Draw': 3, 'Win': 6}

total_score = 0

with open(encrypted_strategy_guide, 'r') as f:
    for line in f.readlines():
        round_score = 0
        moves = line.split()

        # Determine round outcome
        if opponent_move[moves[0]] == my_move[moves[1]]:
            outcome = 'Draw'
        elif opponent_move[moves[0]] == 'Rock':
            if my_move[moves[1]] == 'Paper':
                outcome = 'Win'
            else:
                outcome = 'Loss'

        elif opponent_move[moves[0]] == 'Paper':
            if my_move[moves[1]] == 'Scissors':
                outcome = 'Win'
            else:
                outcome = 'Loss'

        elif opponent_move[moves[0]] == 'Scissors':
            if my_move[moves[1]] == 'Rock':
                outcome = 'Win'
            else:
                outcome = 'Loss'

        # Add scores
        round_score = move_points[my_move[moves[1]]] + round_points[outcome]
        total_score += round_score

print('Round 1:', total_score)

# Part 2
my_result = {'X': 'Loss', 'Y': 'Draw', 'Z': 'Win'}

total_score = 0

with open(encrypted_strategy_guide, 'r') as f:
    for line in f.readlines():
        round_score = 0
        moves = line.split()

        if my_result[moves[1]] == 'Draw':
            round_score += move_points[opponent_move[moves[0]]]

        elif my_result[moves[1]] == 'Win':
            if opponent_move[moves[0]] == 'Rock':
                round_score += move_points['Paper']
            elif opponent_move[moves[0]] == 'Paper':
                round_score += move_points['Scissors']
            elif opponent_move[moves[0]] == 'Scissors':
                round_score += move_points['Rock']
            else:
                print('Missed @ WIN')

        elif my_result[moves[1]] == 'Loss':
            if opponent_move[moves[0]] == 'Rock':
                round_score += move_points['Scissors']
            elif opponent_move[moves[0]] == 'Paper':
                round_score += move_points['Rock']
            elif opponent_move[moves[0]] == 'Scissors':
                round_score += move_points['Paper']
            else:
                print('Missed @ Loss')
        else:
            print('Missed @ MyResult')

        round_score += round_points[my_result[moves[1]]]
        total_score += round_score

print('Round 2:', total_score) #11800 WRONG

