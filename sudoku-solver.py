print("Sudoku Solver")

import numpy as np

dim = 9
sudoku = np.zeros(shape=(dim,dim))

def fillSudoku():
    print("fill")
    for i in range(0,(len(sudoku))):
        for j in range(0, len(sudoku[i])):
            # sudoku[i][j] = j + 9*i + 1
            sudoku[i][j] = 1

line = ((dim) * "--") + "-"

def printSudoku():
    print(line)
    for i in range(0,(len(sudoku))):
        print("|",end="")
        for j in range(0, len(sudoku[i])):
            print(int(sudoku[i][j]), end="|")
        if(i==len(sudoku)-1 and j == len(sudoku[i])-1):
            print("\n" + line)
       
        print("\n")

    

fillSudoku()
printSudoku()