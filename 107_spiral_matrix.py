matrix = [[0] * 4 for _ in range(4)]
top, bottom, left, right = 0, 3, 0, 3
num = 1
while top <= bottom and left <= right:
    for j in range(left, right + 1):
        matrix[top][j] = num; num += 1
    top += 1
    for i in range(top, bottom + 1):
        matrix[i][right] = num; num += 1
    right -= 1
    for j in range(right, left - 1, -1):
        matrix[bottom][j] = num; num += 1
    bottom -= 1
    for i in range(bottom, top - 1, -1):
        matrix[i][left] = num; num += 1
    left += 1
for row in matrix:
    print(*(f"{v:2d}" for v in row))
