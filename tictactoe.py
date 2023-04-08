import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.buttons = []

        # create buttons for each cell in the board
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text=" ", font=('Arial', 60), width=4, height=2,
                                    command=lambda row=i, col=j: self.play_move(row, col))
                button.grid(row=i, column=j, padx=10, pady=10, sticky="nsew")
                self.buttons.append(button)

        # create new game button
        new_game_button = tk.Button(self.master,text="New Game", fg="Blue" , font=('Arial', 20), command=self.new_game)
        new_game_button.grid(row=3, column=1, padx=10, pady=10)

        # create status label
        self.status_label = tk.Label(self.master, text=f"Current Player: {self.current_player}", font=('Arial', 20))
        self.status_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

    def play_move(self, row, col):
        index = row * 3 + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.update_button(row, col)
            if self.check_win():
                messagebox.showinfo("Game Over", f"{self.current_player} wins!")
                self.new_game()
            elif self.check_tie():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.new_game()
            else:
                self.switch_player()

    def update_button(self, row, col):
        index = row * 3 + col
        button = self.buttons[index]
        button.config(text=self.current_player)

    def check_win(self):
        # check rows
        for i in range(0, 9, 3):
            if self.board[i:i+3] == [self.current_player] * 3:
                return True

        # check columns
        for i in range(3):
            if self.board[i::3] == [self.current_player] * 3:
                return True

        # check diagonals
        if self.board[0] == self.current_player and self.board[4] == self.current_player and self.board[8] == self.current_player:
            return True
        if self.board[2] == self.current_player and self.board[4] == self.current_player and self.board[6] == self.current_player:
            return True

        return False

    def check_tie(self):
        return " " not in self.board

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        self.status_label.config(text=f"Current Player: {self.current_player}")

    def new_game(self):
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        for i, button in enumerate(self.buttons):
            button.config(text=" ")
        self.status_label.config(text=f"Current Player: {self.current_player}")

root = tk.Tk()
TicTacToeGUI(root)
root.mainloop()
