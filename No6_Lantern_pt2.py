with open('Data/Lantern.data') as f:  # loading txt file from data, reading each line
    work_Fishes = f.read().split(',')  # fishus je list se str hodnotou
    f.close()

good_Fish = []  # fishes je list s int hodnotou z fishus, preklada se nize
for fish in range(0, len(work_Fishes)):
    good_Fish.append(int(work_Fishes[fish]))

generace = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # list prvku sum?cu
for i in range(0, len(good_Fish)):
    generace[good_Fish[i]] += 1

generace_mezikrok = [0 for x in range(len(generace))]  # pomocny list pro zapisovani mezikroku iterace

# for x in range(len(lyst)):  # does the same as the above code
#         list.append(0)

for days in range(0, 256):
    for j in range(len(generace) - 1, -1, -1):
        if j == 0:
            generace_mezikrok[6] = generace_mezikrok[6] + generace[j]
            generace_mezikrok[8] = generace_mezikrok[8] + generace[j]
        else:
            generace_mezikrok[j - 1] = generace[j]

    generace = generace_mezikrok.copy()
    generace_mezikrok = [0 for x in range(len(generace))]

# # print(fishes, ' a ', len(fishes))
print(generace)

suma = 0
for krok in generace:
    suma = suma + krok
print(suma)

