from typing import List


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        res = 0
        cover = 0
        tiles.sort(key=lambda x: x[0])
        left_idx = 0

        # 右进左出
        for tl, tr, c in tiles:
            cover += (tr - tl + 1) * c
            while tiles[left_idx][1] < tr - carpetLen + 1:
                cover -= (tiles[left_idx][1] - tiles[left_idx][0] + 1) * tiles[
                    left_idx
                ][2]
                left_idx += 1
            uncover = max(
                0, (tr - carpetLen + 1 - tiles[left_idx][0]) * tiles[left_idx][2]
            )
            res = max(res, cover - uncover)

        return res

    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort(key=lambda c: c[0])
        ans = self.maximumWhiteTiles(coins, k)

        coins.reverse()
        for t in coins:
            t[0], t[1] = -t[1], -t[0]
        return max(ans, self.maximumWhiteTiles(coins, k))
