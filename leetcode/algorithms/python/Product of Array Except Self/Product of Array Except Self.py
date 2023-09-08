class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # ans[i] = A[0]*A[1]*A[i-1]*A[i+1]*A[n-1]
        ans = [1] * len(nums)
        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1]
        tmp = 1
        for i in range(len(nums) - 2, -1, -1):
            tmp *= nums[i + 1]
            ans[i] *= tmp
        return ans
