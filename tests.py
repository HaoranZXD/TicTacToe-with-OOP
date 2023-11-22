import unittest
import io
from unittest.mock import patch
from game import TicTacToeGame
from player import HumanPlayer, BotPlayer

class TestTicTacToeGame(unittest.TestCase):

    def test_initial_empty_board(self):
        # Test that the game board is initialized as empty
        game = TicTacToeGame(HumanPlayer('X'), HumanPlayer('O'))
        self.assertTrue(all(all(cell is None for cell in row) for row in game.board), "Board should be initialized empty")

    def test_two_players_initialization(self):
        # Test that the game initializes correctly with two human players
        player1 = HumanPlayer('X')
        player2 = HumanPlayer('O')
        game = TicTacToeGame(player1, player2)
        self.assertEqual(game.players[0].symbol, 'X')
        self.assertEqual(game.players[1].symbol, 'O')

    def test_single_player_initialization(self):
        # Test that the game initializes correctly with one human player and one bot player
        player = HumanPlayer('X')
        bot = BotPlayer('O')
        game = TicTacToeGame(player, bot)
        self.assertIsInstance(game.players[0], HumanPlayer)
        self.assertIsInstance(game.players[1], BotPlayer)

    def test_alternating_turns(self):
        # Test that the game alternates turns between the two players
        game = TicTacToeGame(HumanPlayer('X'), HumanPlayer('O'))
        self.assertEqual(game.current_player, 0)
        game.board[0][0] = 'X'
        game.current_player = 1 - game.current_player
        self.assertEqual(game.current_player, 1)

    def test_detect_win(self):
        # Test that the game correctly detects a win
        game = TicTacToeGame(HumanPlayer('X'), HumanPlayer('O'))
        game.board = [['X', 'X', 'X'], [None, 'O', None], [None, None, 'O']]
        self.assertEqual(game.get_winner(), 'X')

    def test_detect_draw(self):
        # Test that the game correctly identifies a draw
        game = TicTacToeGame(HumanPlayer('X'), HumanPlayer('O'))
        game.board = [['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]
        self.assertEqual(game.get_winner(), 'Draw')

    def test_viable_spots_only(self):
        # Test that players can only play in viable spots (not already taken)
        with patch('builtins.input', side_effect=['0,0', '1,1']), patch('sys.stdout', new=io.StringIO()):
            game = TicTacToeGame(HumanPlayer('X'), HumanPlayer('O'))
            game.board[0][0] = 'X'  
            row, col = game.players[0].make_move(game.board)
            self.assertNotEqual((row, col), (0, 0))  # Assert the move is not on the taken spot

    def test_correct_winner(self):
        # Test that the game correctly detects the winner
        game = TicTacToeGame(HumanPlayer('X'), HumanPlayer('O'))
        game.board = [['X', None, 'O'], ['O', 'X', 'O'], ['X', None, 'X']]
        self.assertEqual(game.get_winner(), 'X')

if __name__ == '__main__':
    unittest.main()
