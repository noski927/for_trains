'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
'''
nums = [8,1,2,2,3]


def smallerNumbersThanCurrent(nums):
    a = []
    for i in nums:
        st = len(list(filter(lambda x :x<i ,nums)))
        a.append(st)
    return a

print(smallerNumbersThanCurrent(nums))

