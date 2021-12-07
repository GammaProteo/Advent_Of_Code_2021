import sys

with open('Data/Crabs.data') as f:  # loading txt file from data, reading each line
    temp_cords = f.read().split(',')
    f.close()

# crab_cords = []
# for crab in range(0, len(temp_cords)):
#     crab_cords.append(int(temp_cords[crab]))

crab_cords = [int(x) for x in temp_cords]  # pitonic vej # fagt pycha # tvoje mama
fuel = 0
min_fuel = sys.maxsize
max_crab = max(crab_cords)

for step in range(0, max_crab):
    for crab in crab_cords:
        fuel += ((abs(crab - step) ** 2 + abs(crab - step)) // 2)  # Pascaluv triangl (triangular number),
                                                                   # vypocet rozvoje pro n-ty krok + spotreba paliva
                                                                   # ** - na druhou, // celociselne deleni
    if fuel < min_fuel:
        min_fuel = fuel
    fuel = 0

print(crab_cords)
print(min_fuel)
