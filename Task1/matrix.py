from Task1.printMatrix import print_matrix
from Task1.transpose import transpose


def task1_matrix():
    matrix_1 = [[1]]
    matrix_2 = [[2, 3], [4, 5]]
    matrix_3 = [[6, 7, 8], [9, 10, 11]]
    matrix_4 = [[12, 13], [14, 15], [16, 17]]

    print("Original matrix: \nFirst:")
    print_matrix(matrix_1)

    print("Second:")
    print_matrix(matrix_2)

    print("Third:")
    print_matrix(matrix_3)

    print("Fourth:")
    print_matrix(matrix_4)

    matrix_1_transpose = transpose(matrix_1)
    matrix_2_transpose = transpose(matrix_2)
    matrix_3_transpose = transpose(matrix_3)
    matrix_4_transpose = transpose(matrix_4)

    print("After transpose: \nFirst:")
    print_matrix(matrix_1_transpose)

    print("Second:")
    print_matrix(matrix_2_transpose)

    print("Third:")
    print_matrix(matrix_3_transpose)

    print("Fourth:")
    print_matrix(matrix_4_transpose)
