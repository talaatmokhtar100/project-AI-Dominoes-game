import random
import copy
import numpy as np

class DominoesGame:
    def __init__(self, board):
        self.board = board
        self.current_player = 1
        self.game_over = False
        self.winner = None

    def get_board(self):
        return self.board.copy()

    def get_current_player(self):
        return self.current_player

    def get_winner(self):
        return self.winner

    def is_game_over(self):
        return self.game_over

    def set_board(self, board):
        self.board = board

    def set_current_player(self, player):
        self.current_player = player

    def set_winner(self, winner):
        self.winner = winner

    def play(self, row, col):
        if self.board[row][col] != False:
            return False

        self.board[row][col] = self.current_player

        if self.check_game_over():
            self.game_over = True
            self.winner = self.current_player

        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

        return True

    def check_game_over(self):
        # Check rows
        for row in self.board:
            if False in row:
                continue
            if len(set(row)) == 1:
                return True

        # Check columns
        for col in range(len(self.board[0])):
            column = [self.board[row][col] for row in range(len(self.board))]
            if False in column:
                continue
            if len(set(column)) == 1:
                return True

        # Check diagonals
        diagonals = [np.diag(self.board), np.diag(np.fliplr(self.board))]
        for diagonal in diagonals:
            if False in diagonal:
                continue
            if len(set(diagonal)) == 1:
                return True

        return False


def create_dominoes_game(rows, cols):
    row = [False] * cols
    board = [row[:] for _ in range(rows)]
    return DominoesGame(board)
