from board import Board
from input_and_converter import input_validator, Converter

def Play_Human():
    Player_1_String = "X"
    Player_2_String = "O"
    brd = Board()
    XorO = input("Player 1, pick your poison (type X or O)\n")
    if str(XorO.lower()) == "o":
        Player_1_String = "O"
        Player_2_String = "X"
    print("Player 1 will go first.")
    brd.reset_board()
    for turn in range(5):
        print("Turn:" , turn + 1)
        brd.board_layout()
        Player1 = input("Type top-, mid-, or low-, + L, M, R\n")
        while not input_validator(Player1):
            Player1 = input("You typed the wrong input!\n")
        Human_Turn1 = Converter(Player1)
        print(Human_Turn1)
        while not brd.position_occupied(Human_Turn1):
            Player1 = input('The spot is already taken!\nType top-, mid-, or low-, + L, M, R\n')
        brd.update_board(Human_Turn1, Player_1_String)
        if brd.board_checker(turn):
            break
        if brd.everything_occupied():
            print("Looks like everything is occupied, It's a tie!\nGame Over")
            break
        print("It's Player 2's turn.")
        Player2 = input("Type top-, mid-, or low-, + L, M, R\n")
        while input_validator(Player2) == False:
            Player2 = input("You typed the wrong input!\n")
        Human_Turn2 = Converter(Player2)
        print(Human_Turn2)
        while not brd.position_occupied(Human_Turn2):
            Player2 = input("The spot is already taken!\nType top-, mid-, or low-, + L, M, R\n")
        brd.update_board(Human_Turn2, Player_2_String)
        if brd.board_checker(turn):
            break
        if brd.everything_occupied():
            print("Looks like everything is occupied, It's a tie!\nGame Over")
            break
        print("It's Player 1's turn.")