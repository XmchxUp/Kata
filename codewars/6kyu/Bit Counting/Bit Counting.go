package main

import (
	"strconv"
	"strings"
)

func CountBits(num uint) int {
	res := 0
	for num > 0 {
		if num&0x1 == 0x1 {
			res++
		}
		num /= 2
	}
	return res
}

func CountBits2(num uint) int {
	b := convert2Binary(num)
	res := 0
	for _, c := range b {
		if c == '1' {
			res++
		}
	}
	return res
}

func convert2Binary(num uint) string {
	var sb strings.Builder
	for num != 0 {
		sb.WriteString(strconv.Itoa(int(num % 2)))
		num /= 2
	}
	// TODO: reverse
	return sb.String()
}

func main() {

}
