import re
import numpy as np

# this is a hideous solution but c'est la vie

def filter_val(ls, val):
    if val in ls:
        ls.remove(val)
        print(ls) 
    return ls

def find_non_empty_crate(crates):
    for i, crate in enumerate(crates):
        if crate != "o":
            return i

def rearrange_crates(crates, move):
    num_to_move = move[0]
    crate_to_move = move[1] - 1
    crate_to_move_to = move[2] - 1

    c_remove = crates[crate_to_move]
    c_insert = crates[crate_to_move_to]

    print(move)
    print(f'OLD CRATE - removed: {c_remove}')
    print(f'OLD CRATE - added:   {c_insert}')

    remove_crates = c_remove[:num_to_move]

    for i, crate in enumerate(remove_crates):
        c_insert.insert(i, crate)
    
    for i in range(num_to_move):
        del c_remove[0]

    return crates 

with open("crates.txt", "r") as file:
    file_arr = file.readlines()

    hor_crates = file_arr[0:9]
    hor_crates = [[c.replace("[", "").replace("]", "").replace("\n", "") for c in crate.split(" ")] for crate in hor_crates]
    # transpose crates to be vertical
    np_crates = np.array(hor_crates)
    crates = np_crates.transpose()
    # don't want a numpy array
    crates = list(crates)
    crates = [list(c) for c in crates]
    # further data sanitization - don't need o's
    crates = [[str(c) for c in crate if c != "o"] for crate in crates]

    # extracts from from string
    # first number is number of crates to move
    # second number is the number of the crate to move
    # third number is the number of the crate to move to
    moves = file_arr[11:]
    moves = [re.findall(r'\d+', m) for m in moves]
    moves = [[int(i) for i in m] for m in moves]

    for move in moves:
        print(f'MOVE: {moves.index(move)}')
        try:
            rearrange_crates(crates, move)
        except:
            print(f'ERROR: {move}')
            break



        crate_to_move = move[1] - 1
        crate_to_move_to = move[2] - 1

        c_remove = crates[crate_to_move]
        c_insert = crates[crate_to_move_to]
        print(f'NEW CRATE - removed: {c_remove}')
        print(f'NEW CRATE - add:     {c_insert}')
        print()


    end_crates = ''
    for c in crates:
        end_crates += c[0]
    print(end_crates)