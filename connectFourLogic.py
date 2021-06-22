import numpy as np


# Definicja potrzebnych wymiarów
ROWS = 6
COLS = 7

# klasa z metodami logicznymi dotyczącymi gry
class connect_four:
    def __init__(self):
        self.board = np.zeros((ROWS, COLS))

    def put_coin(self,row_1, col_1, player):
        self.board[row_1][col_1] = player

    def full_col(self, col_1):
        return self.board[ROWS - 1][col_1] == 0

    def full_board(self):
        counter = 0
        for i in range(COLS):
            if not self.board[ROWS - 1][i] == 0:
                counter +=1
        if counter == 7:
            return True
        return False

    def free_row(self, col_1):
        for i in range(ROWS):
            if self.board[i][col_1] == 0:
                return i
# lambda wyrażenie
    g = lambda self: print(np.flip(self.board,0))

    def ktoWygral(self, player):
        # Warunek sprawdzający czy są 4 monety w rzędzie poziomo
        for column in range(COLS - 3):
            for row in range(ROWS):
                if self.board[row][column] == player and self.board[row][column + 1] == player and self.board[row][column + 2] == player and self.board[row][column + 3] == player:
                    return True

        # Warunek sprawdzający czy są 4 monety w rzędzie pionowo
        for column in range(COLS):
            for row in range(ROWS - 3):
                if self.board[row][column] == player and self.board[row + 1][column] == player and self.board[row + 2][column] == player and self.board[row + 3][column] == player:
                    return True

        # Warunek sprawdzający czy są 4 monety w rzędzie na skos
        for column in range(COLS - 3):
            for row in range(ROWS - 3):
                if self.board[row][column] == player and self.board[row + 1][column + 1] == player and self.board[row + 2][column + 2] == player and self.board[row + 3][column + 3] == player:
                    return True
        for column in range(COLS - 3):
            for row in range(3, ROWS):
                if self.board[row][column] == player and self.board[row - 1][column + 1] == player and self.board[row - 2][column + 2] == player and self.board[row - 3][column + 3] == player:
                    return True
