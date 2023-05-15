package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

func gcd(x, y int) int {
	if y == 0 {
		return x
	}
	if x < y {
		return gcd(y, x)
	}
	return gcd(y, x%y)
}

func parse(s string) (int, int, error) {
	if strings.ContainsAny(s, ".") {
		// 0.66
		lst := strings.Split(s, ".")
		if len(lst) != 2 {
			return 0, 0, nil
		}
		x, err := strconv.Atoi(lst[0])
		if err != nil {
			return 0, 0, err
		}
		n := len(lst[1])
		n = int(math.Pow10(n))
		y, err := strconv.Atoi(lst[1])
		if err != nil {
			return 0, 0, err
		}
		x = x*n + y
		y = n
		g := gcd(x, y)
		return x / g, y / g, nil
	} else if strings.ContainsAny(s, "/") {
		// a/b
		lst := strings.Split(s, "/")
		if len(lst) != 2 {
			return 0, 0, nil
		}
		x, err := strconv.Atoi(lst[0])
		if err != nil {
			return 0, 0, err
		}
		y, err := strconv.Atoi(lst[1])
		if err != nil {
			return 0, 0, err
		}
		g := gcd(x, y)
		return x / g, y / g, nil
	} else {
		x, err := strconv.Atoi(s)
		return x, 1, err
	}
}

func Decompose(s string) []string {
	var res []string
	x, y, err := parse(s)
	if err != nil {
		panic("error format argument")
	}
	if x == 0 {
		return []string{}
	}
	var k int
	for x >= y {
		k = x / y
		res = append(res, fmt.Sprintf("%d", k))
		x = x - k*y
	}
	if x != 0 {
		for {
			if x <= 1 {
				break
			}
			k = y/x + 1
			res = append(res, fmt.Sprintf("1/%d", k))
			// x/y - 1/k
			x = x*k - y
			y = y * k
			g := gcd(x, y)
			x = x / g
			y = y / g
		}
		res = append(res, fmt.Sprintf("1/%d", y))
	}
	return res
}

func main() {
	fmt.Println(Decompose("21/23"))
	fmt.Println(Decompose("12/4"))
	fmt.Println(Decompose("0.66"))
	fmt.Println(Decompose("1"))
}
