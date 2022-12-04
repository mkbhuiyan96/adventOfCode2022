file = open("input.txt", "r")
highest = 0
total = 0

for line in file:
    if line.strip() != "":
        total += int(line)
    else:
        highest = max(highest, total)
        total = 0
        
print(highest)