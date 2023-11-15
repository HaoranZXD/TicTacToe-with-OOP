# main.py

from player import HumanPlayer, BotPlayer
from game import TicTacToeGame

if __name__ == '__main__':
    player1 = HumanPlayer('X')
    choice = input("Play against another player (2) or bot (1)? ")
    player2 = BotPlayer('O') if choice == '1' else HumanPlayer('O')

    game = TicTacToeGame(player1, player2)
    game.play_game()
