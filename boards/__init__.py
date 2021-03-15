from chessBoard import Board
from pieces import Pawn, Rook, Knight, Bishop, King, Queen
from colors import Black, White


def defaultBoard():
    board = Board()

    for letter in 'abcdefgh':
        board.positions[letter + '2'] = Pawn(White(), letter + '2')

    for letter in 'abcdefgh':
        board.positions[letter + '7'] = Pawn(Black(), letter + '7')

    board.positions['a8'] = Rook(Black(), 'a8')
    board.positions['h8'] = Rook(Black(), 'h8')
    board.positions['b8'] = Knight(Black(), 'b8')
    board.positions['g8'] = Knight(Black(), 'g8')
    board.positions['c8'] = Bishop(Black(), 'c8')
    board.positions['f8'] = Bishop(Black(), 'f8')
    board.positions['d8'] = Queen(Black(), 'd8')
    board.positions['e8'] = King(Black(), 'e8')

    board.positions['a1'] = Rook(White(), 'a1')
    board.positions['h1'] = Rook(White(), 'h1')
    board.positions['b1'] = Knight(White(), 'b1')
    board.positions['g1'] = Knight(White(), 'g1')
    board.positions['c1'] = Bishop(White(), 'c1')
    board.positions['f1'] = Bishop(White(), 'f1')
    board.positions['d1'] = Queen(White(), 'd1')
    board.positions['e1'] = King(White(), 'e1')

    #testing branch
    board.positions['d4'] = Rook(White(), 'd4')

    return board
