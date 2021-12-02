with open('Data/Swim.data') as f:  # loading txt file from data, reading each line
    cords = f.read().splitlines()
    f.close()

horizontal = 0
vertical = 0
final = 0

for i in cords:
    x = i.split(" ")
    if x[0] == "up":
        vertical = vertical - int(x[1])  # up X decreases the depth by X units
    elif x[0] == "down":
        vertical = vertical + int(x[1])  # down X increases the depth by X units.
    elif x[0] == "forward":
        horizontal = horizontal + int(x[1])

final = vertical * horizontal
print("Horisontal position is ", horizontal, ", vertical is ", vertical,". The final result is ", final)
