from random import randint
import re

class Board:
    def __init__(self):
        self.board = {"1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " ",}
    def board_layout(self):
        print (self.board["1"] + "|" + self.board["2"] + "|" + self.board["3"])
        print ("-----")
        print (self.board["4"] + "|" + self.board["5"] + "|" + self.board["6"])
        print ("-----")
        print (self.board["7"] + "|" + self.board["8"] + "|" + self.board["9"])
    def update_board(self, player_input, string_update):
        self.board[str(player_input)] = string_update
        self.board_layout()
    def reset_board(self):
        for i in self.board:
            self.board[i] = " "
    def everything_occupied(self): 
        for n in self.board:
            if self.board[n] != "X" and self.board[n] != "O":
                return False
        return True
    def position_occupied(self, input):
        self.tira = input
        if self.board[self.tira] == " ": 
            return True
        else:
            return False
    def random_turn(self):
        turn = randint(1, 9)
        while self.board[str(turn)] != " ":
            turn = randint(1, 9)
        return turn
    def board_checker(self, counter):
        self.c = counter
        if self.c <= 5:
            if self.board["1"] == self.board["2"] == self.board["3"] != " ":
                print("Game Over!")
                print("The " + str(self.board["1"]) + " has won.")
                return True
            elif self.board["4"] == self.board["5"] == self.board["6"] != " ":
                print("Game Over!")
                print("The " + str(self.board["4"]) + " has won.")
                return True
            elif self.board["7"] == self.board["8"] == self.board["9"] != " ":
                print("Game Over!")
                print("The " + str(self.board["7"]) + " has won.")
                return True
            elif self.board["1"] == self.board["4"] == self.board["7"] != " ":
                print("Game Over!")
                print("The " + str(self.board["1"]) + " has won.")
                return True
            elif self.board["2"] == self.board["5"] == self.board["8"] != " ":
                print("Game Over!")
                print("The " + str(self.board["2"]) + " has won.")
                return True
            elif self.board["3"] == self.board["6"] == self.board["9"] != " ":
                print("Game Over!")
                print("The " + str(self.board["3"]) + " has won.")
                return True
            elif self.board["1"] == self.board["5"] == self.board["9"] != " ":
                print("Game Over!")
                print("The " + str(self.board["1"]) + " has won.")
                return True
            elif self.board["3"] == self.board["5"] == self.board["7"] != " ":
                print("Game Over!")
                print("The " + str(self.board["3"]) + " has won.")
                return True
        return False