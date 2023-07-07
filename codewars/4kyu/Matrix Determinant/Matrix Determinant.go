package main

import "fmt"

func Determinant(matrix [][]int) int {
	var result int
	n := len(matrix)
	if n == 1 {
		return matrix[0][0]
	}
	sign := 1
	for i := 0; i < n; i++ {
		result += sign * matrix[0][i] * Determinant(createSubMatrix(matrix, i))
		sign *= -1
	}
	return result
}

func createSubMatrix(matrix [][]int, col int) [][]int {
	subMatrix := make([][]int, len(matrix)-1)
	for i := 1; i < len(matrix); i++ {
		subMatrix[i-1] = append([]int{}, matrix[i][:col]...)
		subMatrix[i-1] = append(subMatrix[i-1], matrix[i][col+1:]...)
	}
	return subMatrix
}

func main() {
	fmt.Println((Determinant([][]int{{1}})))
	fmt.Println(Determinant([][]int{{1, 3}, {2, 5}}))
	fmt.Println(Determinant([][]int{{2, 5, 3}, {1, -2, -1}, {1, 3, 4}}))
}
