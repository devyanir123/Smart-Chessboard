class ChessEngine:
    def __init__(self):
        self.board = self.initialize_board()  # Initialize an 8x8 grid to represent the chessboard
        self.black_squares, self.white_squares = self.identify_squares()
        self.pieces = self.define_pieces()

    def initialize_board(self):
        # Initialize an 8x8 grid to represent the chessboard
        return [["" for _ in range(8)] for _ in range(8)]

    def identify_squares(self):
        # Initialize variables to hold positions for all black and white squares
        black_squares = []
        white_squares = []
        
        # Loop through the chessboard to determine black and white squares
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    white_squares.append((i, j))  # White square
                else:
                    black_squares.append((i, j))  # Black square
        
        return black_squares, white_squares

    def define_pieces(self):
        # Define all the types and colors of pieces in the game
        # Each piece is represented as a string with its type and color
        pieces = []
        
        # Pawns
        for i in range(8):
            pieces.append({'type': 'pawn', 'color': 'white', 'id': f'wp{i+1}', 'position': (1, i)})  # White pawns
            pieces.append({'type': 'pawn', 'color': 'black', 'id': f'bp{i+1}', 'position': (6, i)})  # Black pawns
        
        # Rooks
        pieces.append({'type': 'rook', 'color': 'white', 'id': 'wr1', 'position': (0, 0)})
        pieces.append({'type': 'rook', 'color': 'white', 'id': 'wr2', 'position': (0, 7)})
        pieces.append({'type': 'rook', 'color': 'black', 'id': 'br1', 'position': (7, 0)})
        pieces.append({'type': 'rook', 'color': 'black', 'id': 'br2', 'position': (7, 7)})
        
        # Knights
        pieces.append({'type': 'knight', 'color': 'white', 'id': 'wn1', 'position': (0, 1)})
        pieces.append({'type': 'knight', 'color': 'white', 'id': 'wn2', 'position': (0, 6)})
        pieces.append({'type': 'knight', 'color': 'black', 'id': 'bn1', 'position': (7, 1)})
        pieces.append({'type': 'knight', 'color': 'black', 'id': 'bn2', 'position': (7, 6)})
        
        # Bishops
        pieces.append({'type': 'bishop', 'color': 'white', 'id': 'wb1', 'position': (0, 2)})
        pieces.append({'type': 'bishop', 'color': 'white', 'id': 'wb2', 'position': (0, 5)})
        pieces.append({'type': 'bishop', 'color': 'black', 'id': 'bb1', 'position': (7, 2)})
        pieces.append({'type': 'bishop', 'color': 'black', 'id': 'bb2', 'position': (7, 5)})
        
        # Queens
        pieces.append({'type': 'queen', 'color': 'white', 'id': 'wq', 'position': (0, 3)})  # White queen on a light square
        pieces.append({'type': 'queen', 'color': 'black', 'id': 'bq', 'position': (7, 3)})  # Black queen on a light square
        
        # Kings
        pieces.append({'type': 'king', 'color': 'white', 'id': 'wk', 'position': (0, 4)})  # White king on a light square
        pieces.append({'type': 'king', 'color': 'black', 'id': 'bk', 'position': (7, 4)})  # Black king on a light square
        
        return pieces

    def display_info(self):
        # Place pieces on the board
        for piece in self.pieces:
            self.board[piece['position'][0]][piece['position'][1]] = piece['id']
        
        print("\nUpdated Board:")
        print("  a b c d e f g h")
        for i, row in enumerate(self.board):
            print(8 - i, end=" ")  # Print row number (8 to 1)
            for cell in row:
                print(cell, end=" ")
            print()
        
        print("\nBlack Squares:", self.black_squares)
        print("White Squares:", self.white_squares)

    
    def coordinates_to_chess_notation(self, move):
        i, j = move
        file = chr(ord('a') + j)  # Convert column to file letter
        rank = i + 1  # Convert row to rank number
        return f"{file}{rank}"



    def chess_notation_to_coordinates(self, notation):
        file = notation[0]  # Get the file letter
        rank = int(notation[1])  # Get the rank number
        
        # Convert file letter to column index
        j = ord(file) - ord('a')
        
        # Convert rank number to row index
        i = 8 - rank
        
        return (i, j)


    def pawn_valid_moves_empty_board(self, id, position):
        valid_moves = []
        piece_id = list(id)
        
        if piece_id[0] == 'w':
            i, j = position
            if i == 1:
                valid_moves.append((i+1, j))  
                valid_moves.append((i+2, j))  
            else:
                valid_moves.append((i+1, j))  
        elif piece_id[0] == 'b':
            i, j = position
            if i == 6:
                valid_moves.append((i-1, j))  
                valid_moves.append((i-2, j))  
            else:
                valid_moves.append((i-1, j))  
        
        # print("Valid Moves in Chess Notation:")
        # for move in valid_moves:
        #     print(self.display_move_in_chess_notation(move))
        
        return valid_moves

    def rook_valid_moves_empty_board(self, id, position):
        valid_moves = []
        piece_id = list(id)
        
        i, j = position
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Right, Left, Down, Up
        
        for direction in directions:
            x, y = i + direction[0], j + direction[1]
            while 0 <= x < 8 and 0 <= y < 8:
                valid_moves.append((x, y))
                x += direction[0]
                y += direction[1]
        
        # print("Valid Moves in Chess Notation:")
        # for move in valid_moves:
        #     print(self.display_move_in_chess_notation(move))
        
        return valid_moves

    def bishop_valid_moves_empty_board(self, id, position):
        valid_moves = []
        piece_id = list(id)
        
        i, j = position
        
        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]  # Down-Right, Up-Left, Down-Left, Up-Right
        
        for direction in directions:
            x, y = i + direction[0], j + direction[1]
            while 0 <= x < 8 and 0 <= y < 8:
                valid_moves.append((x, y))
                x += direction[0]
                y += direction[1]
        
        # print("Valid Moves in Chess Notation:")
        # for move in valid_moves:
        #     print(self.display_move_in_chess_notation(move))
        
        return valid_moves

    def knight_valid_moves_empty_board(self, id, position):
        valid_moves = []
        piece_id = list(id)
        
        i, j = position
        
        moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        
        for move in moves:
            x, y = i + move[0], j + move[1]
            if 0 <= x < 8 and 0 <= y < 8:
                valid_moves.append((x, y))
        
        # print("Valid Moves in Chess Notation:")
        # for move in valid_moves:
        #     print(self.display_move_in_chess_notation(move))
        
        return valid_moves

    def king_valid_moves_empty_board(self, id, position):
        valid_moves = []
        piece_id = list(id)
        
        i, j = position
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        
        for direction in directions:
            x, y = i + direction[0], j + direction[1]
            if 0 <= x < 8 and 0 <= y < 8:
                valid_moves.append((x, y))
        
        # print("Valid Moves in Chess Notation:")
        # for move in valid_moves:
        #     print(self.display_move_in_chess_notation(move))
        
        return valid_moves

    def queen_valid_moves_empty_board(self, id, position):
        valid_moves = []
        piece_id = list(id)
        
        i, j = position
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        
        for direction in directions:
            x, y = i + direction[0], j + direction[1]
            while 0 <= x < 8 and 0 <= y < 8:
                valid_moves.append((x, y))
                x += direction[0]
                y += direction[1]
        
        # print("Valid Moves in Chess Notation:")
        # for move in valid_moves:
        #     print(self.display_move_in_chess_notation(move))
        
        return valid_moves

# Initialize the chess engine
engine = ChessEngine()
move = (5,2)
print(engine.coordinates_to_chess_notation(move))

