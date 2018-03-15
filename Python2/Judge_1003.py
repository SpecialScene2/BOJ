# judge_1003
final = [0,0]
def fibonacci(element):
    if element == 0:
        return [1, 0]
    elif element == 1:
        return [0, 1]
    elif 0<=element<=40:
        # if len(element)
        a, b = 1, 0
        c, d = 0, 1
        for i in range(element):
            a, b = b, a+b
            c, d = d, c+d
        final[0] = a
        final[1] = c
        return final

length = int(input())

for i in range(length):
    a = int(input())
    b = fibonacci(a)
    print(str(b[0]) + ' ' +str(b[1]))