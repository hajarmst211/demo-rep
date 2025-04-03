def get_minor(matrix, i, j):
    """Returns the minor of the element at row i, column j."""
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

def determinant(matrix):
    """Computes the determinant of a square matrix."""
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for j in range(size):
        det += ((-1) ** j) * matrix[0][j] * determinant(get_minor(matrix, 0, j))
    return det

def cofactor_matrix(matrix):
    """Computes the cofactor matrix of a square matrix."""
    size = len(matrix)
    cofactor = []
    for i in range(size):
        row = []
        for j in range(size):
            minor = get_minor(matrix, i, j)
            cofactor_value = ((-1) ** (i + j)) * determinant(minor)
            row.append(cofactor_value)
        cofactor.append(row)
    return cofactor

def transpose(matrix):
    """Returns the transpose of a matrix."""
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def inverse_matrix(matrix):
    """Computes the inverse of a square matrix using the adjugate method."""
    det = determinant(matrix)
    if det == 0:
        raise ValueError("Matrix is singular and cannot be inverted.")
    
    cofactor = cofactor_matrix(matrix)
    adjugate = transpose(cofactor)
    inverse = [[adjugate[i][j] / det for j in range(len(matrix))] for i in range(len(matrix))]
    
    return inverse

# Example usage
matrix = [
    [4, 7],
    [2, 6]
]

inv_matrix = inverse_matrix(matrix)
for row in inv_matrix:
    print(row)