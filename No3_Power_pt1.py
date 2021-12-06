with open('Data/Power.data') as f:  # loading txt file from data, reading each line
    reading = f.read().splitlines()
    f.close()

gamma = str()
epsilon = str()
consumption = 0

count_0 = 0
count_1 = 0

for x in range(len(reading[0])):
    for y in range(len(reading)):
        if int(reading[y][x]) == 0:
            count_0 += 1
        else:
            count_1 += 1
    if count_0 > count_1:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
    count_0 = 0
    count_1 = 0

consumption = int(gamma, 2) * int(epsilon, 2)
print(gamma, epsilon)
print(consumption)
