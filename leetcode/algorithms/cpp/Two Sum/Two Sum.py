class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for i in range(len(nums)):
            another = target - nums[i]
            if another in m:
                return [i, m[another]]
            else:
                m[nums[i]] = i
        return [-1, -1]
