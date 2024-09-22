# asked in zupee 3rd round

def spiral_print(input_matrix):
    ans = []
    if len(input_matrix) == 0:
        return ans

    m = len(input_matrix)
    n = len(input_matrix[0])

    visited = [[0 for i in range(n)] for j in range(m)]

    item_1 = [0, 1, 0, -1]
    item_2 = [1, 0, -1, 0]
    x = 0
    y = 0
    temp = 0

    for i in range(m * n):
        ans.append(input_matrix[x][y])
        visited[x][y] = True

        cr = x + item_1[temp]
        cc = y + item_2[temp]

        if 0 <= cr < m and 0 <= cc < n and not (visited[cr][cc]):
            x = cr
            y = cc
        else:
            temp = (temp + 1) % 4
            x += item_1[temp]
            y += item_2[temp]

    return ans


if __name__ == '__main__':
    input_matrix_1 = [[1, 2, 3, 4], [5, 6, 7, 8]]
    # input_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    # output = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    for out in spiral_print(input_matrix_1):
        print(out, end=",")
