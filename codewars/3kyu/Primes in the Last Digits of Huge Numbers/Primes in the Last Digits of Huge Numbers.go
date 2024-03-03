package main

import (
	"fmt"
	"math/big"
)

func KthLastDigitPrime(k int) [2]int {
	seq := make([]*big.Int, 5)
	seq[0] = big.NewInt(0)
	seq[1] = big.NewInt(1)
	seq[2] = big.NewInt(1)
	seq[3] = big.NewInt(2)
	seq[4] = big.NewInt(4)

	cnt := 0
	tmpVal := big.NewInt(1e9)
	for n := 5; ; n++ {
		// next := seq[4] + seq[3] - seq[2] + seq[1] - seq[0]
		next := big.NewInt(0).Set(seq[4])
		next.Add(next, seq[3])
		next.Sub(next, seq[2])
		next.Add(next, seq[1])
		next.Sub(next, seq[0])

		seq = append(seq[1:], next)
		if seq[4].Cmp(tmpVal) < 0 {
			continue
		}

		last9 := big.NewInt(0).Mod(seq[4], tmpVal)
		if last9.ProbablyPrime(20) {
			cnt++
			if cnt == k {
				return [2]int{n + 1, int(last9.Int64())}
			}
		}
	}

	return [2]int{}
}

func main() {
	fmt.Println(KthLastDigitPrime(1))
	fmt.Println(KthLastDigitPrime(7))
}
