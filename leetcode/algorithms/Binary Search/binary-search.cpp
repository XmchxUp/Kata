class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (hi - lo) // 2 + lo
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid
            else:
                lo = mid + 1
        return -1