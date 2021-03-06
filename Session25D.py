"""

    n-Queen Problem :)
    1. Create a Chess Board
        take input form user (2*2, 4*4, 8*8....)
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1

    2. Take input from User to place n-queens

    1 0 1 9 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 9 1 0 1 0
    0 1 0 1 0 1 0 1

      > No second Queen



"""

class QueenChessBoard:
    def __init__(self, size):
        # board has dimensions size x size
        self.size = size

        self.columns = []

    def place_in_next_row(self, column):
        self.columns.append(column)

    def remove_in_current_row(self):
        return self.columns.pop()

    def is_this_column_safe_in_next_row(self, column):
        # index of next row
        row = len(self.columns)

        # check column
        for queen_column in self.columns:
            if column == queen_column:
                return False

        # check diagonal
        for queen_row, queen_column in enumerate(self.columns):
            if queen_column - queen_row == column - row:
                return False

        # check other diagonal
        for queen_row, queen_column in enumerate(self.columns):
            if ((self.size - queen_column) - queen_row
                    == (self.size - column) - row):
                return False

        return True

    def display(self):
        for row in range(self.size):
            for column in range(self.size):
                if column == self.columns[row]:
                    print('Q', end=' ')
                else:
                    print('.', end=' ')
            print()


def solve_queen(size):

    board = QueenChessBoard(size)
    number_of_solutions = 0

    row = 0
    column = 0
    # iterate over rows of board
    while True:
        # place queen in next row
        while column < size:
            if board.is_this_column_safe_in_next_row(column):
                board.place_in_next_row(column)
                row += 1
                column = 0
                break
            else:
                column += 1


        if (column == size or row == size):

            if row == size:
                board.display()
                print()
                number_of_solutions += 1

                board.remove_in_current_row()
                row -= 1

            # now backtrack
            try:
                prev_column = board.remove_in_current_row()
            except IndexError:

                break
            # try previous row again
            row -= 1

            column = 1 + prev_column

    print('Number of solutions:', number_of_solutions)


n = int(input('Enter n: '))
solve_queen(n)
