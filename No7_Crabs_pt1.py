from numpy import median

with open('Data/Crabs.data') as f:  # loading txt file from data, reading each line
    temp_cords = f.read().split(',')
    f.close()

# crab_cords = []
# for crab in range(0, len(temp_cords)):
#     crab_cords.append(int(temp_cords[crab]))

crab_cords = [int(x) for x in temp_cords]  # pitonic vej # fagt pycha # tvoje mama
middle_crab = int(median(crab_cords))
fuel = 0
for crab in crab_cords:
    fuel += abs(crab - middle_crab)

print(crab_cords)
print(int(middle_crab))
print(fuel)
