package main

import "fmt"

type A struct {
	B int
}

var a [1]A

func tet(c [1]A) {
	c[0].B = 2
}

func main() {

	a[0] = A{B: 1}
	tet(a)
	fmt.Println(a[0].B)
}
