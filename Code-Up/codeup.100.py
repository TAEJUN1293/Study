# 코드업 100제 6095
'''
n = int(input())
matrix = [[0 for i in range(20)]for j in range(20)]

for _ in range(n):
    a,b = map(int, input().split())
    matrix[a][b] = 1
for i in range(1,20):
    for j in range(1,20):
        print(matrix[i][j], end=' ')
    print()
'''

# 6096 코드업
'''
matrix = [[]*19 for _ in range(19)]
for i in range(19):
    matrix[i] = list(map(int, input().split()))
n = int(input())

for i in range(n):
    a,b = map(int, input().split())
    for j in range(19):
        if matrix[a-1][j] == 1:
            matrix[a-1][j] = 0
        else:
            matrix[a-1][j] = 1
    for j in range(19):
        if matrix[j][b-1] == 1:
            matrix[j][b-1] = 0
        else:
            matrix[j][b-1] = 1
for i in range(19):
    for j in range(19):
        print(matrix[i][j], end = ' ')
    print()'''

### 6097 코드업
'''
h, w = map(int, input().split(' '))
n = int(input())
matrix = [[0]*w for _ in range(h)]

for i in range(n):
    l,d,x,y = map(int,input().split())

    for j in range(l):
        if d == 0 :
            matrix[x-1][y-1+j] = 1
        else :
            matrix[x-1+j][y-1] = 1

for i in range(h):
    for j in range(w):
        print(matrix[i][j], end = ' ')
    print()'''

### 6098 코드업
import sys
input = sys.stdin.readline

matrix = [[]*10 for i in range(10)]
for i in range(10):
    matrix[i] = list(map(int,input().split()))

x = 1
y = 1

matrix[x][y] = 0
while True:
    if matrix[x][y] == 2:
        matrix[x][y] = 9
        break
    if matrix[x][y+1] != 1:
        matrix[x][y] = 9
        y += 1
    else :
        if matrix[x+1][y] != 1:
            matrix[x][y] = 9
            x += 1
        else :
            matrix[x][y] = 9
            break
for i in range(10):
    for j in range(10):
        print(matrix[i][j], end = ' ')
    print()