from copy import deepcopy
from itertools import chain

class SudokuGame:
    def __init__(self, num_string):
        self.num_string = num_string
        self.input_grid = self.makeSudokuString2d(num_string)
        self.solution_grid = deepcopy(self.input_grid)

    def makeSudokuString2d(self, num_string):
        str_board = [list(num_string[i:i+9]) for i in range(0, len(num_string), 9)]
        int_board = [list(map(int, x)) for x in str_board]
        return int_board

    def makeSudokuArray1d(self, num_array):
        singleDimensionArray = list(chain.from_iterable(num_array))
        singleDimensionArray = list(map(str,singleDimensionArray))
        numString = ''.join(singleDimensionArray)
        return numString

    def moveForward(self, position):
        row, col = position
        while (row < 9):
            while (col < 9):
                if self.solution_grid[row][col] == 0:
                    return (row, col)
                elif (row == 8 and col == 8):
                    return None
                col = col + 1
            col = 0
            row = row + 1

    def moveBackward(self, position):
        row, col = position
        while (row != 0 or col != 0):
            if col == 0:
                row -= 1
                col = 8
            else:
                col -= 1
            if self.input_grid[row][col] == 0:
                return (row, col)
        return None

    def isValid(self, position, number):
        row, col = position
        rowCheck = all([number != self.solution_grid[row][x] for x in range(9)])
        if not rowCheck:
            return False
        colCheck = all([number != self.solution_grid[x][col] for x in range(9)])
        if not colCheck:
            return False
        secTopRow, secTopCol = 3 * (row // 3), 3 * (col // 3)
        for y in range(secTopRow, secTopRow + 3):
          for x in range(secTopCol, secTopCol + 3):
              if self.solution_grid[y][x] == number:
                  return False
        return True

    def solveSudoku(self):
        position = self.moveForward((0, 0))
        while (position != None):
            row, col = position
            found = False
            for number in range(self.solution_grid[row][col] + 1, 10):
                if self.isValid(position, number):
                    self.solution_grid[row][col] = number
                    found = True
                    position = self.moveForward(position)
                    break
            if found == False:
                    self.solution_grid[row][col] = 0
                    position = self.moveBackward(position)
        finalAnswer = self.makeSudokuArray1d(self.solution_grid)
        return finalAnswer
