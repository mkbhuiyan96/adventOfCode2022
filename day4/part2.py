import re

def main():
    file = open("input.txt", "r")
    count = 0

    for line in file:
        if overlap(re.split("[-,]", line)):
            count += 1

    print(count)
    
    
def overlap(nums):
    nums = list(map(int, nums))
    
    if nums[1] >= nums[2] and nums[1] <= nums[3]:
        return True
    if nums[3] >= nums[0] and nums[3] <= nums[1]:
        return True
    return False

if __name__ == "__main__":
   main()