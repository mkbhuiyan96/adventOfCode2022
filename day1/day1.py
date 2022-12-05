def main():
    calorie_list = []
    sum_calories = 0
    
    with open("input.txt") as file:
        for line in file:
            if line.strip() != "":
                sum_calories += int(line)
            else:
                calorie_list.append(sum_calories)
                sum_calories = 0
    
    calorie_list = sorted(calorie_list, reverse=True)
    print("The most calories carried is:", calorie_list[0], "calories")
    print("The 3 elves carrying the most calories are holding:", sum(calorie_list[:3]))
            
if __name__ == "__main__":
    main()