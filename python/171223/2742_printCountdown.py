from sys import stdin, stdout

read = lambda: stdin.readline().rstrip()
element = list(map(int, read().split()))[0]

for i in range(element, 0 ,-1):
    print(i)