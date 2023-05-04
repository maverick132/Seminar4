def print_matrix(matrix):
    for row in matrix:
        for x in row:
            print("{:4d}".format(x), end="")
        print()
