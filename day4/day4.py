import re

def main():
    sum_fully_contained = 0
    sum_overlaps = 0
    
    file = open("input.txt", "r")
    for line in file:
        nums = list(map(int, re.split("[-,]", line)))
        if fully_contained(nums):
            sum_fully_contained += 1
        if overlap(nums):
            sum_overlaps += 1
    file.close()
    
    print("There are", sum_fully_contained, "ranges that fully contain another")
    print("There are", sum_overlaps, "ranges that overlap")
    
def overlap(nums):    
    if nums[1] >= nums[2] and nums[1] <= nums[3]:
        return True
    if nums[3] >= nums[0] and nums[3] <= nums[1]:
        return True
    return False

def fully_contained(nums):    
    if nums[0] >= nums[2] and nums[1] <= nums[3]:
        return True
    if nums[2] >= nums[0] and nums[3] <= nums[1]:
        return True
    return False

if __name__ == "__main__":
   main()