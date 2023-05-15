package main

import "fmt"

func Permutations(s string) []string {
	// your code here
	var res []string
	m := make(map[string]bool)
	helper(s, "", &res, &m)
	return res
}

func helper(s string, curr string, res *[]string, m *map[string]bool) {
	if 0 == len(s) {
		if _, ok := (*m)[curr]; !ok {
			(*m)[curr] = true
			*res = append(*res, curr)
		}
		return
	}
	for i := 0; i < len(s); i++ {
		helper(s[0:i]+s[i+1:], curr+string(s[i]), res, m)
	}
}

func main() {
	fmt.Println(Permutations("ab"))
}
