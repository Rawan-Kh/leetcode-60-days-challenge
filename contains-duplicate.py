class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        setlist =set(nums)
        normalist = nums
        if ( len(setlist) ==  len(normalist)):
            return False
        else:
            return True
