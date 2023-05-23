package main

import (
	"fmt"
	"math"
)

// https://zh.wikipedia.org/wiki/%E6%AC%A7%E6%8B%89%E5%87%BD%E6%95%B0
func ProperFractions(n int) int {
	if n == 1 {
		return 0
	}

	res := n
	limit := int(math.Sqrt(float64(n))) + 1

	for i := 2; i < limit; i++ {
		if n%i == 0 {
			res = res / i * (i - 1)
			for n%i == 0 {
				n /= i
			}
		}
	}
	if n > 1 {
		res = res / n * (n - 1)
	}

	return res
}

func main() {
	fmt.Println(ProperFractions(1))
	fmt.Println(ProperFractions(15))
}
