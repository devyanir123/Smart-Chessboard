from stockfish import Stockfish

# Initialializing stockfish engine here
stockfish_path = r"D:\\stockfish\\stockfish-windows-x86-64-avx2.exe"
stockfish = Stockfish(path=stockfish_path)

# Store moves
moves = []

while True:
    print("Current Moves: " + str(moves))

    opponent_move = input("Enter Opponent's move: ")

    if opponent_move.lower() == "quit":
        break
    
    moves.append(opponent_move)

    # Update the engine
    stockfish.set_position(moves)
    best_move = stockfish.get_best_move()

    if best_move == None:
        print("Game Over")
        break
    
    print("Best Move: +" + str(best_move))

    moves.append(best_move)