file = open("input.txt", "r")

dict = {}
total = 0

for line in file:
    dict.clear()
    firstHalf = line[:len(line)//2]
    secondHalf = line[len(line)//2:]
    
    for char in firstHalf:
        dict[char] = 1
    for char in secondHalf:
        if dict.get(char) == 1:
            if char.isupper():
                total += ord(char) - 38
            else:
                total += ord(char) - 96
            dict[char] = 0

print(total)