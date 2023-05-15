package main

func ExpSum(n uint64) uint64 {
	// your code here
	tmp := make([]uint64, n+1)
	tmp[0] = 1
	var i, j uint64
	for i = 1; i <= n; i++ {
		for j = i; j <= n; j++ {
			tmp[j] += tmp[j-i]
		}
	}
	return tmp[n]
}

func main() {

}
