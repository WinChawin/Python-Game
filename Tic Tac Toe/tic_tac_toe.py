import random
import time

def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def display_board(board):
    print("     1   2   3")
    print(" ----------------")
    for i in range(3):
        print(f" {i+1} | {board[i][0]} | {board[i][1]} | {board[i][2]} |")
        print(" ----------------")
    print()

def check_winner(board, mark):
    for row in range(3):
        if(board[row][0] == board[row][1] == board[row][2] == mark):
            return True
        
    for col in range(3):
        if(board[0][col] == board[1][col] == board[2][col] == mark):
            return True
        
    if(board[0][0] == board[1][1] == board[2][2] == mark):
        return True
    
    if(board[0][2] == board[1][1] == board[2][0] == mark):
        return True

    return False
    
def full_board(board):
    for i in range(3):
        for j in  range(3):
            if(board[i][j] == " "):
                return False
    return True

def place_mark(board, row, col, mark):
    board[row][col] = mark

def choose_start_player():
    print("You are Player 1 and Bot is Player 2.")
    print("Who will start first?")
    start = input("'1' for Player 1 or '2' for Bot: ")
    start_player = 'Player 1' if start == '1' else 'Bot'

    choose = input("Choose 'X' or 'O': ").upper()
    player_mark = choose
    bot_mark = 'O' if choose == 'X' else 'X'


    print(f"Player 1 is '{choose}' and Bot is '{bot_mark}'")
    print(f"{'Player 1' if start == '1' else 'Bot'} will start first.")

    return {
        'current_player' : start_player,
        'player_mark' : player_mark,
        'bot_mark' : bot_mark
    }

def is_valid_move(board, row, col):
    if(row < 0 or row > 2 or col < 0 or col > 2):
        return False
    return board[row][col] == " "

def get_player_move(board):
    row = int(input("Choose your row (1-3): ")) - 1
    col = int(input("Choose your column (1-3): ")) - 1

    if(is_valid_move(board, row, col)):
        return row, col
    else:
        print("Invalid move. Try again.")
        return get_player_move(board)
    
def get_bot_move(board):
    time.sleep(1)

    empty = []
    for i in range(3):
        for j in  range(3):
            if(board[i][j] == " "):
                empty.append((i,j))

    if empty:
        row, col = random.choice(empty)
        return row, col
    
    return None, None

def play_game():
    print("Welcome to Tic Tac Toe!")

    board = create_board()
    setup = choose_start_player()
    current_player = setup['current_player']
    player_mark = setup['player_mark']
    bot_mark = setup['bot_mark']

    move_count = 0

    while True:
        display_board(board)
        if current_player == 'Player 1':
            current_mark = player_mark
            print("Your turn.")
            row, col = get_player_move(board)
        else:
            current_mark = bot_mark
            print("Bot is making a move...")
            row, col = get_bot_move(board)

        place_mark(board, row, col, current_mark)
        move_count += 1

        if check_winner(board, current_mark):
            display_board(board)
            if current_player == 'Player 1':
                print("Congratulations! You win!")
            else:
                print("Bot wins!")
            break

        if full_board(board):
            display_board(board)
            print("It's a tie!")
            break

        current_player = 'Bot' if current_player == 'Player 1' else 'Player 1'

    print("Game Over.")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == 'y':
        play_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_game()