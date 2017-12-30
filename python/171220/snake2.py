from sys import stdin, exit

read = lambda: stdin.readline().rstrip()
N = int(read())

Map = []
for i in range(N):
    temp = []
    for j in range(N):
        temp.append(0)
    Map.append(temp)
print(Map)

appleNum = int(read())

appleLocate = []
for k in range(appleNum):
    temp = list(map(int,read().split()))
    Map[temp[0]-1][temp[1]-1] = 1
    # appleLocate.append(temp)
print(Map)

#왼쪽 L, 오른쪽 D
directionLoop = int(read())
print('directionLoop',directionLoop)

order2 = []
for z in range(directionLoop):
    temp = list(read().split())
    temp[0] = int(temp[0])
    order2.append(temp)
# print(order2)

container = []
for g in order2:
    container.append(g[0])
# print(container)

container2 = [container[0]]
for u in range(1,len(container)):
    container2.append(container[u]-container[u-1])
# print(container2)

order =[]
for n in range(len(order2)):
    order.append([container2[n],order2[n][1]])
print('order',order)

# Direction = ['E','W','S','N']
# snake = [Direction[0], snakeHead, []]
# seconds = 0
# head = snake[1]
# body = snake[2]
snakeHead = [0,0]
snakeBody = []
snake = [snakeHead, snakeBody]
future = 'E'
current = 'E'
count = 0

