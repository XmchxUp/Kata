class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = set()
        for num in nums:
            if num in m:
                return True
            m.add(num)
        return False
