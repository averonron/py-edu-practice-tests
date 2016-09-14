import random

grid_val = [" ", " ", " ", " ", " ", " ", " ", " ", " "]   # [" "] * 9
GRID_WIDTH = 13

CORNERS = (1, 3, 7, 9)
MIDDLES = (2, 4, 6, 8)
CENTER = (5,)
avail_pos = list(CORNERS + MIDDLES + CENTER)

HUMAN = 1
MACHINE = 2
PLAYER = {HUMAN: 'Human', MACHINE: 'Machine'}
move = [None, [], []]

cur_player = None
winner = None
draw = False

win_comb = [
    (1, 2, 3), (4, 5, 6), (7, 8, 9),
    (1, 4, 7), (2, 5, 8), (3, 6, 9),
    (1, 5, 9), (3, 5, 7)
]

signs = [None, 'X', 'O']
player_sign = (None,)

choice = (1, 2)

def set_first_player():
    global cur_player
    first_player = None
    
    print("Who will first?")
    print("Human - 1")
    print("Machine - 2")

    while first_player not in choice:
        try:
            first_player = int(input("Input 1 or 2: "))
        except ValueError:
            continue

    cur_player = first_player


def swap_player():
    global cur_player
    cur_player = HUMAN if cur_player == MACHINE else MACHINE


def set_signs():
    global signs, player_sign
    hum_sign = None
    print("Select your sign:")
    print("\"X\" - 1")
    print("\"0\" - 2")

    while hum_sign not in choice:
        try:
            hum_sign = int(input("Input 1 or 2: "))
        except ValueError:
            continue
    
    player_sign += (signs.pop(hum_sign),)
    player_sign += (signs.pop(),)
    del signs


def add_move_to_list(pos):
    global move
    move[cur_player].append(pos)


def remove_pos_from_avail(pos):
    avail_pos.remove(pos)


def get_pos():
    if cur_player == HUMAN:
        return get_human_pos()
    else:
        return get_machine_pos()
    # return get_human_pos if cur_player is HUMAN else get_machine_pos


def get_human_pos():
    pos = None
    while pos not in avail_pos:
        try:
            pos = int(input("Make your move, man: "))
        except ValueError:
            continue
        if pos == 0:
            return 0
    pos_handle(pos)
    return pos


## ----- machine move exec -----

def getin(perc):
    """Return True in perc% cases"""
    tempint = random.randint(1, 100)
    intrange = range(1, perc + 1)
    if tempint in intrange:
        return True

def prob_choice(prob, *seq):
    """ """
    if len(prob) != len(seq)-1:
        raise ("ArgumentError")
    prob += (100,)
    
    for (pr, sq) in zip(prob, seq):
        if getin(pr) and sq:   ## 'sq' may be empty - busy center
            return random.choice(sq)

def get_avail_pos(region):
    """Exec available positions in regions: CORNERS or MIDDLES or CENTER"""
    avail = tuple(set(avail_pos) & set(region))   ## Common elements in avail and region
    return avail

def rand_pos():
    """temp func returns rand position"""
    return random.choice(avail_pos)

def get_machine_pos():
    """ """
    avail_center = get_avail_pos(CENTER)
    avail_corners = get_avail_pos(CORNERS)
    avail_middles = get_avail_pos(MIDDLES)
    
    ## if no moves yet, 90% to center, 95% to corners, middles otherwise
    if len(move[HUMAN]) == len(move[MACHINE]) == 0:
        pos = prob_choice((90, 95), CENTER, CORNERS, MIDDLES)

    ## human did a move, if center is free - 95% to center, 95% to corners, middles otherwise
    elif len(move[HUMAN]) == 1 and len(move[MACHINE]) == 0:
        pos = prob_choice((95, 95), avail_center, avail_corners, avail_middles)
    
    elif len(move[HUMAN]) == 1 and len(move[MACHINE]) == 1:
        pass

    else: pos = rand_pos()
    
    print("Machine chose: ", pos)
    pos_handle(pos)
    return pos






def pos_handle(pos):
    add_move_to_list(pos)
    remove_pos_from_avail(pos)

def probab(prob):
    if random.randint(1, 100) in range(1, prob):
        return True


# Define whether seq contains subseq
def contain_seq(seq, subseq):
    for elem in subseq:
        if elem not in seq:
            return False
    else:
        return True


def draw_grid(new_pos = None):
    if new_pos:
        grid_val[new_pos-1] = player_sign[cur_player]   # HUMAN or MACHINE
    
    # dash line "--------------"
    dash = "-"
    dash_line = dash * GRID_WIDTH
    
    # empty line "|   |   |   |"
    sub_line = "|   "
    line_end = "|"
    empty_line = sub_line*3 + line_end
    
    # line with values like "| X |   | O |"
    def value_line(p1, p2, p3):
        start = "| "
        mid = " | "
        end = " |"
        line = start + grid_val[p1] + mid + grid_val[p2] + mid + grid_val[p3] + end
        return line

    def draw_row(points):
        print(dash_line)
        print(empty_line)
        print(value_line(*points))
        print(empty_line)
    
    def draw_all_rows():
        line_points = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
        for points in line_points:
            draw_row(points)
        print(dash_line)
    
    draw_all_rows()


def check_win():
    global winner
    if len(move[cur_player]) >= 3:
        for comb in win_comb:
            if contain_seq(move[cur_player], comb):
                winner = cur_player
                break

def check_draw():
    global draw
    if not avail_pos:
        draw = True

def game_over():
    check_win()
    if winner:
        return True
    check_draw()
    if draw:
        return True
    # return False

set_signs()
set_first_player()

while True:
    pos = get_pos()
    if pos == 0:
        break
    draw_grid(pos)
    # print(avail_pos)
    # print(move[cur_player])
    
    if game_over():
        break
    
    swap_player()


if winner:
    winner_msg = "Winner is - " + PLAYER[cur_player]
    print(winner_msg)
elif draw:
    draw_msg = "Draw"
    print(draw_msg)
else:
    exit_msg = "You left the game by yourself.\nBye"
    print(exit_msg)

"""

set_signs()
print(player_sign)


set_first_player()
print(cur_player)
swap_player()
print(cur_player)
"""