import unittest
from solver import SudokuGame

class TestSolver(unittest.TestCase):

    def testMakeSudokuString2d(self):
        num_string = "012345678012345678012345678012345678012345678012345678012345678012345678012345678"
        game = SudokuGame(num_string)
        board = game.makeSudokuString2d(num_string)
        self.assertEqual(board[8], [0,1,2,3,4,5,6,7,8])
        #print(game.input_grid)

    def testMoveForward(self):
        game = SudokuGame('')
        game.solution_grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        position = game.moveForward((0,0))
        self.assertEqual(position, (0,2))
        position = game.moveForward((3,8))
        self.assertEqual(position, (4,1))
        position = game.moveForward((7,3))
        self.assertEqual(position, (7,6))
        position = game.moveForward((2,7))
        self.assertEqual(position, (2,8))

    def testMoveBackward(self):
        game = SudokuGame('')
        game.input_grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        position = game.moveBackward((0,0))
        self.assertEqual(position, None)
        position = game.moveBackward((1,5))
        self.assertEqual(position, (1,2))
        position = game.moveBackward((8,6))
        self.assertEqual(position, (8,5))
        position = game.moveBackward((0,8))
        self.assertEqual(position, (0,7))
        position = game.moveBackward((1,1))
        self.assertEqual(position, (0,8))


    def testIsValid(self):
        game = SudokuGame('')
        game.solution_grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        check = game.isValid((1,1), 7)
        self.assertEqual(check, True)

    def testSolveSudoku(self):
        game = SudokuGame('530070000600195000098000060800060003400803001700020006060000280000419005000080079')
        answer = game.solveSudoku()
        solution = '534678912672195348198342567859761423426853791713924856961537284287419635345286179'
        self.assertEqual(answer, solution)

if __name__ == '__main__':
    unittest.main()

