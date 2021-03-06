from player import Player
from computer import Computer
import random

class Morpion:
    def __init__(self, human=True):
        """
        initialize attributes
        """

        print("Le jeu du morpion")

        # initialize attributs
        self.board = list(range(1,10))
        self.available_squares = list(range(1,10))

        # set players
        player1 = Player("O")
        player1.args = { "available_squares" : self.available_squares }

        if not human:
            player2 = Computer("X")
            player2.args = { "board" : self.board, "opponent_token" : player1.token }
        else :
            player2 = Player("X")
            player2.args = { "available_squares" : self.available_squares }
        
        self.players = [player1, player2]

        self.winning_combi = [
            [0, 1, 2],
            [0, 4, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [2, 4, 6],
            [3, 4, 5],
            [6, 7, 8]
        ] # il y a 8 combinaisaons gagnates - on récupère leurs index

        self.current_player = self.players[random.randint(0,1)]
        self.mode = human
        self.gameon = True

    def start_game(self):
        """
        launch the game with the current state of the board and the current player
        """

        while self.gameon:
            self.change_player()
            self.print_board()
            choice = self.current_player.choose_square(self.current_player.args)
            self.print_choice(choice)
            self.check_winner()

    def print_board(self):
        """
        print the current state of the board
        """
        print('\n')

        for key, i in enumerate(self.board):
            if (key + 1) % 3 == 0:
                print(i)
            else :
                print(i, end =" ")
        print('-----------------')

    def print_choice(self, square):
        """
        print current player choice in the designated square
        """
        self.available_squares.remove(square) 

        square = square - 1 # we have to remove 1 for indexation purposes
        self.board[square] = self.current_player.token # place pawn

    def check_winning_combinations(self):
        """
        check among the winning combinations if the current player has one of them
        """
        
        for square1, square2, square3 in self.winning_combi:
            if self.current_player.token == self.board[square1] == self.board[square2] == self.board[square3]:
                return True
        return False

    def change_player(self):
        # change player for next round
        index = (self.players.index(self.current_player) + 1) % 2
        self.current_player = self.players[index]

    def check_winner(self):
        """
        check if there is a winner, otherwise resume the game
        """

        if self.board.count(self.current_player.token) >= 3: # if less than 3 pawns on the board, no use to compute check if the player wins
            if self.check_winning_combinations() : # the current player wins
                self.print_board()
                print("=================\n")
                print(f"{self.current_player.token} a gagné\n")
                print("End of the game")
                self.gameon = False
            else :
                if not self.available_squares: # game finished because all squares are filled
                    self.print_board()
                    print("il n'y a pas de gagant\n")
                    print("End of the game")
                    self.gameon = False