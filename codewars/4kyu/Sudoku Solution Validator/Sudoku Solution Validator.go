package main

func ValidateSolution(m [][]int) bool {
	// check row
	for i := 0; i < 9; i++ {
		mm := make(map[int]bool)
		for j := 0; j < 9; j++ {
			if m[i][j] == 0 {
				continue
			}
			if _, ok := mm[m[i][j]]; ok {
				return false
			}
			mm[m[i][j]] = true
		}
	}
	// check col
	for j := 0; j < 9; j++ {
		mm := make(map[int]bool)
		for i := 0; i < 9; i++ {
			if m[i][j] == 0 {
				continue
			}
			if _, ok := mm[m[i][j]]; ok {
				return false
			}
			mm[m[i][j]] = true
		}
	}
	// check 3*3
	for i := 0; i < 9; i += 3 {
		for j := 0; j < 9; j += 3 {
			mm := make(map[int]bool)
			for k := 0; k < 3; k++ {
				for kk := 0; kk < 3; kk++ {
					if m[i+k][j+kk] == 0 {
						continue
					}
					if _, ok := mm[m[i+k][j+kk]]; ok {
						return false
					}
					mm[m[i+k][j+kk]] = true
				}
			}
		}
	}
	return true
}
