import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game import TicTacToe

class TestTicTacToe(unittest.TestCase):
    """Тесты для класса TicTacToe."""

    def setUp(self) -> None:
        """Создать новый экземпляр игры перед каждым тестом."""
        self.game = TicTacToe()

    def test_initial_board(self) -> None:
        """Проверить, что доска инициализируется пустой."""
        self.assertEqual(self.game.board, [' '] * 9)

    def test_make_move(self) -> None:
        """Проверить, что ход успешно выполняется."""
        self.assertTrue(self.game.make_move(0))
        self.assertEqual(self.game.board[0], 'X')

    def test_make_move_on_occupied_space(self) -> None:
        """Проверить, что нельзя сделать ход на занятую клетку."""
        self.game.make_move(0)
        self.assertFalse(self.game.make_move(0))

    def test_switch_player(self) -> None:
        """Проверить, что игроки переключаются правильно."""
        self.assertEqual(self.game.current_player, 'X')
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 'O')

    def test_check_winner(self) -> None:
        """Проверить, что победитель определяется правильно."""
        # Пример 1: Проверка горизонтальной победы
        self.game.board = ['X', 'X', 'X', ' ', 'O', 'O', ' ', ' ', ' ']
        self.assertTrue(self.game.check_winner())
        
        # Пример 2: Проверка вертикальной победы
        self.game.board = ['X', 'O', ' ', 'X', 'O', ' ', 'X', ' ', ' ']
        self.assertTrue(self.game.check_winner())
        
        # Пример 3: Проверка диагональной победы
        self.game.board = ['X', 'O', 'O', ' ', 'X', ' ', ' ', 'O', 'X']
        self.assertTrue(self.game.check_winner())
        
        # Пример 4: Проверка, когда победителя нет
        self.game.board = ['O', 'X', 'O', 'X', 'O', 'X', ' ', ' ', ' ']
        self.assertFalse(self.game.check_winner())

    def test_is_board_full(self) -> None:
        """Проверить, что метод правильно определяет заполненную доску."""
        self.assertFalse(self.game.is_board_full())
        self.game.board = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
        self.assertTrue(self.game.is_board_full())

if __name__ == '__main__':
    unittest.main()