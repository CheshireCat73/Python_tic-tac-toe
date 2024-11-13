class TicTacToe:
    """Класс, представляющий игру в крестики-нолики."""

    def __init__(self) -> None:
        """Инициализация пустой доски и установка текущего игрока."""
        self.board: list[str] = [' ' for _ in range(9)]
        self.current_player: str = 'X'

    def make_move(self, position: int) -> bool:
        """Сделать ход на указанной позиции.

        Args:
            position (int): Позиция на доске (от 0 до 8).

        Returns:
            bool: True, если ход был успешным, иначе False.
        """
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        return False

    def switch_player(self) -> None:
        """Сменить текущего игрока."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self) -> bool:
        """Проверить, есть ли победитель.

        Returns:
            bool: True, если есть победитель, иначе False.
        """
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if (
                self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]
                and self.board[combo[0]] != ' '
            ):
                return True
        return False

    def is_board_full(self) -> bool:
        """Проверить, заполнена ли доска.

        Returns:
            bool: True, если доска заполнена, иначе False.
        """
        return ' ' not in self.board
