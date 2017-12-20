element = int(input())
for i in range(1, element+1):
    print('*'*i+(' '*(2*element-2*i))+'*'*i)
for j in range(element-1, 0, -1):
    print('*' * j + (' ' * (2 * element - 2 * j)) + '*' * j)