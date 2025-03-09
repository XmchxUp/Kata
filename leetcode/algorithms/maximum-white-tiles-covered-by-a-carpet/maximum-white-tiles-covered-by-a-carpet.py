from typing import List


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        res = 0
        cover = 0
        tiles.sort(key=lambda x: x[0])
        left_idx = 0

        # 右进左出
        for tl, tr in tiles:
            cover += tr - tl + 1
            while tiles[left_idx][1] < tr - carpetLen + 1:
                cover -= tiles[left_idx][1] - tiles[left_idx][0] + 1
                left_idx += 1
            uncover = max(0, tr - carpetLen + 1 - tiles[left_idx][0])
            res = max(res, cover - uncover)

        return res
