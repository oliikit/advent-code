# 1 for rock
# 2 for paper
# 3 for scissors
# 6 if won
# 0 if lost
# 3 for draw

rock = ("A", "X", 1)
paper = ("B", "Y", 2)
scissors = ("C", "Z", 3)
win = 6
lose = 0
draw = 3
total_points = 0

with open("strategy.txt", "r") as f:
    strategy = f.read().splitlines()

    for i in range(len(strategy)):
        opponent = strategy[i][0]
        my_move = strategy[i][2]

        if opponent in rock:
            if my_move in rock:
                total_points += rock[2]
                total_points += draw
            elif my_move in paper:
                total_points += paper[2]
                total_points += win
            elif my_move in scissors:
                total_points += scissors[2]
                total_points += lose
        
        if opponent in scissors:
            if my_move in scissors:
                total_points += scissors[2]
                total_points += draw
            elif my_move in rock:
                total_points += rock[2]
                total_points += win
            elif my_move in paper:
                total_points += paper[2]
                total_points += lose
        
        if opponent in paper:
            if my_move in paper:
                total_points += paper[2]
                total_points += draw
            elif my_move in scissors:
                total_points += scissors[2]
                total_points += win
            elif my_move in rock:
                total_points += rock[2]
                total_points += lose

print(total_points)