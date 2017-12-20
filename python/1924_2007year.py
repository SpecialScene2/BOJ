Day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

Date = input().split(' ')
Month = int(Date[0])
Day2 = int(Date[1])

if Month == 1 or Month == 10:
    if Day2 % 7 == 1:
        print(Day[1])
    elif Day2 % 7 == 2:
        print(Day[2])
    elif Day2 % 7 == 3:
        print(Day[3])
    elif Day2 % 7 == 4:
        print(Day[4])
    elif Day2 % 7 == 5:
        print(Day[5])
    elif Day2 % 7 == 6:
        print(Day[6])
    elif Day2 % 7 == 0:
        print(Day[0])

elif Month == 2 or Month == 3 or Month == 11:
    if Day2 % 7 == 1:
        print(Day[4])
    elif Day2 % 7 == 2:
        print(Day[5])
    elif Day2 % 7 == 3:
        print(Day[6])
    elif Day2 % 7 == 4:
        print(Day[0])
    elif Day2 % 7 == 5:
        print(Day[1])
    elif Day2 % 7 == 6:
        print(Day[2])
    elif Day2 % 7 == 0:
        print(Day[3])

elif Month == 4 or Month == 7:
    if Day2 % 7 == 1:
        print(Day[0])
    elif Day2 % 7 == 2:
        print(Day[1])
    elif Day2 % 7 == 3:
        print(Day[2])
    elif Day2 % 7 == 4:
        print(Day[3])
    elif Day2 % 7 == 5:
        print(Day[4])
    elif Day2 % 7 == 6:
        print(Day[5])
    elif Day2 % 7 == 0:
        print(Day[6])

elif Month == 5 :
    if Day2 % 7 == 1:
        print(Day[2])
    elif Day2 % 7 == 2:
        print(Day[3])
    elif Day2 % 7 == 3:
        print(Day[4])
    elif Day2 % 7 == 4:
        print(Day[5])
    elif Day2 % 7 == 5:
        print(Day[6])
    elif Day2 % 7 == 6:
        print(Day[0])
    elif Day2 % 7 == 0:
        print(Day[1])

elif Month == 6 :
    if Day2 % 7 == 1:
        print(Day[5])
    elif Day2 % 7 == 2:
        print(Day[6])
    elif Day2 % 7 == 3:
        print(Day[0])
    elif Day2 % 7 == 4:
        print(Day[1])
    elif Day2 % 7 == 5:
        print(Day[2])
    elif Day2 % 7 == 6:
        print(Day[3])
    elif Day2 % 7 == 0:
        print(Day[4])

elif Month == 8 :
    if Day2 % 7 == 1:
        print(Day[3])
    elif Day2 % 7 == 2:
        print(Day[4])
    elif Day2 % 7 == 3:
        print(Day[5])
    elif Day2 % 7 == 4:
        print(Day[6])
    elif Day2 % 7 == 5:
        print(Day[0])
    elif Day2 % 7 == 6:
        print(Day[1])
    elif Day2 % 7 == 0:
        print(Day[2])

elif Month == 9 or Month == 12:
    if Day2 % 7 == 1:
        print(Day[6])
    elif Day2 % 7 == 2:
        print(Day[0])
    elif Day2 % 7 == 3:
        print(Day[1])
    elif Day2 % 7 == 4:
        print(Day[2])
    elif Day2 % 7 == 5:
        print(Day[3])
    elif Day2 % 7 == 6:
        print(Day[4])
    elif Day2 % 7 == 0:
        print(Day[5])

