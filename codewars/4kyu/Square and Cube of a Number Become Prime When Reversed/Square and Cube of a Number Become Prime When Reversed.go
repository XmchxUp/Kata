package main

import (
	"fmt"
	"math"
)

var (
	_primeCache         = make(map[int]bool)
	_reverseNumberCache = make(map[int]int)
)

func isPrimeNumber(n int) bool {
	if v, ok := _primeCache[n]; ok {
		return v
	}
	if n <= 2 {
		v := (n == 2)
		_primeCache[n] = v
		return v
	}
	if n%2 == 0 {
		_primeCache[n] = false
		return false
	}
	sqrt := int(math.Sqrt(float64(n)))
	for i := 3; i <= sqrt+1; i += 2 {
		if n%i == 0 {
			_primeCache[n] = false
			return false
		}
	}
	_primeCache[n] = true
	return true
}

// func reverseNumber(n int) int {
// 	s := strconv.FormatInt(int64(n), 10)
// 	b := []byte(s)
// 	sLen := len(s)
// 	for i := 0; i < sLen/2; i++ {
// 		b[i], b[sLen-i-1] = b[sLen-i-1], b[i]
// 	}
// 	res, _ := strconv.Atoi(string(b))
// 	return res
// }

func reverseNumber(n int) int {
	if v, ok := _reverseNumberCache[n]; ok {
		return v
	}
	res := 0
	for n > 0 {
		res = res*10 + n%10
		n /= 10
	}
	_reverseNumberCache[n] = res
	return res
}

func isFRevPrime(f func(int) int, n int) bool {
	tmpNumber := reverseNumber(f(n))
	tmp := isPrimeNumber(tmpNumber)
	return tmp
}

func SqCubRevPrime(n int) int {
	square := func(c int) int {
		return c * c
	}
	cube := func(c int) int {
		return c * c * c
	}

	cnt := 0
	res := 0
	for i := 89; cnt < n; i++ {
		if isFRevPrime(square, i) && isFRevPrime(cube, i) {
			res = i
			cnt++
		}
	}
	return res
}

func main() {
	for i := 1; i <= 250; i++ {
		fmt.Println(SqCubRevPrime(i))
	}
}
