with open('Data/SonarSweep.data') as f: #loading txt file from data, reading each line
    lines = f.readlines()
    f.close()

prev_mes = int(lines[0])
num_inc = 0

for i in lines:
    if prev_mes < int(i):
        num_inc += 1
    prev_mes = int(i)

print(num_inc)








