package main

import (
	"fmt"
	"sort"
)

func MakeValley(arr []int) []int {
	// your code
	sort.Ints(arr)
	n := len(arr)

	res := make([]int, n)
	mid := n / 2
	res[mid] = arr[0]
	idx := 0
	i := n - 1
	for k := 0; k < mid; k++ {
		res[idx] = arr[i]
		res[n-idx-1] = arr[i-1]
		i -= 2
		idx += 2
	}
	return res
}

func main() {
	fmt.Println(MakeValley([]int{20, 7, 6, 2}))
}
