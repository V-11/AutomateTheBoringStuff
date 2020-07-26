def isValidChessBoard(board):
    x_axis = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    y_axis = (1, 2, 3, 4, 5, 6, 7, 8)
    pieces_counter = {'w': 0, 'b': 0}
    pawns_counter = {'w': 0, 'b': 0}
    kings_counter = {'w': 0, 'b': 0}
    colors = ('w','b')
    pieces = ('pawn','knight','bishop','rook','queen','king')

    for position, piece in board.items():
        if int(position[0]) not in y_axis:
            print('Exceeded y_axis limit!!')
            exit()

        if str(position[1]) not in x_axis:
            print('Exceeded x_axis limit!!')
            exit()

        if piece != '':
            if piece[0] not in colors:
                print('This is not a piece color!!')
                exit()
            
            current_color = piece[0]
            pieces_counter[current_color] += 1
            
            if pieces_counter[current_color] > 16:
                print('Exceeded number of pieces!!')
                exit()
            
            current_piece = piece[1:]
            if current_piece not in pieces:
                print('There is a wrong chess piece!!')
                exit()

            if current_piece == 'pawn':
                pawns_counter[current_color] += 1
                if pawns_counter[current_color] > 8:
                    print('Exceeded number of pawns!!')
                    exit()

            if current_piece == 'king':
                kings_counter[current_color] += 1
                if kings_counter[current_color] > 1:
                    print('Exceeded number of kings!!')
                    exit()

    if list(kings_counter.values()) != [1, 1]:
        return ('You can not play without kings!!')
    else:
        return('Nice board, Have a good game :D')

board = {'1a': 'bking','2a': 'bqueen','3a': 'brook','4a': 'brook',
'5a': 'bknight','6a': 'bknight','7a':'bbishop','8a': 'bbishop',
'1b': 'bpawn','2b': 'bpawn','3b': 'bpawn','4b':'bpawn',
'5b': 'bpawn','6b': 'bpawn','7b': 'bpawn','8b': 'bpawn',
'1c': 'wking','2c': 'wqueen','3c': 'wrook','4c': 'wrook',
'5c': 'wbishop','6c': 'wbishop','7c': 'wknight','8c':'wknight',
'1e': 'wpawn','2e': 'wpawn','3e': 'wpawn','4e': 'wpawn',
'5e': 'wpawn','6e': 'wpawn','7e': 'wpawn','8e': 'wpawn',
'1g': '','2g': '','3g': '','4g': '','5g': '','6g': '','7g': '','8g': '',
'1h': '','2h': '','3h': '','4h': '','5h': '','6h': '','7h': '','8h': ''}

print(isValidChessBoard(board))
