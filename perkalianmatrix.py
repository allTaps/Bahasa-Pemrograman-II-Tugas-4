matrix1 = [
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [4, 5, 3, 2, 1],
    [3, 5, 2, 1, 4],
    [2, 4, 5, 1, 3]
]

matrix2 = [
    [1, 2, 2, 1, 3],
    [2, 2, 3, 1, 3],
    [3, 3, 2, 1, 2],
    [1, 1, 1, 2, 3],
    [3, 2, 1, 2, 2]
]

hasilMatrix = []
for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix2[0])):
        sum = 0
        for k in range(len(matrix2)):
            sum += matrix1[i][k] * matrix2[k][j]
        row.append(sum)
    hasilMatrix.append(row)

print("Hasil perkalian matrix:")
for row in hasilMatrix:
    print(row)