from colors import White, Black

letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
numbers = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}


class Pawn:
    def __init__(self, color, position):
        self.color = color
        self.worth = 1
        self.hasMoved = False
        self.validMoves = None
        self.validCaptures = None
        self.position = position

    def __str__(self):
        return 'P'

    def generateValidMoves(self, board):
        moves = []


        self.validMoves = moves

    def generateValidCaptures(self, board):
        captures = []
        columnNumber = letters[self.position[0]]
        rowNumber = self.position[1]
        if type(self.color) is Black:
            if str(numbers[columnNumber - 1]) in letters and board.positions[str(numbers[columnNumber - 1]) + str(int(rowNumber) - 1)] is not None and type(board.positions[str(numbers[columnNumber - 1]) + str(int(rowNumber) - 1)].color) is not type(self.color):
                captures.append(self.position[0] + 'x' + str(numbers[columnNumber - 1]) + str(int(rowNumber) - 1))
            if columnNumber + 1 in numbers and board.positions[str(numbers[columnNumber + 1]) + str(int(rowNumber) - 1)] is not None and type(board.positions[str(numbers[columnNumber + 1]) + str(int(rowNumber) - 1)].color) is not self.color:
                captures.append(self.position[0] + 'x' + str(numbers[columnNumber + 1]) + str(int(rowNumber) - 1))
        else:
            if str(numbers[columnNumber - 1]) in letters and board.positions[str(numbers[columnNumber - 1]) + str(int(rowNumber) + 1)] is not None and type(board.positions[str(numbers[columnNumber - 1]) + str(int(rowNumber)+ 1)].color) is not type(self.color):
                captures.append(self.position[0] + 'x' + str(numbers[columnNumber - 1]) + str(int(rowNumber) + 1))
            if columnNumber + 1 in numbers and board.positions[str(numbers[columnNumber + 1]) + str(int(rowNumber) + 1)] is not None and type(board.positions[str(numbers[columnNumber + 1]) + str(int(rowNumber) + 1)].color) is not self.color:
                captures.append(self.position[0] + 'x' + str(numbers[columnNumber + 1]) + str(int(rowNumber) + 1))
        self.validCaptures = captures
        return captures



class Rook:
    def __init__(self, color, position):
        self.color = color
        self.worth = 5
        self.position = position

    def __str__(self):
        return 'R'

    def generateValidMoves(self, board):
        moves = []

        #up
        for i in range(8 - int(self.position[-1])):
            i += 1
            piece = board.positions[self.position[-2] + str(int(self.position[-1]) + i)]
            if piece is None:
                print('valid move')
                moves.append('r' + self.position[-2] + str(int(self.position[-1]) + i))
            else:
                break

        #down
        for i in range(int(self.position[-1]) - 1):
            i += 1
            piece = board.positions[self.position[-2] + str(int(self.position[-1]) - i)]
            if piece is None:
                print('valid move')
                moves.append('r' + self.position[-2] + str(int(self.position[-1]) - i))
            else:
                break

        numericalletter = letters[self.position[-2]]

        #right
        for i in range(8 - numericalletter):
            i += 1
            piece = board.positions[numbers[i + numericalletter] + self.position[-1]]
            if piece is None:
                moves.append('r' + numbers[i + numericalletter] + self.position[-1])
            else:
                break

        #left
        for i in range(numericalletter - 1):
            i += 1
            piece = board.positions[numbers[numericalletter - i] + self.position[-1]]
            if piece is None:
                moves.append('r' + numbers[numericalletter - i] + self.position[-1])
            else:
                break


        return moves

    def generateValidCaptures(self, board):
        captures = []

        #up
        for i in range(8 - int(self.position[-1])):
            i += 1
            piece = board.positions[self.position[-2] + str(int(self.position[-1]) + i)]
            if piece is not None:
                captures.append(piece)
                break
        # down
        for i in range(int(self.position[-1]) - 1):
            i += 1
            piece = board.positions[self.position[-2] + str(int(self.position[-1]) - i)]
            if piece is not None:
                captures.append('rx' + piece.position)
                break

        numericalletter = letters[self.position[-2]]

        # right
        for i in range(8 - numericalletter):
            i += 1
            piece = board.positions[numbers[i + numericalletter] + self.position[-1]]
            if piece is not None:
                captures.append('rx' + piece.position)
                break

        # left
        for i in range(numericalletter - 1):
            i += 1
            piece = board.positions[numbers[numericalletter - i] + self.position[-1]]
            if piece is not None:
                captures.append('rx' + piece.position)
                break

        return captures


class Knight:
    def __init__(self, color, position):
        self.color = color
        self.worth = 3
        self.position = position

    def __str__(self):
        return 'N'

    def generateValidMoves(self, board):
        pass

    def generateValidCaptures(self, board):
        moves = []

        return moves


class Bishop:
    def __init__(self, color, position):
        self.color = color
        self.worth = 3.25
        self.position = position

    def __str__(self):
        return 'B'

    def generateValidMoves(self, board):
        pass

    def generateValidCaptures(self, board):
        moves = []

        return moves


class Queen:
    def __init__(self, color, position):
        self.color = color
        self.worth = 9
        self.position = position

    def __str__(self):
        return 'Q'

    def generateValidMoves(self, board):
        pass

    def generateValidCaptures(self, board):
        moves = []

        return moves


class King:
    def __init__(self, color, position):
        self.color = color
        self.worth = 60
        self.position = position

    def __str__(self):
        return 'K'

    def generateValidMoves(self, board):
        pass

    def generateValidCaptures(self, board):
        moves = []

        return moves
