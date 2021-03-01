from random import randint
from board import Board
from input_and_converter import input_validator, Converter
from Play_Human import Play_Human
from Play_Computer import Play_Computer


if __name__ == '__main__':
    Play_Again = "yes"
    while str(Play_Again.lower()) == "yes" or str(Play_Again.lower()) != "y":
        print("Tic Tac Toe!")
        CompOrHuman = input("Do you want to play with a computer or with a Human? (Type Computer/Human)\n")
        while str(CompOrHuman.lower()) != "computer" and str(CompOrHuman.lower()) != "human":
            CompOrHuman = input("You typed the wrong input.\n")
        if str(CompOrHuman.lower()) == "human":
            Play_Human()
        else:
            Play_Computer()
        print("Do you want to play again? (Type Yes/No)")
        Play_Again = input()
        while str(Play_Again.lower()) != "yes" and str(Play_Again.lower()) != "no" and str(Play_Again.lower()) != "y" and str(Play_Again.lower()) != "n":
            print("Not a valid input. Do you want to play again? (Type Yes/No)")
            Play_Again = input()
        if str(Play_Again.lower()) == "no" or str(Play_Again.lower()) == "n":
            break
