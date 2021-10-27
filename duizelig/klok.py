i = [1,1,1]

while i[0] < 3:
    while i[1] < 13:
        print(str(i[1])+'AM')
        i[1] += 1
    while i[2] < 13:
        print(str(i[2])+'PM')
        i[2] += 1
    i[0] += 1