def goSnake(pastDir, toDir, snakeInf, order):
    global count, current, future, Map, snake
    dir = pastDir
    dir2 = toDir
    head = snakeInf[0]
    body = snakeInf[1]
    for i in range(1, order[0]+1): # i는 i초를 뜻함
        count+=1
        print(i)
        print(dir, dir2, head, body, order)
        if dir == 'E' and dir2 == 'E': # 유니크한 케이스 : 처음에 시작할때를 과거 현재방향을 E로 줌.
            print('여기')
            newHead = [head[0],head[1]+1] # 일단 머리부터 옮겨 두고
            if 0 <= newHead[0] <= N-1 and 0 <= newHead[1] <= N-1 : # 머리 검증 : Map을 벗어 나지 않는 경우
                if newHead in body: # 머리 검증2 : Map 안 벗어 나더라도 body에 박을 수 있음.
                    return count
                elif Map[newHead[0]][newHead[1]] == 1: # newHead로 이동한 곳에 사과가 놓여져있는 경우
                    Map[newHead[0]][newHead[1]] = 0 # 사과 먹었으니 0으로 바꿔준다.
                    if body:
                        forAppend = body[-1]
                        for j in body:
                            j[1] += 1
                        body.append(forAppend)
                    else:
                        body.append(head)
                else: # 사과 안 먹은 경우는 body를 1칸씩 움직여준다.
                    if body:
                        for j in body:
                            j[1] += 1
            else:
                return count
            current = dir2
            if order[1] == 'D':
                future = 'S'
            else:
                future = 'N'
            head = newHead
            snake = [head, body]

        elif dir == 'E' and dir2 == 'S':
            newHead = [head[0]+1,head[1]] # 일단 머리부터 옮겨 두고
            if 0 <= newHead[0] <= N-1 and 0 <= newHead[1] <= N-1 : # 머리 검증 : Map을 벗어 나지 않는 경우
                if newHead in body: # 머리 검증2 : Map 안 벗어 나더라도 body에 박을 수 있음.
                    return count
                elif Map[newHead[0]][newHead[1]] == 1: # newHead로 이동한 곳에 사과가 놓여져있는 경우
                    Map[newHead[0]][newHead[1]] = 0 # 사과 먹었으니 0으로 바꿔준다.
                    if body:
                        if i > 1 :
                            forAppend = body[-1]
                            for j in body[:i-1]:
                                j[0] += 1 # S방향으로 향하는 부분들은 row값을 키워준다.
                            for k in body[i-1:]:
                                k[1] += 1 # S방향으로 가지 못하고 E방향으로 가는 녀석들은 col 값만 키워준다.
                            body.append(forAppend)
                    else: # body가 없었던 경우
                        body.append(head)
                elif Map[newHead[0]][newHead[1]] == 0: # 사과 안 먹은 경우는 body를 1칸씩 움직여준다.
                    if body:
                        if i > 1 :
                            for j in body[:i-1]:
                                j[0] += 1 # S방향으로 향하는 부분들은 row값을 키워준다.
                            for k in body[i-1:]:
                                k[1] += 1 # S방향으로 가지 못하고 E방향으로 가는 녀석들은 col 값만 키워준다.
                if newHead in body: # 머리 검증2 : Map 안 벗어 나더라도 body에 박을 수 있음.
                    return count
            else:
                return count
            current = dir2
            if order[1] == 'D':
                future = 'W'
            else:
                future = 'E'
            head = newHead
            snake = [head, body]

        elif dir == 'E' and dir2 == 'N':
            newHead = [head[0] - 1, head[1]]  # 일단 머리부터 옮겨 두고
            if 0 <= newHead[0] <= N - 1 and 0 <= newHead[1] <= N - 1:  # 머리 검증 : Map을 벗어 나지 않는 경우
                if newHead in body:  # 머리 검증2 : Map 안 벗어 나더라도 body에 박을 수 있음.
                    return count
                elif Map[newHead[0]][newHead[1]] == 1:  # newHead로 이동한 곳에 사과가 놓여져있는 경우
                    Map[newHead[0]][newHead[1]] = 0  # 사과 먹었으니 0으로 바꿔준다.
                    if body:
                        if i > 1:
                            forAppend = body[-1]
                            for j in body[:i - 1]:
                                j[0] -= 1  # S방향으로 향하는 부분들은 row값을 키워준다.
                            for k in body[i - 1:]:
                                k[1] += 1  # S방향으로 가지 못하고 E방향으로 가는 녀석들은 col 값만 키워준다.
                            body.append(forAppend)
                    else:  # body가 없었던 경우
                        body.append(head)
                elif Map[newHead[0]][newHead[1]] == 0:  # 사과 안 먹은 경우는 body를 1칸씩 움직여준다.
                    if body:
                        if i > 1:
                            for j in body[:i - 1]:
                                j[0] -= 1  # N방향으로 향하는 부분들은 row값을 키워준다.
                            for k in body[i - 1:]:
                                k[1] += 1  # N방향으로 가지 못하고 E방향으로 가는 녀석들은 col 값만 키워준다.
                if newHead in body: # 머리 검증2 : Map 안 벗어 나더라도 body에 박을 수 있음.
                    return count
            else:
                return count
            current = dir2
            if order[1] == 'D':
                future = 'E'
            else:
                future = 'W'
            head = newHead
            snake = [head, body]

        elif dir == 'S' and dir2 == 'W':
            newHead = [head[0], head[1] - 1]  # 일단 머리부터 옮겨 두고
            if 0 <= newHead[0] <= N - 1 and 0 <= newHead[1] <= N - 1:  # 머리 검증 : Map을 벗어 나지 않는 경우
                if newHead in body: # 머리 검증2 : Map 안 벗어 나더라도 body에 박을 수 있음.
                    return count
                elif Map[newHead[0]][newHead[1]] == 1:  # newHead로 이동한 곳에 사과가 놓여져있는 경우
                    Map[newHead[0]][newHead[1]] = 0  # 사과 먹었으니 0으로 바꿔준다.
                    if body:
                        if i > 1:
                            forAppend = body[-1]
                            for j in body[:i - 1]:
                                j[1] -= 1  # W방향으로 향하는 부분들은 col값을 줄여준다.
                            for k in body[i - 1:]:
                                k[0] += 1  # W방향으로 가지 못하고 S방향으로 가는 녀석들은 row값만 키워준다.
                            body.append(forAppend)
                    else:  # body가 없었던 경우
                        body.append(head)
                elif Map[newHead[0]][newHead[1]] == 0:  # 사과 안 먹은 경우는 body를 1칸씩 움직여준다.
                    if body:
                        if i > 1:
                            for j in body[:i - 1]:
                                j[1] -= 1  # W방향으로 향하는 부분들은 col값을 키워준다.
                            for k in body[i - 1:]:
                                k[0] += 1  # W방향으로 가지 못하고 S방향으로 가는 녀석들은 row값만 키워준다.
                if newHead in body: # 머리 검증2 : Map 안 벗어 나더라도 body에 박을 수 있음.
                    return count
            else:
                return count
            current = dir2
            if order[1] == 'D':
                future = 'N'
            else:
                future = 'S'
            head = newHead
            snake = [head, body]

        elif dir == 'S' and dir2 == 'E':
            newHead = [head[0], head[1] + 1]  # 일단 머리부터 옮겨 두고
            if 0 <= newHead[0] <= N - 1 and 0 <= newHead[1] <= N - 1:  # 머리 검증 : Map을 벗어 나지 않는 경우
                if newHead in body: # 머리 검증2 : Map 안 벗어 나더라도 body에 박을 수 있음.
                    return count
                elif Map[newHead[0]][newHead[1]] == 1:  # newHead로 이동한 곳에 사과가 놓여져있는 경우
                    Map[newHead[0]][newHead[1]] = 0  # 사과 먹었으니 0으로 바꿔준다.
                    if body:
                        if i > 1:
                            forAppend = body[-1]
                            for j in body[:i - 1]:
                                j[1] += 1  # E방향으로 향하는 부분들은 col값을 키워준다
                            for k in body[i - 1:]:
                                k[0] += 1  # E방향으로 가지 못하고 S방향으로 가는 녀석들은 row값만 키워준다.
                            body.append(forAppend)
                    else:  # body가 없었던 경우
                        body.append(head)
                elif Map[newHead[0]][newHead[1]] == 0:  # 사과 안 먹은 경우는 body를 1칸씩 움직여준다.
                    if body:
                        if i > 1:
                            for j in body[:i - 1]:
                                j[1] += 1  # E방향으로 향하는 부분들은 col값을 키워준다
                            for k in body[i - 1:]:
                                k[0] += 1  # E방향으로 가지 못하고 S방향으로 가는 녀석들은 row값만 키워준다.
                if newHead in body: # 머리 검증2 : Map 안 벗어 나더라도 body에 박을 수 있음.
                    return count
            else:
                return count
            current = dir2
            if order[1] == 'D':
                future = 'S'
            else:
                future = 'N'
            head = newHead
            snake = [head, body]

        elif dir == 'W' and dir2 == 'N':
            newHead = [head[0]-1, head[1]]  # 일단 머리부터 옮겨 두고
            if 0 <= newHead[0] <= N - 1 and 0 <= newHead[1] <= N - 1:  # 머리 검증 : Map을 벗어 나지 않는 경우
                if newHead in body: # 머리 검증2 : Map 안 벗어 나더라도 body에 박을 수 있음.
                    return count
                elif Map[newHead[0]][newHead[1]] == 1:  # newHead로 이동한 곳에 사과가 놓여져있는 경우
                    Map[newHead[0]][newHead[1]] = 0  # 사과 먹었으니 0으로 바꿔준다.
                    if body:
                        if i > 1:
                            forAppend = body[-1]
                            for j in body[:i - 1]:
                                j[0] -= 1  # N방향으로 향하는 부분들은 row값을  줄여준다
                            for k in body[i - 1:]:
                                k[1] -= 1  # N방향으로 가지 못하고 W방향으로 가는 녀석들은 col값만 줄여준다.
                            body.append(forAppend)
                    else:  # body가 없었던 경우
                        body.append(head)
                elif Map[newHead[0]][newHead[1]] == 0:  # 사과 안 먹은 경우는 body를 1칸씩 움직여준다.
                    if body:
                        if i > 1:
                            for j in body[:i - 1]:
                                j[0] -= 1  # N방향으로 향하는 부분들은 row값을  줄여준다
                            for k in body[i - 1:]:
                                k[1] -= 1  # N방향으로 가지 못하고 W방향으로 가는 녀석들은 col값만 줄여준다.
                if newHead in body: # 머리 검증2 : Map 안 벗어 나더라도 body에 박을 수 있음.
                    return count
            else:
                return count
            current = dir2
            if order[1] == 'D':
                future = 'E'
            else:
                future = 'W'
            head = newHead
            snake = [head, body]

        elif dir == 'W' and dir2 == 'S':
            newHead = [head[0]+1, head[1]]  # 일단 머리부터 옮겨 두고
            if 0 <= newHead[0] <= N - 1 and 0 <= newHead[1] <= N - 1:  # 머리 검증 : Map을 벗어 나지 않는 경우
                if newHead in body: # 머리 검증2 : Map 안 벗어 나더라도 body에 박을 수 있음.
                    return count
                elif Map[newHead[0]][newHead[1]] == 1:  # newHead로 이동한 곳에 사과가 놓여져있는 경우
                    Map[newHead[0]][newHead[1]] = 0  # 사과 먹었으니 0으로 바꿔준다.
                    if body:
                        if i > 1:
                            forAppend = body[-1]
                            for j in body[:i - 1]:
                                j[0] += 1  # S방향으로 향하는 부분들은 row값을 늘려준다
                            for k in body[i - 1:]:
                                k[1] -= 1  # S방향으로 가지 못하고 W방향으로 가는 녀석들은 col값만 줄여준다.
                            body.append(forAppend)
                    else:  # body가 없었던 경우
                        body.append(head)
                elif Map[newHead[0]][newHead[1]] == 0:  # 사과 안 먹은 경우는 body를 1칸씩 움직여준다.
                    if body:
                        if i > 1:
                            for j in body[:i - 1]:
                                j[0] += 1  # S방향으로 향하는 부분들은 row값을 늘려준다
                            for k in body[i - 1:]:
                                k[1] -= 1  # S방향으로 가지 못하고 W방향으로 가는 녀석들은 col값만 줄여준다.
                if newHead in body: # 머리 검증2 : Map 안 벗어 나더라도 body에 박을 수 있음.
                    return count
            else:
                return count
            current = dir2
            if order[1] == 'D':
                future = 'W'
            else:
                future = 'E'
            head = newHead
            snake = [head, body]

        elif dir == 'N' and dir2 == 'E':
            newHead = [head[0], head[1]+1]  # 일단 머리부터 옮겨 두고
            if 0 <= newHead[0] <= N - 1 and 0 <= newHead[1] <= N - 1:  # 머리 검증 : Map을 벗어 나지 않는 경우
                if newHead in body: # 머리 검증2 : Map 안 벗어 나더라도 body에 박을 수 있음.
                    return count
                elif Map[newHead[0]][newHead[1]] == 1:  # newHead로 이동한 곳에 사과가 놓여져있는 경우
                    Map[newHead[0]][newHead[1]] = 0  # 사과 먹었으니 0으로 바꿔준다.
                    if body:
                        if i > 1:
                            forAppend = body[-1]
                            for j in body[:i - 1]:
                                j[1] += 1  # E방향으로 향하는 부분들은 col값을 늘려준다
                            for k in body[i - 1:]:
                                k[0] -= 1  # E방향으로 가지 못하고 N방향으로 가는 녀석들은 row값만 줄여준다.
                            body.append(forAppend)
                    else:  # body가 없었던 경우
                        body.append(head)
                elif Map[newHead[0]][newHead[1]] == 0:  # 사과 안 먹은 경우는 body를 1칸씩 움직여준다.
                    if body:
                        if i > 1:
                            for j in body[:i - 1]:
                                j[1] += 1  # E방향으로 향하는 부분들은 col값을 늘려준다
                            for k in body[i - 1:]:
                                k[0] -= 1  # E방향으로 가지 못하고 N방향으로 가는 녀석들은 row값만 줄여준다.
                if newHead in body: # 머리 검증2 : Map 안 벗어 나더라도 body에 박을 수 있음.
                    return count
            else:
                return count
            current = dir2
            if order[1] == 'D':
                future = 'S'
            else:
                future = 'N'
            head = newHead
            snake = [head, body]

        elif dir == 'N' and dir2 == 'W':
            newHead = [head[0], head[1]-1]  # 일단 머리부터 옮겨 두고
            if 0 <= newHead[0] <= N - 1 and 0 <= newHead[1] <= N - 1:  # 머리 검증 : Map을 벗어 나지 않는 경우
                if newHead in body: # 머리 검증2 : Map 안 벗어 나더라도 body에 박을 수 있음.
                    return count
                elif Map[newHead[0]][newHead[1]] == 1:  # newHead로 이동한 곳에 사과가 놓여져있는 경우
                    Map[newHead[0]][newHead[1]] = 0  # 사과 먹었으니 0으로 바꿔준다.
                    if body:
                        if i > 1:
                            forAppend = body[-1]
                            for j in body[:i - 1]:
                                j[1] -= 1  # W방향으로 향하는 부분들은 col값을 줄여준다
                            for k in body[i - 1:]:
                                k[0] -= 1  # W방향으로 가지 못하고 N방향으로 가는 녀석들은 row값만 줄여준다.
                            body.append(forAppend)
                    else:  # body가 없었던 경우
                        body.append(head)
                elif Map[newHead[0]][newHead[1]] == 0:  # 사과 안 먹은 경우는 body를 1칸씩 움직여준다.
                    if body:
                        if i > 1:
                            for j in body[:i - 1]:
                                j[1] -= 1  # W방향으로 향하는 부분들은 col값을 줄여준다
                            for k in body[i - 1:]:
                                k[0] -= 1  # W방향으로 가지 못하고 N방향으로 가는 녀석들은 row값만 줄여준다.
                if newHead in body: # 머리 검증2 : Map 안 벗어 나더라도 body에 박을 수 있음.
                    return count
            else:
                return count
            current = dir2
            if order[1] == 'D':
                future = 'S'
            else:
                future = 'N'
            head = newHead
            snake = [head, body]

for i in range(directionLoop):
    print('횟수', order[i])
    a = goSnake(current, future, snake, order[i])
    if a:
        print(a)
        exit()
    else:
        print('%d번째 까지는 정상' %i)
        continue