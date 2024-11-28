input_size = input().split('x')
m = int(input_size[0])
n = int(input_size[1])
p = int(input())

board = []
for _ in range(m):
    board.append([0] * n)

mines = []

for _ in range(p):
    x, y = input().strip().split(',')
    x = int(x)
    y = int(y)
    mines.append((x, y))
    board[x][y] = '*'
    
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and board[nx][ny] != '*':
                board[nx][ny] += 1

for row in board:
    line = ''
    for cell in row:
        line += str(cell)
    print(line)