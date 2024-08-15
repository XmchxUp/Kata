package main

import "fmt"

type A struct {
	x, y int
}

func main() {

	a := A{1, 2}
	fmt.Println(a == A{2, 2})
	fmt.Println(a == A{1, 2})
}
