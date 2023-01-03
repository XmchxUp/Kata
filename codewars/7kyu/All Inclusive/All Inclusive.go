package main

import "fmt"

func ContainAllRots(strng string, arr []string) bool {
	m := make(map[string]bool)
	for _, a := range arr {
		m[a] = true
	}

	n := len(strng)
	for i := 0; i < n; i++ {
		tmpStr := strng[i:] + strng[0:i]
		if _, ok := m[tmpStr]; !ok {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(ContainAllRots("bsjq", []string{"bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"}))
	// fmt.Println(ContainAllRots("XjYABhR", []string{"TzYxlgfnhf", "yqVAuoLjMLy", "BhRXjYA", "YABhRXj", "hRXjYAB", "jYABhRX", "XjYABhR", "ABhRXjY"}))
	// fmt.Println(ContainAllRots("", []string{}))
}
