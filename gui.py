import tkinter as tk
from tkinter import messagebox
from game import TicTacToe


class TicTacToeGUI:
    """Графический интерфейс для игры в крестики-нолики."""

    def __init__(self) -> None:
        """Инициализация графического интерфейса и игры."""
        self.game: TicTacToe = TicTacToe()
        self.window: tk.Tk = tk.Tk()
        self.window.title("Крестики-Нолики")
        self.buttons: list[tk.Button] = [
            tk.Button(
                self.window,
                text=' ',
                font='Arial 20',
                width=5,
                height=2,
                сommand=lambda i=i: self.on_button_click(i),
                bg='lightgray'
                ) for i in range(9)
            ]
        self.create_grid()

    def create_grid(self) -> None:
        """Создать сетку кнопок для игры."""
        for i, button in enumerate(self.buttons):
            button.grid(row=i // 3, column=i % 3)

    def on_button_click(self, position: int) -> None:
        """Обработать нажатие кнопки.

        Args:
            position (int): Позиция кнопки, на которую нажали.
        """
        if self.game.make_move(position):
            self.buttons[position].config(
                text=self.game.current_player,
                bg='lightblue' if self.game.current_player == 'X' else 'lightgreen'
            )
            if self.game.check_winner():
                messagebox.showinfo(
                    "Игра окончена",
                    f"Игрок {self.game.current_player} выиграл!"
                    )
                self.reset_game()
            elif self.game.is_board_full():
                messagebox.showinfo("Игра окончена", "Ничья!")
                self.reset_game()
            else:
                self.game.switch_player()

    def reset_game(self) -> None:
        """Сбросить игру к начальному состоянию."""
        self.game = TicTacToe()
        for button in self.buttons:
            button.config(text=' ', bg='lightgray')

    def run(self) -> None:
        """Запустить графический интерфейс."""
        self.window.mainloop()
