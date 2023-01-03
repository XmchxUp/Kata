package main

import (
	"fmt"
	"unicode"
)

func PlayPass(s string, n int) string {
	rns := []rune(s)
	nn := int32(n)
	for i, c := range s {
		if unicode.IsLetter(c) {
			// y + 2 -> a
			if unicode.IsUpper(c) {
				rns[i] = (c+nn-'A')%26 + 'A'
			} else {
				rns[i] = (c+nn-'a')%26 + 'a'
			}
		} else {
			rns[i] = c
		}
	}
	for i, c := range string(rns) {
		if unicode.IsDigit(c) {
			rns[i] = '9' - c + '0'
		} else {
			rns[i] = c
		}
	}
	for i, c := range string(rns) {
		if unicode.IsLetter(c) {
			if i%2 == 0 {
				rns[i] = unicode.ToUpper(c)
			} else {
				rns[i] = unicode.ToLower(c)
			}
		} else {
			rns[i] = c
		}
	}
	return reverse(rns)
}

func reverse(rns []rune) string {
	for i, j := 0, len(rns)-1; i < j; i, j = i+1, j-1 {
		rns[i], rns[j] = rns[j], rns[i]
	}
	return string(rns)
}

func main() {
	// fmt.Println(PlayPass("a123", 1))
	// fmt.Println(PlayPass("BORN IN 2015!", 1))
	fmt.Println(PlayPass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2))
}
