class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """
        total_dis = 0
        while mainTank:
            remainTank = mainTank % 5
            if mainTank >= 5:
                cnt = mainTank // 5
                total_dis += 50 * cnt
                while additionalTank and cnt:
                    additionalTank -= 1
                    cnt -= 1
                    remainTank += 1
            else:
                total_dis += 10 * remainTank
                remainTank = 0
            mainTank = remainTank

        return total_dis
