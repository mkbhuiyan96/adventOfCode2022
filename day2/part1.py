file = open("input.txt", "r")
score = 0

for line in file:
    theirValue = ord(line[0]) - ord('A')
    myValue = ord(line[2]) - ord('X')
    
    score += myValue + 1
    if (theirValue - myValue) % 3 == 2:
        score += 6
    elif (theirValue - myValue) % 3 == 0:
        score += 3

print(score)