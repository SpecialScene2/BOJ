N = int(input())

container = []
for i in range(N):
    element = int(input())
    container.append(element)

def quick_sort(items):
    if len(items) > 1:
        pivot_index = len(items) // 2 # 홀수이면 정중앙에 있는 요소, 짝수이면 우측으로 한칸 치우친 위치
        smaller_items = []
        larger_items = []

        for i, val in enumerate(items): #i는 인덱스값, val은 요소값
            if i != pivot_index: # 인덱스 값 자신하고는 비교하는 경우를 제외하기 위해
                if val < items[pivot_index]: #pivot 보다 작으면 smaller list에 넣기
                    smaller_items.append(val)
                else:                        #pivot 보다 크면 larger list에 넣기
                    larger_items.append(val)
        #smaller or larger는 items[pivot_index]보다 작거나 크기는 하지만
        #자기들끼리는 대소비교가 안이루어진 상태라 아래의 recursion 과정이 필요하다.
        quick_sort(smaller_items)
        quick_sort(larger_items)
        items[:] = smaller_items + [items[pivot_index]] + larger_items
    # print(items)
quick_sort(container)
for i in container:
    print(i)