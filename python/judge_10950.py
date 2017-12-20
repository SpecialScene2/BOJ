#10950
# a = int(input())
# for i in range(a):
#     b,c = map(int, input().split())
#     print(b+c)

#10951
# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except ValueError:
#         break

#10952
# while True:
#     a, b = map(int, input().split())
#     if a == 0 & b == 0:
#         break
#     else:
#         print(a+b)

# 10953
a = int(input())
for i in range(a):
    b,c = map(int, input().split(','))
    print(b+c)