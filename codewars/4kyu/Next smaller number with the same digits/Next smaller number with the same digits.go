package kata

import (
	"sort"
	"strconv"
	"strings"
)

func NextSmaller(n int) int {
	// Your code here
	digits := strings.Split(strconv.Itoa(n), "")
	// 1. find the first index i from the right where digits[i] > digits[i+1]
	i := len(digits) - 2
	for i >= 0 && digits[i] <= digits[i+1] {
		i -= 1
	}

	if i == -1 {
		return -1
	}
	// 2. find the largest index j from the right where digits[j] < digits[i]
	j := len(digits) - 1
	for j > i && digits[j] >= digits[i] {
		j -= 1
	}

	// 3. swap
	digits[i], digits[j] = digits[j], digits[i]

	// 4. sorted desc digits[i+1:]
	sort.Slice(digits[i+1:], func(a, b int) bool {
		return digits[i+1+a] > digits[i+1+b]
	})

	res, _ := strconv.Atoi(strings.Join(digits, ""))

	// check zero leading
	if len(strconv.Itoa(res)) != len(digits) {
		return -1
	}

	return res
}
