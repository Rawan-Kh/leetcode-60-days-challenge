#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and "you may not use the same element twice".

#that's correct if we used the same elem twice
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement_map = {}
        for i, num in enumerate(nums):
            for j, num in enumerate(nums):
                if (nums[i] + nums[j]) == target:
                    return (i , j)
