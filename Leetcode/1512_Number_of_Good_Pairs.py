'''
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Input: nums = [1,2,3,1,1,3]
Output: 4
'''


def numIdenticalPairs(nums):
    count = {}
    for num in nums:
        count.update({num: nums.count(num)})

    total = 0
    for val in count.values():
        total += ((val * (val - 1)) // 2)
    return total
