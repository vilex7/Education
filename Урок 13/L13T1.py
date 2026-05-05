import random

def create_matrix(rows, cols, min_val=-100, max_val=100):
    matrix = []
    for _ in range(rows):
        row = [random.randint(min_val, max_val) for _ in range(cols)]
        matrix.append(row)
    return matrix

def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0]) if rows > 0 else 0
    result = []
    for i in range(rows):
        row = [matrix_a[i][j] + matrix_b[i][j] for j in range(cols)]
        result.append(row)
    return result


matrix_1 = create_matrix(rows=int(input()), cols=int(input()))
matrix_2 = create_matrix(rows=int(input()), cols=int(input()))
matrix_3 = add_matrices(matrix_1, matrix_2)


print("Матрица 1:")
for row in matrix_1:
    print(row)

print("\nМатрица 2:")
for row in matrix_2:
    print(row)

print("\nСумма матриц (матрица 3):")
for row in matrix_3:
    print(row)