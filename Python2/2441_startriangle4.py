rowNum = int(input())

for i in range(rowNum, 0, -1):
    print(' '*(rowNum-i) + i*'*')
