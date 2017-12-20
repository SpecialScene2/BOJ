from sys import stdin, stdout
read = lambda: stdin.readline().rstrip()
N = int(read())

container = []
for i in range(N):
    element = int(read())
    container.append(element)

newlist = []

def merge(a, b):
    index_a = 0
    index_b = 0
    c = []
    while index_a < len(a) and index_b< len(b): #index_a가 len(a)과 같거나 크다는 뜻은 모든 요소들을 훑었다는 뜻
        if a[index_a] <= b[index_b]: # a list요소가 b list요소 보다 작을때
             c.append(a[index_a]) # 대소비교에서 작았던 a list요소를 c에 넣어준다
             index_a = index_a + 1
        else: #반대경우 : 원리는 작은것을 c에 넣어준다.
             c.append(b[index_b])
             index_b = index_b + 1
    # 대소비교 다 끝나고 남는 쪽은 c에 붙여준다.
    c.extend(a[index_a:])
    c.extend(b[index_b:])
    return c

def msort(list) :
    global newlist
    if len(list) == 0 or len(list) == 1:
        return list[:len(list)] #리스트 길이가 0이거나 1이면 처음 넣어준 list가 return됨
    halfway = len(list) // 2
    list1 = list[0: halfway]
    list2 = list[halfway:len(list)]
    newlist1 = msort(list1)
    newlist2 = msort(list2)
    newlist = merge(newlist1, newlist2)
    return newlist

msort(container)
for i in newlist:
    stdout.write(str(i)+'\n')

'''
5
5
4
3
2
1
'''