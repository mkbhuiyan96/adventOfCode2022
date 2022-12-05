def main():
    data = []
    with open("input.txt") as file:
        for i, line in enumerate(file):
            if i < 8:
                for j, char in enumerate(line):
                    if(j%4 == 1):
                        data.append(char)
    
    list = []
    for i in range(9):
        list.append([])
    for i, element in enumerate(data):
        if element != " ":
            list[i%9].append(element)
    
    for i in list:
        print(i)
    
if __name__ == "__main__":
    main()