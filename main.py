# This is the main file of the tic-tac-toe game
from tic_tac_toe import *

game_board = [
	["1", "2", "3"],
	["4", "5", "6"],
	["7", "8", "9"]
]

print()
print("Welcome to Tic Tac Toe!")
print()

print("Game has started!")
print("You are player X.")
print()
print_board(game_board)
while not game_is_over(game_board):
    print("Player X moves.")
    space = int(input("Enter a free space: "))
    while not space in available_moves(game_board):
        space = int(input("Enter a free space: "))
    select_space(game_board, space, "X")
    print()
    print_board(game_board)
    if not game_is_over(game_board):
        print("Player O moves.")
        select_space(game_board, minimax(game_board, False)[1], "O")
        print()
        print_board(game_board)

print("Game ended.")
result = evaluate_board(game_board)
if result == 1:
    print("X wins!")
elif result == -1:
    print("O wins!")
else:
    print("It's a draw!")
print()