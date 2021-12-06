with open('Data/Bingo.data') as f:  # loading txt file from data, reading each line
    commands = f.readline().strip().split(",")
    f.readline()  # getting rid of one whitespace
    bingo_raw = f.read().splitlines()
    f.close()

bingo = list()
card = list()

for item in bingo_raw:
    if item == "":
        bingo.append(card)
        card = list()
    else:
        item = [int(x) for x in item.split(" ") if x != ""]
        card.append(item)

bingo.append(card)

commands = [int(x) for x in commands]
bingo_len = len(bingo)

for x in bingo:
    for y in x:
        print(y)
    print(" ")


for com in commands:
    for card in range(bingo_len):
        pass
