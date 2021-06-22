import random
import connectFourLogic as logic
import unittest


class unitests(unittest.TestCase):

    def testInsertCoin(self):
        player_1 = 1
        player_2 = 2
        game = logic.connect_four()
        for i in range(2):
            game.put_coin(i, player_1)
            game.put_coin(i, player_2)
        result = (game.board[0][0] == 1
                    and game.board[0][1] == 1
                    and game.board[1][0] == 2
                    and game.board[1][1] == 2)
        self.assertTrue(result)

    def testWinPionowo(self):
        player = 1
        column = random.randint(0, 6)
        game = logic.connect_four()
        for i in range(4):
            game.put_coin(column, player)
        result = game.ktoWygral(player)
        self.assertTrue(result)

    def testWinPoziomo(self):
        player = 2
        game = logic.connect_four()
        for i in range(4):
            game.put_coin(i, player)
        result = game.ktoWygral(player)
        self.assertTrue(result)

    def testWinSkos(self):
        player_1 = 1
        player_2 = 2
        game = logic.connect_four()
        for i in range(1, 4):
            for j in range(i, 4):
                game.put_coin(j, player_1)
        for i in range(4):
            game.putcoin(i, player_2)
            
            # [[0. 0. 0. 0. 0. 0. 0.]
            #  [0. 0. 0. 0. 0. 0. 0.]
            #  [0. 0. 0. 2. 0. 0. 0.]
            #  [0. 0. 2. 1. 0. 0. 0.]
            #  [0. 2. 1. 1. 0. 0. 0.]
            #  [2. 1. 1. 1. 0. 0. 0.]]

        result = game.ktoWygral(player_2)
        self.assertTrue(result)

    def testFullBoard(self):
        game = logic.connect_four()
        player_1 = 1
        player_2 = 2
        for i in [0, 2, 4]:
            for j in range(3):
                game.put_coin(i, player_1)
            for k in range(3):
                game.put_coin(i, player_2)

        for i in [1, 3, 5]:
            for j in range(3):
                game.put_coin(i, player_2)
            for k in range(3):
                game.put_coin(i, player_1)

        for i in range(3):
            game.put_coin(6, player_1)
            game.put_coin(6, player_2)

        #  [[2, 1, 2, 1, 2, 1, 1],
        #   [2, 1, 2, 1, 2, 1, 2],
        #   [2, 1, 2, 1, 2, 1, 1],
        #   [1, 2, 1, 2, 1, 2, 2],
        #   [1, 2, 1, 2, 1, 2, 1],
        #   [1, 2, 1, 2, 1, 2, 2]]

        result = game.full_board()
        self.assertTrue(result)

    def testMoreThanFourInARow(self):
        player_1 = 1
        player_2 = 2
        game = logic.connect_four()
        for i in range(3):
            game.put_coin(i, player_2)
            game.put_coin(i, player_1)

        for i in range(4,7):
            game.put_coin(i, player_2)
            game.put_coin(i, player_1)

        game.put_coin(3, player_2)
        game.show_board()
        result = game.ktoWygral(player_2)
        self.assertTrue(result)

    def testFullColumn(self):
        player = random.randint(1, 2)
        column = random.randint(0, 6)
        game = logic.connect_four()
        for i in range(6):
            game.put_coin(column, player)

        result = game.put_coin(column, player)

        self.assertFalse(result)