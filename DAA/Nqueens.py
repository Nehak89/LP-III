def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(board, row, n, solutions):
    if row == n:
        # Append a copy of the current solution
        solutions.append(board[:])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens(board, row + 1, n, solutions)
            board[row] = -1  # Backtrack

def print_board(board, n):
    for i in range(n):
        row = ['Q' if j == board[i] else '.' for j in range(n)]
        print(' '.join(row))
    print()

def n_queens(n):
    board = [-1] * n
    solutions = []
    solve_n_queens(board, 0, n, solutions)

    if not solutions:
        print(f"No solution exists for N = {n}")
    else:
        print(f"\n{len(solutions)} solution(s) exist for N = {n}\n")
        for idx, sol in enumerate(solutions, 1):
            print(f"Solution {idx}:")
            print_board(sol, n)

# User input for N
n = int(input("Enter the value of N for N-Queens: "))
n_queens(n)
