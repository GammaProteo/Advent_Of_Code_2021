with open('Data/Swim.data') as f:  # loading txt file from data, reading each line
    cords = f.read().splitlines()
    f.close()

horizontal = 0
vertical = 0  # up X decreases the depth by X units, down X increases the depth by X units.
aim = 0  # up and down, down X increases your aim by X units, up X decreases your aim by X units.

final = 0

for i in cords:
    x = i.split(" ")
    if x[0] == "up":
        aim = aim - int(x[1])
    elif x[0] == "down":
        aim = aim + int(x[1])
    elif x[0] == "forward":
        horizontal = horizontal + int(x[1])
        vertical = vertical + (aim * int(x[1]))

final = vertical * horizontal
print("Horizontal position is ", horizontal, ", vertical is ", vertical, ", aim is ", aim, ".")
print("The final result is ", final, ".")
