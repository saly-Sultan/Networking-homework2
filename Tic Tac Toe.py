import tkinter as tk
from tkinter import font

def print_board(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                buttons[i][j].config(text="X", fg="blue", font=large_font)
            elif board[i][j] == "O":
                buttons[i][j].config(text="O", fg="red", font=large_font)
            else:
                buttons[i][j].config(text="", font=large_font)

def check_winner(board, player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def handle_click(row, col):
    global current_player
    if board[row][col] == " ":
        board[row][col] = current_player
        print_board(board)
        if check_winner(board, current_player):
            if current_player == "X":
                status_label.config(text="Player X wins!", fg="blue")
            else:
                status_label.config(text="Player O wins!", fg="red")
            disable_buttons()
            return
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
        status_label.config(text=f"Player {current_player}'s turn", fg="black")

def disable_buttons():
    for row in buttons:
        for button in row:
            button.config(state="disabled")

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

current_player = "X"

root = tk.Tk()
root.title("Tic Tac Toe")

large_font = font.Font(size=24, weight="bold")

buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(root, text="", width=5, height=2, command=lambda x=i, y=j: handle_click(x, y))
        button.grid(row=i, column=j, padx=10, pady=10)
        row.append(button)
    buttons.append(row)

status_label = tk.Label(root, text=f"Player {current_player}'s turn", font=large_font, pady=10)
status_label.grid(row=3, column=0, columnspan=3)

root.mainloop()