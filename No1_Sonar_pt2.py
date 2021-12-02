with open('Data/SonarSweep.data') as f:  # loading txt file from data, reading each line
    lines = f.readlines()
    f.close()  # returns lists with lines with /n

for i in range(len(lines)):  # deletes /n from string during int translation
    lines[i] = int(lines[i])

prev_mes = 0
curr_mes = 0
num_inc = 0

for i in range(len(lines)-3):
    prev_mes = lines[0+i] + lines[1+i] + lines[2+i]
    curr_mes = lines[1+i] + lines[2+i] + lines[3+i]
    if prev_mes < curr_mes:
        num_inc += 1

print(num_inc)
