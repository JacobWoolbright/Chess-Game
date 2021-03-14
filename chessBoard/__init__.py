class Board:
    def __init__(self):
        self.positions = {}
        for i in range(8):
            i += 1
            for letter in 'abcdefgh':
                self.positions[letter + str(i)] = None
        self.moves = 1


    def __str__(self):
        lines = []
        for i in range(8):
            i = 8-(i)
            line = ''
            for letter in 'abcdefgh':
                if self.positions[letter + str(i)] is None:
                    line += '   '
                else:
                    piece = self.positions[letter + str(i)]
                    line += str(piece.color) + str(piece) + ' '
            lines.append(line)
        return '\n'.join(lines)