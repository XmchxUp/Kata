package main

import "fmt"

// https://www.youtube.com/watch?v=Ww3HbHMnJ5g&t=4s

// Tips & Tricks
// a. Start with "1" Clues - those must be the tallest Skyscrapers.
// b. Then go to the largest clues. A clue of N (the greatest digit) is easily filled.
// C. Any clue of N-1 means you can put the Nth digit in the last or second to last cell.
// d. Use 'sudoku' like scanning of numbers across rows/columns
// e. Any clue > 2 you can 'x' out N and N-1 in the front
type clueDirInfo struct {
	isCheckRow bool
	start      int
	end        int
	step       int
}

var n = 6
var clues = []int{3, 2, 2, 3, 2, 1,
	1, 2, 3, 3, 2, 2,
	5, 1, 2, 2, 4, 3,
	3, 2, 1, 2, 2, 4}

var clueDirInfos = []clueDirInfo{
	{isCheckRow: false, start: 0, end: n, step: 1},
	{isCheckRow: true, start: n - 1, end: -1, step: -1},
	{isCheckRow: false, start: n - 1, end: -1, step: -1},
	{isCheckRow: true, start: 0, end: n, step: 1},
}

var possibleValues [][][]bool
var rowBitMaps, colBitMaps []BitMap

type BitMap uint32

func (b *BitMap) Set(key int, value bool) {
	if value {
		*b = *b | (1 << key)
	} else {
		*b = *b & (^(1 << key))
	}
}

func (b *BitMap) HasKey(key int) bool {
	return (*b & (1 << key)) != 0
}

func canPlace(row, col, height int) bool {
	return !(rowBitMaps[row].HasKey(height) || colBitMaps[col].HasKey(height))
}

func getClueInfo(idx int) clueDirInfo {
	if idx < n {
		return clueDirInfos[0]
	} else if idx < 2*n {
		return clueDirInfos[1]
	} else if idx < 3*n {
		return clueDirInfos[2]
	} else {
		return clueDirInfos[3]
	}
}

func getChangedIdx(idx int, info clueDirInfo) int {
	idx %= n
	if (info.step == 1 && info.isCheckRow) || (info.step == -1 && !info.isCheckRow) {
		idx = n - 1 - idx
	}
	return idx
}

func getCount(grid [][]int, idx int) int {
	prevMaxHeight := 0
	cnt := 0
	info := getClueInfo(idx)

	getGridValue := func(idx, i int) int {
		if info.isCheckRow {
			return grid[idx][i]
		} else {
			return grid[i][idx]
		}
	}

	idx = getChangedIdx(idx, info)

	for i := info.start; i != info.end; i += info.step {
		val := getGridValue(idx, i)
		if val == n {
			cnt += 1
			break
		}

		if val > prevMaxHeight {
			prevMaxHeight = val
			cnt += 1
		}
	}

	return cnt
}

func isValidate(grid [][]int, clues []int, row, col int, fullCheck bool) bool {
	relativeCluesIdx := []int{
		col, 6 + row, 17 - col, 23 - row,
	}

	for idx, clue := range clues {
		if clue == 0 {
			continue
		}

		if !fullCheck {
			if idx != relativeCluesIdx[0] || idx != relativeCluesIdx[1] || idx != relativeCluesIdx[2] || idx != relativeCluesIdx[3] {
				continue
			}
		}

		if clue != getCount(grid, idx) {
			return false
		}
	}

	return true

}

func dfs(grid [][]int, clues []int, row, col int) bool {
	if row == n {
		return isValidate(grid, clues, row, col, true)
	}

	nextRow, nextCol := row, col+1
	if nextCol == n {
		nextRow++
		nextCol = 0
	}

	if grid[row][col] != 0 {
		return dfs(grid, clues, nextRow, nextCol)
	}

	for height, isOk := range possibleValues[row][col] {
		if !isOk || height == 0 {
			continue
		}

		if canPlace(row, col, height) {
			grid[row][col] = height
			updateState(row, col, height, false)

			if row != nextRow || col+1 != nextCol {
				if !isValidate(grid, clues, row, col, false) {
					grid[row][col] = 0
					updateState(row, col, height, true)
					continue
				}
			}

			if dfs(grid, clues, nextRow, nextCol) {
				return true
			}

			grid[row][col] = 0
			updateState(row, col, height, true)
		}
	}

	return false
}

func updateState(row, col, height int, canUseHeight bool) {
	rowBitMaps[row].Set(height, !canUseHeight)
	colBitMaps[col].Set(height, !canUseHeight)
	for k := 0; k < n; k++ {
		possibleValues[k][col][height] = canUseHeight
		possibleValues[row][k][height] = canUseHeight
	}
}

func preprocess(grid [][]int, clues []int) {
	rowBitMaps = make([]BitMap, n)
	colBitMaps = make([]BitMap, n)

	possibleValues = make([][][]bool, n)
	for i := range possibleValues {
		possibleValues[i] = make([][]bool, n)
		for j := range possibleValues[i] {
			possibleValues[i][j] = make([]bool, n+1)
			for k := range possibleValues[i][j] {
				possibleValues[i][j][k] = true
			}
		}
	}

	for i, clue := range clues {
		info := getClueInfo(i)
		idx := getChangedIdx(i, info)

		if clue == 1 {
			if info.isCheckRow {
				grid[idx][info.start] = n
			} else {
				grid[info.start][idx] = n
			}
		} else if clue == n {
			v := 1
			for j := info.start; j != info.end; j += info.step {
				if info.isCheckRow {
					grid[idx][j] = v
				} else {
					grid[j][idx] = v
				}
				v++
			}
		} else if clue == n-1 {
			for j := info.start; j != info.end-info.step*2; j += info.step {
				if info.isCheckRow {
					possibleValues[idx][j][n] = false
				} else {
					possibleValues[j][idx][n] = false
				}
			}
		} else if clue > 2 {
			for j := info.start; j != info.start+info.step*(clue-1); j += info.step {
				if info.isCheckRow {
					possibleValues[idx][j][n] = false
					possibleValues[idx][j][n-1] = false
				} else {
					possibleValues[j][idx][n] = false
					possibleValues[j][idx][n-1] = false
				}
			}
		} else if clue == 2 {
			if info.isCheckRow {
				possibleValues[idx][info.start][n] = false
			} else {
				possibleValues[info.start][idx][n] = false
			}
		}
	}

	for i := range grid {
		for j := range grid[i] {
			if grid[i][j] != 0 {
				updateState(i, j, grid[i][j], false)
			}
		}
	}
}

func SolvePuzzle(clues []int) [][]int {
	grid := make([][]int, n)
	for i := range grid {
		grid[i] = make([]int, n)
	}

	preprocess(grid, clues)

	dfs(grid, clues, 0, 0)
	return grid
}

func main() {
	fmt.Println(SolvePuzzle(clues))
	clues = []int{0, 0, 0, 2, 2, 0, 0, 0, 0, 6, 3, 0, 0, 4, 0, 0, 0, 0, 4, 4, 0, 3, 0, 0}
	fmt.Println(SolvePuzzle(clues))
	clues = []int{0, 3, 0, 5, 3, 4, 0, 0, 0, 0, 0, 1, 0, 3, 0, 3, 2, 3, 3, 2, 0, 3, 1, 0}
	fmt.Println(SolvePuzzle(clues))
}
