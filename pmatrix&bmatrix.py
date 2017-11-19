# -*- coding: utf-8 -*-
# pmatrix and bmatrix
import numpy as np

def pmatrix(a):
    matrix = ""
    row, col = a.shape
    if row > 1:
        for i in range(0,row):
            for j in range(0,col):
                if j != col-1:
                    matrix = matrix + str(a[i][j]) + r"&"
                else:
                    matrix = matrix + str(a[i][j])
            matrix = matrix + "\\\\\n"
    """
    else:
        for i in range(0,row):
            if i != row:
                matrix = matrix + str(a[i]) + r"&"
            else:
                matrix = matrix + str(a[i])
        matrix = matrix + "\\\\\n"  
    """
    print("""
$\\begin{pmatrix}
%s\\end{pmatrix}$
"""%matrix)
    return 0

def bmatrix(a):
    matrix = ""
    row, col = a.shape
    if row > 1:
        for i in range(0,row):
            for j in range(0,col):
                if j != col-1:
                    matrix = matrix + str(a[i][j]) + r"&"
                else:
                    matrix = matrix + str(a[i][j])
            matrix = matrix + "\\\\\n"
    """
    else:
        for i in range(0,row):
            if i != row:
                matrix = matrix + str(a[i]) + r"&"
            else:
                matrix = matrix + str(a[i])
        matrix = matrix + "\\\\\n"  
    """
    print("""
$\\begin{bmatrix}
%s\\end{bmatrix}$
"""%matrix)
    return 0
a = np.array([
    [1, 3, 4, 6, 9],
    [1, 1, 2, 1, 10],
    [2, 5, 1, 9, 2]
])
pmatrix(a)



            
