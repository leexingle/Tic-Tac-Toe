import random

playing = 'Y'
winner = None
count = 0
row = 0
column = 0
turn_list = [0,1]

place = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']

# combination of winning
win_list = [[0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]]


def game_board(): # printing game board

    print( place[0] + ' | ' + place[1] + ' | ' + place[2] )
    print( place[3] + ' | ' + place[4] + ' | ' + place[5] )
    print( place[6] + ' | ' + place[7] + ' | ' + place[8] )


def user_turn(): # input user move
    global row
    global column
    input_correct = 'N'

    while input_correct == 'N':
        print('Please play your move. By row and column.')
        row = int(input("Row: "))
        column = int(input("Column: "))
        move = (row - 1) * 3 + (column - 1)

        if row > 3 or row < 1 or column > 3 or column < 1:
            print("Wrong input! Try again.")

        elif place[move] != ' ':
            print('Move is taken. Try again.')

        else:
            place[move] = 'X'
            input_correct = "Y"

    win()


def comp_turn(): # determine computer move
    global row
    global column

    i = 0
    for x in win_list:
        count_o = 0
        for y in x:
            if place[y] == 'O':
                count_o += 1
                if count_o == 2:
                    for y in x:
                        if place[y] == ' ':
                            place[y] = 'O'
                            if y == 0 or y == 1 or y == 2:
                                row = 1
                            elif y == 3 or y == 4 or y == 5:
                                row = 2
                            else:
                                row = 3
                            if y == 0 or y == 3 or y == 6:
                                column = 1
                            elif y == 1 or y == 4 or y == 7:
                                column = 2
                            else:
                                column = 3

                            i = 1
        if i == 1:
            break

    if i == 0:
        for x in win_list:
            count_x = 0
            for y in x:
                if place[y] == 'X':
                    count_x += 1
                    if count_x == 2:
                        for y in x:
                            if place[y] == ' ':
                                place[y] = 'O'
                                if y == 0 or y == 1 or y == 2:
                                    row = 1
                                elif y == 3 or y == 4 or y == 5:
                                    row = 2
                                else:
                                    row = 3
                                if y == 0 or y == 3 or y == 6:
                                    column = 1
                                elif y == 1 or y == 4 or y == 7:
                                    column = 2
                                else:
                                    column = 3

                                i = 1
            if i == 1:
                break

    if i == 0:
        available_move = 'N'
        while available_move == 'N':
            y = random.randint(0, 8)
            if place[y] == ' ':
                place[y] = 'O'
                if y == 0 or y == 1 or y == 2:
                    row = 1
                elif y == 3 or y == 4 or y == 5:
                    row = 2
                else:
                    row = 3
                if y == 0 or y == 3 or y == 6:
                    column = 1
                elif y == 1 or y == 4 or y == 7:
                    column = 2
                else:
                    column = 3
                available_move = 'Y'

    win()


def win(): # determine is there a winner

    global winner
    for x in win_list:

        if place[x[0]] == place[x[1]] == place[x[2]] and place[x[0]] != " ":
            winner = place[x[0]]


def check_win(): # determine who is the winner

    if winner == 'X':
        game_board()
        print('You win!')
        return True

    elif winner == 'O':
        game_board()
        print('You lose!')
        return True


def tie(): # determine is there a tie

    if " " not in place:
        game_board()
        print("It is a tie!")
        return True


def log_file(user, piece):
    file = open('logfile_21030234.txt', 'a')
    file.write(str(count) + ',' + str(user) + ',' + str(row) + ',' + str(column) + ',' + str(piece) + '\n')
    file.close()


# game play
# determine who have the first turn
first_turn = random.choice(turn_list)
if first_turn == 0:
    comp_turn()
    count += 1
    log_file('C', 'O')

while playing == 'Y':
    game_board()
    user_turn()
    count += 1
    log_file('H', 'X')

    if check_win():
        playing = 'N'

    elif tie():
        playing = 'N'

    else:
        comp_turn()
        count += 1
        log_file('C', 'O')

        if check_win():
            playing = 'N'

        elif tie():
            playing = 'N'





