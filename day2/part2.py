file = open("input.txt", "r")
LOOKUP = [(3,4,8), (1,5,9), (2,6,7)]
score = 0

for line in file:
    theirValue = ord(line[0]) - ord('A')    
    myValue = ord(line[2]) - ord('X')
    
    score += LOOKUP[theirValue % 3][myValue % 3]
    
print(score)