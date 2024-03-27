package main

func Multiple3And5(number int) int {
	res := 0
	for i := 3; i < number; i++ {
		if i%3 == 0 || i%5 == 0 {
			res += i
		}
	}
	return res
}
