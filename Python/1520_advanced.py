#stdin, stdout
#rstrip을 하면 '\n'및 whitespace를 없애는거
from sys import stdin
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
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    global solutionMap
    solution = 0
    if row == 0 and col == 0:
        return 1
    else:
        for i in range(4):
            newRow = row + dr[i]
            newCol = col + dc[i]
            if 0<= newRow <= N-1 and 0 <= newCol <= M-1:
                if Map[row][col] < Map[newRow][newCol]:
                    if solutionMap[newRow][newCol] == -1:
                        solutionMap[newRow][newCol] = findWay(newRow, newCol)
                        solution += solutionMap[newRow][newCol]
                    else:
                        solution += solutionMap[newRow][newCol]
        solutionMap[row][col] = solution
    return solution
print(findWay(N-1,M-1))
# from pprint import pprint
# pprint(solutionMap, width=20)