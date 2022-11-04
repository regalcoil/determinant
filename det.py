A = []

#rows for A in AB = C
m = int(input("How many rows & columns are there in A? --> "))
n = m


#specify which matrix the user is forming
matrixIndex = 1

#rotate through these command line inputs until both matrices (A and B, i.e. 2 matrices in total) are complete
while matrixIndex < 2:
    #forming A in AB = C
    if matrixIndex == 1:
        print("")
        #rotate through rows until m with this index
        rowIndex = 1
        while rowIndex <= m:
            row = []
            #rotate through colums until n with this index
            colIndex = 1
            while colIndex <= n:
                #user inputs the integer at the specified position in matrix A
                x = int(input("What is the integer in matrix A at row " + str(rowIndex) + ", column " + str(colIndex) + "? --> "))
                row.append(x)
                colIndex += 1
            #add the row to matrix A
            A.append(row)
            rowIndex += 1
    else:
        break
    matrixIndex += 1
#print the matrices to be multiplied
import numpy as np

print("")
for i in A:
    print(i)
print("")


if len(A) == 2:
    determinant = A[0][0]*A[1][1] - A[0][1]*A[1][0]
    print("determinant: " + determinant)
elif len(A) == 3:
    det1 = A[0][0] * (A[1][1]*A[2][2] - A[1][2]*A[2][1])
    det2 = A[0][1] * (A[1][0]*A[2][2] - A[1][2]*A[2][0])
    det3 = A[0][2] * (A[1][0]*A[2][1] - A[1][1]*A[2][0])
    determinant = det1 - det2 + det3
    print("determinant: " + determinant)
else:
    n_array = np.array(A)
    determinant = np.linalg.det(n_array)
    determinant = round(determinant)
    print("determinant: " + determinant)