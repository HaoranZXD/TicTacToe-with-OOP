import random

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, board):
        raise NotImplementedError

class HumanPlayer(Player):
    def make_move(self, board):
        while True:
            try:
                move = input(f"{self.symbol}, enter your move (row, column): ")
                row, col = move.split(",")
                row, col = int(row.strip()), int(col.strip())
                if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] is not None:
                    print("Invalid move. Try again.")
                    continue
                return row, col
            except ValueError:
                print("Please enter numbers only. Try again.")


class BotPlayer(Player):
    def make_move(self, board):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] is None]
        return random.choice(empty_cells) if empty_cells else None
