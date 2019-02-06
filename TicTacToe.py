import random

board_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def end_game():
    res = ""
    if (board_list[1] == board_list[2] == board_list[3] or board_list[4] == board_list[5] == board_list[6] or
        board_list[7] == board_list[8] == board_list[9] or board_list[1] == board_list[4] == board_list[7] or
        board_list[2] == board_list[5] == board_list[8] or board_list[3] == board_list[6] == board_list[9] or
        board_list[1] == board_list[5] == board_list[9] or board_list[3] == board_list[5] == board_list[7]):
        res = "Win"
    else:
        for ele in board_list[1:]:
            if ele != 'X' and ele != 'O':
                res = "Continue"
                break
            else:
                res = "Draw"
    return res


def enter_game():
    clear_screen()
    print("Welcome to TicTacToe Game")
    player1_name = input("Enter nick name for player1:")
    player2_name = input("Enter nick name for player2:")
    toss = random.randint(0, 1)
    toss_won = player1_name if toss == 0 else player2_name
    toss_loss = player1_name if toss_won == player2_name else player2_name
    print(" {} won the toss".format(toss_won))
    marker1 = ''
    while marker1 != 'X' and marker1 != 'O':
        marker1 = input("Hello {}.. Choose marker: X or O : ".format(toss_won))
    marker2 = "X" if marker1 == "O" else "O"
    print("{} has marker:{} \n{} has marker:{} ".format(toss_won, marker1, toss_loss, marker2))
    return ((toss_won,marker1), (toss_loss,marker2))


def clear_screen():
    print("\n"*25)


def choose_grid(player):
    player_name, marker = player
    player_input = int(input("Hello {}, Pick an available number for {} marker :".format(player_name,marker)))
    board_list[player_input] = marker


def display_board(board):
    clear_screen()
    print("Welcome to TicTacToe Game")
    print("-" * 35)
    print("{s}{s}{s}{w}{s}{s}{s}{w}{s}{s}{s}".format(s='\t', w='|'))
    print("{s}{b7}{s}{s}{w}{s}{b8}{s}{s}{w}{s}{b9}{s}{s}".format(s='\t', w='|', b7=board[7], b8=board[8], b9=board[9]))
    print("{s}{s}{s}{w}{s}{s}{s}{w}{s}{s}{s}".format(s='\t', w='|'))
    print("-"*35)
    print("{s}{s}{s}{w}{s}{s}{s}{w}{s}{s}{s}".format(s='\t', w='|'))
    print("{s}{b4}{s}{s}{w}{s}{b5}{s}{s}{w}{s}{b6}{s}{s}".format(s='\t', w='|', b4=board[4], b5=board[5], b6=board[6]))
    print("{s}{s}{s}{w}{s}{s}{s}{w}{s}{s}{s}".format(s='\t', w='|'))
    print("-" * 35)
    print("{s}{s}{s}{w}{s}{s}{s}{w}{s}{s}{s}".format(s='\t', w='|'))
    print("{s}{b1}{s}{s}{w}{s}{b2}{s}{s}{w}{s}{b3}{s}{s}".format(s='\t', w='|', b1=board[1], b2=board[2], b3=board[3]))
    print("{s}{s}{s}{w}{s}{s}{s}{w}{s}{s}{s}".format(s='\t', w='|'))
    print("-" * 35)
    print("\n" * 1)


if __name__ == "__main__":
        play = True
        while play:
            player_info = enter_game()
            display_board(board_list)
            turn = 0
            result = end_game()

            while result == "Continue":
                if turn == 0:
                    choose_grid(player_info[0])
                    turn = 1
                else:
                    choose_grid(player_info[1])
                    turn = 0
                display_board(board_list)
                result = end_game()
            if result == "Win":
                winner = player_info[1] if turn == 0 else player_info[0]
                print("Congratulations {}..!! You have won the game..!".format(winner[0]))
            else:
                print("It's a Tie game...")
            replay = ''
            while replay != 'Y' and replay != 'N':
                replay = input("Do you like to replay?? (Y/N) : ")
            play = True if replay == 'Y' else False

