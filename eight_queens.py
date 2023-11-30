import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd

def solve_n_queens(n):
    solutions = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(board, 0, solutions)
    return solutions

def backtrack(board, row, solutions):
    if row == len(board):
        # one solution
        solutions.append([''.join(row) for row in board])
        return

    for col in range(len(board)):
        if is_valid(board, row, col):
            board[row][col] = 'Q'
            backtrack(board, row + 1, solutions)
            board[row][col] = '.'

def is_valid(board, row, col):
    # check 1
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # check 2
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # check 3
    i, j = row - 1, col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

solutions = solve_n_queens(8)

# Save solutions to Excel
excel_filename = 'n_queens_solutions_matplotlib_pandas.xlsx'
excel_writer = pd.ExcelWriter(excel_filename, engine='xlsxwriter')

for i, solution in enumerate(solutions):
    df_solution = pd.DataFrame([list(row) for row in solution], columns=[f'Column_{j+1}' for j in range(len(solution[0]))])
    df_solution.to_excel(excel_writer, sheet_name=f'Solution_{i+1}', index=False)

excel_writer.save()

# Save solutions to PDF
pdf_filename = 'n_queens_solutions_matplotlib_pandas.pdf'
with PdfPages(pdf_filename) as pdf:
    for i, solution in enumerate(solutions):
        plt.figure()
        plt.imshow([[1 if cell == 'Q' else 0 for cell in row] for row in solution], cmap='Blues', vmin=0, vmax=1)
        plt.title(f'Solution {i+1}')
        plt.axis('off')
        pdf.savefig()
        plt.close()

print(f"Excel file '{excel_filename}' and PDF file '{pdf_filename}' created successfully.")
