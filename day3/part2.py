file = open("input.txt", "r")

dict = {}
total = 0
lineNumber = 0

for line in file:
    lineNumber += 1
    if lineNumber == 4:
        dict.clear()
        lineNumber = 1
        
    for char in line:
        if lineNumber == 1 or dict.get(char) == lineNumber - 1:
            dict[char] = lineNumber
        if dict.get(char) == 3:
            if char.isupper():
                total += ord(char) - 38
            else:
                total += ord(char) - 96
            break

print(total)