from pieces import Pawn, Rook
from colors import Black, White

def move(board, string):

    #pawn move
    if len(string) == 2:
        letter = string[0]
        number = string[1]

        if int(number) > 8:
            print('Invalid move!')
            return False
        if letter not in 'abcdefgh':
            print('Invalid move!')
            return False

        if board.positions[string] is not None:
            print('Invalid move!')
            return False
        if board.moves % 2 == 0:
            if type(board.positions[letter + str(int(number) + 1)]) == Pawn and type(board.positions[letter + str(int(number) + 1)].color) == Black:
                board.positions[string] = board.positions[letter + str(int(number) + 1)]
                board.positions[string].hasMoved = True
                board.positions[string].position = string
                board.positions[letter + str(int(number) + 1)] = None
            elif type(board.positions[letter + str(int(number) + 2)]) == Pawn and not board.positions[letter + str(int(number) + 2)].hasMoved and type(board.positions[letter + str(int(number) + 2)].color) == Black:
                board.positions[string] = board.positions[letter + str(int(number) + 2)]
                board.positions[string].hasMoved = True
                board.positions[string].position = string
                board.positions[letter + str(int(number) + 2)] = None
            else:
                print('Invalid move!')
                return False
        else:
            if type(board.positions[letter + str(int(number) - 1)]) == Pawn and type(board.positions[letter + str(int(number) - 1)].color) == White:
                board.positions[string] = board.positions[letter + str(int(number) - 1)]
                board.positions[string].hasMoved = True
                board.positions[string].position = string
                board.positions[letter + str(int(number) - 1)] = None
            elif type(board.positions[letter + str(int(number) - 2)]) == Pawn and not board.positions[letter + str(int(number) - 2)].hasMoved and type(board.positions[letter + str(int(number) - 2)].color) == White:
                board.positions[string] = board.positions[letter + str(int(number) - 2)]
                board.positions[string].hasMoved = True
                board.positions[string].position = string
                board.positions[letter + str(int(number) - 2)] = None
            else:
                print('Invalid move!')
                return False
    #pawn capture
    elif 'x' in string and len(string) == 3:
        allCaptures = []
        attackerColumn = string[0]
        for i in range(8):
            i += 1
            position = board.positions[attackerColumn + str(i)]
            if position is not None:
                allCaptures.append(position.generateValidCaptures(board))
        allMoves = []
        for item in allCaptures:
            for move in item:
                if move not in allMoves:
                    allMoves.append(move)
                else:
                    print('Invalid move!')
                    return False
        for i, item in enumerate(allCaptures):
            for move in item:
                if move == string:
                    pieces = []
                    for t in range(8):
                        thing = board.positions[attackerColumn + str(t+1)]
                        if thing is not None:
                            pieces.append(thing)
                    piece = pieces[i]
        if type(piece) is Pawn:
            piece.hasMoved = True
        board.positions[string[2:]] = piece
        board.positions[piece.position] = None
        board.positions[string[2:]].position = string[2:]
    #other captures
    elif 'x' in string:
        allCaptures = []
    #other piece moves
    else:
        if board.moves % 2 == 0:
            currentColor = Black
        else:
            currentColor = White
        typeOfPiece = string[0]
        if typeOfPiece.lower() == 'r':
            #rook move
            rooks = []
            for i in range(8):
                i += 1
                check = board.positions[string[-2] + str(i)]
                if type(check) == Rook and type(check.color) == currentColor:
                    rooks.append(check)
            for i in 'abcdefgh':
                check = board.positions[i + string[-1]]
                if type(check) == Rook and type(check.color) == currentColor:
                    rooks.append(check)
            moves = []
            for rook in rooks:
                moves.append(rook.generateValidMoves(board))
            allMoves = []
            for item in moves:
                for move in item:
                    if move not in allMoves:
                        allMoves.append(move)
                    else:
                        print('Invalid move!')
                        return False
            for i, item in enumerate(moves):
                if string in item:
                    rook = rooks[i]
                    break
            board.positions[string[1:]] = rook
            board.positions[rook.position] = None
            board.positions[string[1:]].position = string[1:]
            return board



        else:
            return False


    return board
