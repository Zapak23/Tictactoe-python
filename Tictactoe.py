# Tic Tac Toe
def print_board(board):
    for row in range(len(board[0])):
        print('   |'*len(board))

        row_with_items = ''
        for column in range(len(board)):
            row_with_items += (' '+str(board[row][column])) + ' |'
        print(row_with_items)
        print('   |'*len(board))
        print('---+'*len(board))

def move_valid(board, move):
    if move == 1 and board[0][0] == '1':
        return True
    if move == 2 and board[0][1] == '2':
        return True
    if move == 3 and board[0][2] == '3':
        return True
    if move == 4 and board[1][0] == '4':
        return True
    if move == 5 and board[1][1] == '5':
        return True
    if move == 6 and board[1][2] == '6':
        return True
    if move == 7 and board[2][0] == '7':
        return True
    if move == 8 and board[2][1] == '8':
        return True
    if move == 9 and board[2][2] == '9':
        return True
    else:
        return False

def available_moves(board):
    available = []
    for row in range(len(board[0])):
        for column in range (len(board)):
            if board[row][column] != 'X' and board[row][column] !='O':
                available.append(board[row][column])
    available = list(map(int, available))
    return available

def select_space(board, player, move):
    if move_valid(board, move):
        if move == 1:
            board[0][0] = player
        elif move == 2:
            board[0][1] = player
        elif move == 3:
            board[0][2] = player
        elif move == 4:
            board[1][0] = player
        elif move == 5:
            board[1][1] = player
        elif move == 6:
            board[1][2] = player
        elif move == 7:
            board[2][0] = player
        elif move == 8:
            board[2][1] = player
        elif move == 9:
            board[2][2] = player

def has_won(board, player):
    # horizontal win scenario
    for x in range(len(board[0])):
        for y in range (len(board) - 2):
            if board[x][y] == player and board[x][y+1] == player and board[x][y+2] == player:
                return True
    # vertical win scenario
    for x in range(len(board[0]) - 2):
        for y in range (len(board)):        
            if board[x][y] == player and board[x+1][y] == player and board[x+2][y] == player:
                return True
    # diagonal / win scenario
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True
    # diagonal \ win scenario
    if board[0][0] == player and board [1][1] == player and board[2][2] == player:
        return True

def game_over(board):
    return has_won(board, 'X') or has_won(board, 'O') or len(available_moves(board)) == 0

def play_game():
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    
    turn = 'X'
    
    while (not game_over(board)):
        moves = available_moves(board)
        print_board(board)
        move = 0

        while (move not in moves):
            move = int(input("It is " + turn + "'s turn, your options are " + str(moves)))
            select_space(board, turn, move)

        if has_won(board, turn):
            print()
            print()
            print(turn + ' has won!')
            print_board(board)
            break

        if game_over(board):
            print()
            print()  
            print("It's a Tie!")
            print_board(board)
        
        if turn == 'X':
            turn = 'O'
        else: turn = 'X'

play_game()