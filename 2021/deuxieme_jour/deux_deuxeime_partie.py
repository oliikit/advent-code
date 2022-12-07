rock = ("A", 1)
paper = ("B", 2)
scissors = ("C", 3)
lose = ("X", 0)
draw = ("Y", 3)
win = ("Z", 6)
total_points = 0

with open("strategy.txt", "r") as f:
    strategy = f.read().splitlines()

    for i in range(len(strategy)):
        opponent = strategy[i][0]
        my_move = strategy[i][2]

        if opponent in rock:
            if my_move in draw:
                total_points += rock[1]
                total_points += draw[1]
            if my_move in win:
                total_points += paper[1]
                total_points += win[1]
            if my_move in lose:
                total_points += scissors[1]
                total_points += lose[1]

        if opponent in scissors:
            if my_move in draw:
                total_points += scissors[1]
                total_points += draw[1]
            elif my_move in win:
                total_points += rock[1]
                total_points += win[1]
            elif my_move in lose:
                total_points += paper[1]
                total_points += lose[1]
        
        if opponent in paper:
            if my_move in draw:
                total_points += paper[1]
                total_points += draw[1]
            elif my_move in win:
                total_points += scissors[1]
                total_points += win[1]
            elif my_move in lose:
                total_points += rock[1]
                total_points += lose[1]

print(total_points)