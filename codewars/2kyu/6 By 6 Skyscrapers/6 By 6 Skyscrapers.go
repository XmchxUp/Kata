package main

import "fmt"

func SolvePuzzle(clues []int) [][]int {
	// Return 6x6 matrix here ...
	n := 6
	grid := make([][]int, n)
	for i := range grid {
		grid[i] = make([]int, n)
	}

	canPlace := func(row, col, height int) bool {
		if grid[row][col] != 0 {
			return false
		}

		for i := 0; i < n; i++ {
			if grid[row][i] == height && i != col {
				return false
			}
			if grid[i][col] == height && i != row {
				return false
			}
		}
		return true
	}

	type clueInfo struct {
		isCheckRow bool
		start      int
		end        int
		step       int
	}

	dirs := []clueInfo{
		{isCheckRow: false, start: 0, end: n, step: 1},
		{isCheckRow: true, start: n - 1, end: -1, step: -1},
		{isCheckRow: false, start: n - 1, end: -1, step: -1},
		{isCheckRow: true, start: 0, end: n, step: 1},
	}

	isValidate := func() bool {
		for idx, clue := range clues {

			if clue == 0 {
				continue
			}

			dir := idx / n
			info := dirs[dir]
			prevMaxHeight := 0
			idx %= n

			if info.isCheckRow {
				if info.step == 1 {
					idx = n - 1 - idx
				}
				for i := info.start; i != info.end; i += info.step {
					if grid[idx][i] == n {
						clue--
						break
					}
					if grid[idx][i] > prevMaxHeight {
						prevMaxHeight = grid[idx][i]
						clue--
					}
				}
			} else {
				if info.step == -1 {
					idx = n - 1 - idx
				}
				for j := info.start; j != info.end; j += info.step {
					if grid[j][idx] == n {
						clue--
						break
					}
					if grid[j][idx] > prevMaxHeight {
						clue--
						prevMaxHeight = grid[j][idx]
					}
				}
			}

			if clue != 0 {
				return false
			}
		}

		return true
	}

	var helper func(row, col int) bool
	helper = func(row, col int) bool {
		if row == n {
			fmt.Println(grid)
			return isValidate()
		}

		nextRow, nextCol := row, col+1
		if nextCol == n {
			nextRow++
			nextCol = 0
		}

		for height := 1; height <= n; height++ {
			if canPlace(row, col, height) {
				grid[row][col] = height
				if helper(nextRow, nextCol) {
					return true
				}
				grid[row][col] = 0
			}
		}

		return false
	}

	helper(0, 0)
	return grid
}

func main() {
	var clues = []int{3, 2, 2, 3, 2, 1,
		1, 2, 3, 3, 2, 2,
		5, 1, 2, 2, 4, 3,
		3, 2, 1, 2, 2, 4}
	fmt.Print(SolvePuzzle(clues))
}
