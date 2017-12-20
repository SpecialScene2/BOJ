M, N = map(int, input().split(' '))

Map = []
for i in range(map_row):
    element = map(int, input().split(' '))
    Map.append(list(element))

container = {}
container[1] = [(0,0)]

def findWay(Number):
    coord = container[Number-1]
    possibleCoord = []
    for i in coord:
        possibleCoord.append(set(i[0] + 1,i[1]))
        possibleCoord.append(set(i[0] - 1, i[1]))
        possibleCoord.append(set(i[0] , i[1] + 1))
        possibleCoord.append(set(i[0] , i[1] + 1))
    possibleCoord = set(possibleCoord)
    if Map[coord[0]][coord[1]] > Map[coord[0]+1][coord[1]]:
        container[2] = [(coord[0]+1, coord[1])]
        if Map[coordinate[0]+1][coordinate[1]+1] < Map[coordinate[0]][coordinate[1]]:

    # container[Number] =


# for i in range(2, M*N+1):
#     findWay(i)