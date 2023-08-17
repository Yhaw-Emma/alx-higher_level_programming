#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix by making a shallow copy of the input matrix.
    new_matrix = matrix.copy()

    # Iterate through each row of the matrix using index i.
    for i in range(len(matrix)):
        # Apply a mapping function using lambda to square each element in the current row.
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (new_matrix)
