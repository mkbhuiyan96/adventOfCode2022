def main():
    rock_paper_scissors = [(4,8,3), (1,5,9), (7,2,6)]
    lose_draw_win = [(3,4,8), (1,5,9), (2,6,7)]
    part_1_total = 0
    part_2_total = 0
    
    file = open("input.txt", "r")
    for line in file:
        opponent_value = ord(line[0]) - ord('A')
        my_value = ord(line[2]) - ord('X')
        part_1_total += rock_paper_scissors[opponent_value % 3][my_value % 3]
        part_2_total += lose_draw_win[opponent_value % 3][my_value % 3]
    file.close()
    
    print("Part 1 total:", part_1_total)
    print("Part 2 total:", part_2_total)
    
if __name__ == "__main__":
    main()