def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    # matrix[0][0] matrix[0][1] matrix[0][2]
    # matrix[1][0] matrix[1][1] matrix[1][2]
    # matrix[2][0] matrix[2][1] matrix[2][2]

    size = len(matrix)

    sum1 = 0
    sum2 = 0

    # x will be assigned in the for loop
    # y needs to initialized here
    y = size - 1

    for x in range(size):
        sum1 += matrix[x][x]
        sum2 += matrix[y][x]
        y = y - 1
    
    return sum1 + sum2