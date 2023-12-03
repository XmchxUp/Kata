package main

import (
	"fmt"
	"math"
	"sort"
	"strconv"
)

func isPrime(num int) bool {
	if num <= 1 {
		return false
	}
	for i := 2; i <= int(math.Sqrt(float64(num))); i += 1 {
		if num%i == 0 {
			return false
		}
	}
	return true
}

func getPermutation(num int) []int {
	numSet := make(map[int]struct{})
	originalNumStr := strconv.Itoa(num)
	originalNumLength := len(originalNumStr)

	var helper func(string, string)

	helper = func(prefix string, remaining string) {
		if len(remaining) == 0 && prefix[0] != '0' && len(prefix) == originalNumLength {
			val, _ := strconv.Atoi(prefix)
			numSet[val] = struct{}{}
		}
		for i := range remaining {
			helper(prefix+string(remaining[i]), remaining[:i]+remaining[i+1:])
		}
	}

	helper("", originalNumStr)

	res := make([]int, 0, len(numSet))
	for k := range numSet {
		res = append(res, k)
	}
	return res
}

func PermutationalPrimes(nMax, kPerms int) [3]int {
	arr := []int{}
	skips := make(map[int]bool)
	for i := 2; i < nMax; i++ {
		if !isPrime(i) {
			continue
		}
		if _, ok := skips[i]; ok {
			continue
		}

		perms := getPermutation(i)
		primePerms := []int{}
		for _, perm := range perms {
			if isPrime(perm) && perm < nMax {
				skips[perm] = true
				primePerms = append(primePerms, perm)
			}
		}

		for _, v := range primePerms {
			skips[v] = true
		}

		if len(primePerms) != kPerms+1 {
			continue
		}
		sort.Ints(primePerms)
		arr = append(arr, primePerms[0])
	}

	size := len(arr)
	if size == 0 {
		return [3]int{0, 0, 0}
	}
	return [3]int{
		size, arr[0], arr[size-1],
	}
}

func main() {
	fmt.Println(PermutationalPrimes(2000, 1))
	fmt.Println(PermutationalPrimes(40519, 8))
}
