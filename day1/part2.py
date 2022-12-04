file = open("input.txt", "r")
totalList = []
total = 0

for line in file:
    if line.strip() != "":
        total += int(line)
    else:
        totalList.append(total)
        total = 0
        
print(sum(sorted(totalList)[-3:]))