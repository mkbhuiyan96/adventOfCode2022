def main():
    compartment_sum = 0
    badge_sum = 0
    group_of_3 = []
    
    file = open("input.txt", "r")
    for i, line in enumerate(file):
        compartments = []
        compartments.extend([line[:len(line)//2], line[len(line)//2:]])
        compartment_sum += common_component(compartments)
        
        group_of_3.append(line.strip())
        if(i%3 == 2):
            badge_sum += common_component(group_of_3)
            group_of_3.clear()
    file.close()
    
    print("The sum of the common items in both compartments is:", compartment_sum)
    print("The sum of the badges between every 3 elves is:", badge_sum)

def common_component(rucksack):
    common_char = set.intersection(*map(set,rucksack))
    common_char = common_char.pop()
    
    if common_char.isupper():
        return ord(common_char) - 38
    else:
        return ord(common_char) - 96

if __name__ == "__main__":
    main()