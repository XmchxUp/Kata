package kata

import (
	"math/big"
)

// https://zh.wikipedia.org/wiki/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0#%E6%81%86%E7%AD%89%E5%BC%8F
func fib(n int64) *big.Int {
	if n == 0 || n == 1 {
		return big.NewInt(n)
	}

	if n >= 2 && n%2 == 0 {
		l := fib(n / 2)
		x := big.NewInt(2)
		x.Mul(x, fib((n/2)-1))
		x.Add(x, l)
		return x.Mul(x, l)
	}

	mod := (n + 1) / 2
	if n >= 2 {
		// n is odd
		x := fib(mod - 1)
		y := fib(mod)
		x.Mul(x, x)
		y.Mul(y, y)
		return x.Add(x, y)
	}
	// n is negative
	a, b := big.NewInt(0), big.NewInt(1)
	for i := int64(0); i > n; i-- {
		a, b = b.Sub(b, a), a
	}
	return a
}

func fibV1(n int64) *big.Int {
	//Code here :)
	result := big.NewInt(0)
	a := big.NewInt(0)
	b := big.NewInt(1)

	if n == 0 {
		return big.NewInt(0)
	} else if n == 1 || n == -1 {
		return big.NewInt(1)
	} else if n > 1 {
		for i := int64(2); i <= n; i++ {
			result.Add(a, b)
			a.Set(b)
			b.Set(result)
		}
	} else { // negative
		for i := int64(-1); i >= n; i-- {
			result.Sub(b, a)
			b.Set(a)
			a.Set(result)
		}
	}
	return result
}
