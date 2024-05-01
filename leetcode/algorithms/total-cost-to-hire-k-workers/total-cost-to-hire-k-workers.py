import heapq


class Solution(object):
    def totalCost(self, costs, k, candidates):
        # 使用两个堆一个维护前面的，一个维护后面的最小cost

        # 如果元素不足，则不能使用下面的堆，两个堆中有重复元素
        if candidates * 2 + k > len(costs):
            costs.sort()
            return sum(costs[:k])

        begin_heap = costs[:candidates]
        last_heap = costs[-candidates:]
        heapq.heapify(begin_heap)
        heapq.heapify(last_heap)
        res = 0

        i = candidates
        j = len(costs) - 1 - candidates
        for _ in range(k):
            if begin_heap[0] <= last_heap[0]:
                res += heapq.heapreplace(begin_heap, costs[i])
                i += 1
            else:
                res += heapq.heapreplace(last_heap, costs[j])
                j -= 1

        return res

    def totalCost1(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        # 模拟
        total_cost = 0
        while k:
            workers = [(costs[i], i) for i in range(0, min(len(costs), candidates))] + [
                (costs[i], i)
                for i in range(len(costs) - 1, max(len(costs) - candidates - 1, 0), -1)
            ]
            workers.sort()
            total_cost += workers[0][0]
            costs.pop(workers[0][1])
            k -= 1
        return total_cost


print(
    Solution().totalCost(
        [31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58], 11, 2
    )
)
