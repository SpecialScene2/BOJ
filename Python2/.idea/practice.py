import sys

loop = int(input())  # 반복문을 수행할 int형 변수. 첫째 줄에서 입력
stack = []  # 스택 변수
length = len(stack)  # 스택의 길이를 받는 변수

# 첫째 줄에서 입력 받은 수가 (1 ≤ N ≤ 10,000) 을 만족하는지 판별
# 만족을 못하면 프로세스 종료
if loop < 0 or loop > 10000:
    sys.exit()

# 반복문 수행
for i in range(loop):
    # 입력 받는 부분
    # split()을 통해 하나씩 입력 받을 수 있다.
    # Split()이 없으면 loop만큼 입력을 계속 받는다.
    value = input().split()

    # push 하는 부분
    # value[0]은 입력받은 첫번째 요소이고, value[1]은 두번째 요소이다.
    # 만약 "push 4" 라는 입력을 했다면 value[0] == push, value[1] == 4 이다.
    # python3에서는 append()를 통해 배열에 요소를 추가할 수 있다.
    if value[0] == "push":
        stack.append(int(value[1]))
        length += 1

    elif value[0] == "pop":
        if length == 0:
            print(-1)
        else:
            # python3에서는 배열의 마이너스 인덱싱이 가능하다.
            # "lst[ len(lst) - 1 ]" 에서 "len(lst)" 가 생략되어있다고 생각하면 된다.
            print(stack[-1])

            # python3의 함수 중 pop()은 실제 stack의 pop과 같은 역할을 한다.
            # stack의 최상단에 있는 요소를 빼내고 크기를 줄이는 역할
            stack.pop()
            length -= 1

    elif value[0] == "size":
        print(length)


    elif value[0] == "empty":
        if length == 0:
            print(1)
        else:
            print(0)

    elif value[0] == "top":
        if length == 0:
            print(-1)
        else:
            print(stack[-1])