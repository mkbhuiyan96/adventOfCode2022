from copy import deepcopy

def main():
    data = []
    instructions = []
    with open("input.txt") as file:
        for i, line in enumerate(file):
            if i < 8:
                for j, char in enumerate(line):
                    if(j%4 == 1):
                        data.append(char)
            elif i > 9:
                instructions.append([int(j) for j in line.split() if j.isdigit()])
    
    stacks = []
    for i in range(9):
        stacks.append([]) # Create a list of lists
    for i, element in enumerate(data):
        if element != " ":
            stacks[i%9].append(element) # Create the "veritcal" stacks from 1D list
    
    part1_config = move_boxes_individually(stacks, instructions)
    part2_config = move_boxes_together(stacks, instructions)
    
    print("Indivually moving boxes gives us these on top: ", *part1_config[0], sep="")
    print("Moving them together gives us these on top: ", *part2_config[0], sep="")
    
        
def move_boxes_individually(stacks, instructions):
    stacks = deepcopy(stacks)
    for steps in instructions:
        for i in range(steps[0]):
            temp = stacks[steps[1] - 1].pop(0)
            stacks[steps[2] - 1].insert(0, temp)
    return stacks
    
def move_boxes_together(stacks, instructions):
    stacks = deepcopy(stacks)
    for steps in instructions:
        for i in range(steps[0])[::-1]:
            temp = stacks[steps[1] - 1].pop(i)
            stacks[steps[2] - 1].insert(0, temp)
    return stacks
              
if __name__ == "__main__":
    main()