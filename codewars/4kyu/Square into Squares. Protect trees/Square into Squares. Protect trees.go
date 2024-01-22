package kata

func Decompose(n int64) []int64 {
	// your code
	return helper(n, n*n)
}

func helper(n, remain int64) []int64 {
	if remain == 0 {
		return []int64{}
	}
	for i := n - 1; i >= 1; i-- {
		if i*i <= remain {
			res := helper(i, remain-i*i)
			if res != nil {
				return append(res, i)
			}
		}
	}
	return nil
}
