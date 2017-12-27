#stdin, stdout
#rstrip을 하면 '\n'및 whitespace를 없애는거
from sys import stdin, stdout
# lambda를 쓰면 read가 함수다.
read = lambda: stdin.readline().rstrip()
size = list(map(int, read().split()))

N = size[0]
M = size[1]

Map = []
for i in range(N):
    read = lambda: stdin.readline().rstrip()
    Map.append(list(map(int, read().split())))
# print(Map)

solutionMap = []
for j in range(N):
    temp = []
    for k in range(M):
        temp.append(-1)
    solutionMap.append(temp)
# print(solutionMap)

def findWay(row,col):
    global solutionMap
    value = Map[row][col]
    solution = 0
    if row == 0 and col == 0:
        return 1
    if row > 0:
        if value < Map[row-1][col]:
            if solutionMap[row-1][col] != -1:
                solution += solutionMap[row-1][col]
            else:
                solutionMap[row-1][col] = findWay(row-1, col)
                solution += solutionMap[row-1][col]
    if row < N-1:
        if value < Map[row+1][col]:
            if solutionMap[row+1][col] != -1:
                solution += solutionMap[row+1][col]
            else:
                solutionMap[row+1][col] = findWay(row+1, col)
                solution += solutionMap[row+1][col]
    if col > 0:
        if value < Map[row][col-1]:
            if solutionMap[row][col-1] != -1:
                solution += solutionMap[row][col-1]
            else:
                solutionMap[row][col-1] = findWay(row, col-1)
                solution += solutionMap[row][col-1]
    if col < M-1:
        if value < Map[row][col+1]:
            if solutionMap[row][col+1] != -1:
                solution += solutionMap[row][col+1]
            else:
                solutionMap[row][col+1] = findWay(row, col+1)
                solution += solutionMap[row][col+1]
    solutionMap[row][col] = solution
    return solution
print(findWay(N-1,M-1))