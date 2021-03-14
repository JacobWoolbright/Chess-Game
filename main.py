from chessBoard import Board
from boards import defaultBoard
from move import move

board = defaultBoard()

while True:
    print(board)
    if board.moves % 2 == 0:
        movee = input('Black> ')
    else:
        movee = input('White> ')
    newBoard = move(board, movee)
    if newBoard is not False:
        board = newBoard
        board.moves += 1