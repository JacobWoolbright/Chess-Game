from colors import Black

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