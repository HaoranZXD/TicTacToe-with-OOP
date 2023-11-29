import csv
import os
from datetime import datetime

from player import BotPlayer

class TicTacToeGame:
    def __init__(self, player1, player2):
        self.board = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]
        self.players = [player1, player2]
        self.current_player = 0
        self.move_count = {'X': 0, 'O': 0}  # Track moves for each player

    def print_board(self):
        for row in self.board:
            print(' | '.join([str(cell) if cell else ' ' for cell in row]))
        print()

    def get_winner(self):
    # check rows
        for row in self.board:
            if row[0] is not None and len(set(row)) == 1:
                return row[0]

        # check columns
        for i in range(len(self.board)):
            column = [self.board[j][i] for j in range(len(self.board))]
            if len(set(column)) == 1 and self.board[0][i] is not None:
                return self.board[0][i]

        # check diagonals
        top_left_to_bottom_right = [self.board[i][i] for i in range(len(self.board))]
        if len(set(top_left_to_bottom_right)) == 1 and self.board[0][0] is not None:
            return self.board[0][0]

        top_right_to_bottom_left = [self.board[i][len(self.board)-i-1] for i in range(len(self.board))]
        if len(set(top_right_to_bottom_left)) == 1 and self.board[0][len(self.board)-1] is not None:
            return self.board[0][len(self.board)-1]
        
        
        flat_board = []
        for row in self.board:
            flat_board.extend(row)

        if not None in flat_board:
            return "Draw"
            
        return None



    def play_game(self):
        winner = None

        while winner is None:
            self.print_board()
            row, col = self.players[self.current_player].make_move(self.board)
            self.board[row][col] = self.players[self.current_player].symbol
            self.move_count[self.players[self.current_player].symbol] += 1
            winner = self.get_winner()

            if winner == 'Draw' and all(all(cell is not None for cell in row) for row in self.board):
                print("It's a draw!")
                self.log_game_result('Draw')
                self.print_board()
                return

            self.current_player = 1 - self.current_player

        print(f'Player {winner} wins!')
        self.log_game_result(winner)
        self.print_board()

    def log_game_result(self, winner):
        log_folder = 'log'
        log_file = os.path.join(log_folder, 'game_logs.csv')
        log_exists = os.path.exists(log_file)
        player_o_type = 'Bot' if isinstance(self.players[1], BotPlayer) else 'Human'
        if not log_exists:
            print('Creating new log file')
            with open(log_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Timestamp', 'Winner', 'Player X Moves', 'Player O Moves', 'Player O Type'])
        with open(log_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now(), winner, self.move_count['X'], self.move_count['O'], player_o_type])
