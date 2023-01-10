package main

import "fmt"

func ValidISBN10(isbn string) bool {
	bs := []byte(isbn)
	val := 0
	n := len(bs)
	if n != 10 {
		return false
	}

	for i := 0; i < n; i++ {
		if '0' <= bs[i] && bs[i] <= '9' {
			val += int(bs[i]-'0') * (i + 1)
		} else if i == n-1 && (bs[i] == 'X' || bs[i] == 'x') {
			val += 10 * (i + 1)
		} else {
			return false
		}
	}
	fmt.Println(val)
	return val%11 == 0
}

func main() {
	ValidISBN10("1112223339")
}
