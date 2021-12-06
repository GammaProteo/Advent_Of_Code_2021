with open('Data/Power.data') as f:  # loading txt file from data, reading each line
    reading = f.read().splitlines()
    f.close()

oxygen = str()
carbondioxide = str()
x = 0
z = 0

work_ox = reading.copy()  # copies list reading into new lists
work_carb = reading.copy()
count_0 = 0
count_1 = 0

tmp1 = len(work_ox[0])
while x < tmp1:
    for item in work_ox:
        if int(item[x]) == 0:
            count_0 += 1
        else:
            count_1 += 1
    if count_0 > count_1:
        work_ox = [item for item in work_ox if item[x] == '0']
    else:
        work_ox = [item for item in work_ox if item[x] == '1']
    count_0 = 0
    count_1 = 0
    x += 1

tmp2 = len(work_carb[0])
while z < tmp2:
    if len(work_carb) == 1:
        break
    for item in work_carb:
        if int(item[z]) == 0:
            count_0 += 1
        else:
            count_1 += 1
    if count_0 > count_1:
        work_carb = [item for item in work_carb if item[z] == '1']
    else:
        work_carb = [item for item in work_carb if item[z] == '0']
    count_0 = 0
    count_1 = 0
    z += 1

print(int(str(work_ox[0]), 2) * int(str(work_carb[0]), 2))
