import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.player = "X"
        self.board = [""] * 9
        self.buttons = []

        self.create_buttons()

    def create_buttons(self):
        for i in range(9):
            button = tk.Button(self.root, text="", font=("Arial", 24), height=2, width=5,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def make_move(self, index):
        if self.board[index] == "":
            self.board[index] = self.player
            self.buttons[index].config(text=self.player)

            if self.check_winner(self.player):
                messagebox.showinfo("Game Over", f"Player {self.player} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.player = "O" if self.player == "X" else "X"

    def check_winner(self, mark):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
            [0, 4, 8], [2, 4, 6]              # diags
        ]
        return any(all(self.board[i] == mark for i in condition) for condition in win_conditions)

    def reset_game(self):
        self.board = [""] * 9
        self.player = "X"
        for button in self.buttons:
            button.config(text="")

# Start the game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
