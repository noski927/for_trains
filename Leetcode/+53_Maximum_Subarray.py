# Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

# nums = [-2,1,-3,4,-1,2,1,-5,4]



# def maxSubArray(nums):
#     num_lists = []

#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             list_nums = nums[j:i]
#             num_lists.append(list_nums)
#     a = list(map(lambda x: sum(x), num_lists))
#     a.sort(reverse=True)
#     return a[0]

# maxSubArray(nums)


nums = [5,4,-1,7,8]

def maxSubArray(nums: list[int]) -> int: # Kadane’s Algorithm
    n = len(nums)
    maxsum = sum(nums)
    cursum = 0
    for i in range(0, n):
        cursum = cursum + nums[i]
        if (cursum > maxsum):
            maxsum = cursum
        if (cursum < 0):
            cursum = 0
    return maxsum





    

