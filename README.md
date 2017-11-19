# PythonToTeX
The project can be used to transform Python arrays into LaTeX code which can help save time.

For instance, you may feel bored and annoyed to input a "bmatrix" in LaTex like:

    $\begin{pmatrix}
    1&3&4&6&9\\
    1&1&2&1&10\\
    2&5&1&9&2\\
    \end{pmatrix}$
    
It's really a complex work when you face a huge matrix. In this project, we may solve it by using Python. We can easily define function and return what we need. For example:

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
        
Life is short and we should make the tool more efficient.
