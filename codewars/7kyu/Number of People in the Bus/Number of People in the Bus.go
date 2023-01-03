package main

func Number(busStops [][2]int) int {
	res := 0
	for _, arr := range busStops {
		res += (arr[0] - arr[1])
	}
	return res // Good Luck!
}
