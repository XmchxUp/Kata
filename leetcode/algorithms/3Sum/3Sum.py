class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        sorted_nums = sorted(nums)
        for i in range(0, n - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                tmp_sum = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                if tmp_sum == 0:
                    res.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    j += 1
                    while j < k and sorted_nums[j] == sorted_nums[j - 1]:
                        j += 1
                elif tmp_sum < 0:
                    j += 1
                else:
                    k -= 1
        return res
