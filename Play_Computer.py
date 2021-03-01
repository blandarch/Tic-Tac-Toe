from board import Board
from input_and_converter import input_validator, Converter


def Play_Computer():
    CompString = "O"
    HumString = "X"
    brd = Board()
    XorO = input("Pick your poison (type X or O)\n")
    if str(XorO.lower()) == "o":
        HumString = "O"
        CompString = "X"
    print("The computer will go first.")
    brd.reset_board()
    for turn in range(5):
        print("Turn:", turn + 1) 
        CompTurn = brd.random_turn()
        brd.update_board(CompTurn, CompString)
        if brd.board_checker(turn):
            break
        if brd.everything_occupied():
            print("Looks like everything is occupied, It's a tie!\nGame Over")
            break
        turn_in = input("Your turn. (Type top-, mid-, or low-, + L, M, R)\n")
        while input_validator(turn_in) == False:
            turn_in = input("You typed the wrong input!\n")
        _turn = Converter(turn_in)
        print(_turn)
        while not brd.position_occupied(_turn):
            turn_in = input("The spot is already taken!\nType top-, mid-, or low-, + L, M, R\n")
            _turn = Converter(turn_in)   
        brd.update_board(_turn, HumString)
        if brd.board_checker(turn):
            break
        if brd.everything_occupied():
            print("Looks like everything is occupied, It's a tie!\nGame Over")
            break
        print("Computer's Turn")
