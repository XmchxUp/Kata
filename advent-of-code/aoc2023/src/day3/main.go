package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"unicode"
)

type Point struct {
	X, Y int
}

type Number struct {
	Val       int
	Width     int
	HasSymbol bool
	Symbol    *Symbol
	Point
}

type Symbol struct {
	Ch rune
	Point
}

var numbers []*Number
var symbols []*Symbol

func hasSymbol(nm Number, symbol Symbol) bool {
	if nm.Y == symbol.Y {
		if nm.X+nm.Width == symbol.X || nm.X-1 == symbol.X {
			return true
		}
	}

	if symbol.Y == nm.Y-1 {
		for i := 0; i < nm.Width+2; i++ {
			if symbol.X == nm.X-1+i {
				return true
			}
		}
	}

	if symbol.Y == nm.Y+1 {
		for i := 0; i < nm.Width+2; i++ {
			if symbol.X == nm.X-1+i {
				return true
			}
		}
	}

	return false
}

func parse(matrix [][]rune, row, col int) {
	var x, y int

	for y = 0; y < row; y++ {
		for x = 0; x < col; x++ {
			if unicode.IsDigit(matrix[y][x]) {
				var num Number
				end_x := x + 1
				for end_x < col && unicode.IsDigit(matrix[y][end_x]) {
					end_x++
				}
				val, _ := strconv.Atoi(string(matrix[y][x:end_x]))
				num.Val = val
				num.Width = end_x - x
				num.Point = Point{X: x, Y: y}
				x = end_x
				numbers = append(numbers, &num)
			}
			if x == col {
				continue
			}
			if matrix[y][x] == '.' {
				continue
			}
			symbols = append(symbols, &Symbol{Point: Point{X: x, Y: y}, Ch: matrix[y][x]})
		}
	}

	for _, symbol := range symbols {
		for i := range numbers {
			if hasSymbol(*numbers[i], *symbol) {
				numbers[i].HasSymbol = true
				numbers[i].Symbol = symbol
			}
		}
	}
}

func getAnswer() int {
	answerP1 := 0
	answerP2 := 0
	for _, number := range numbers {
		if number.HasSymbol {
			answerP1 += number.Val
		}
	}

	for _, symbol := range symbols {
		if symbol.Ch != '*' {
			continue
		}

		nb1, nb2 := -1, -1
		// TODO: 可以优化使用个map存储每个Poin,这样只需要遍历判断周边是否有Number
		for _, number := range numbers {
			if !number.HasSymbol || number.Symbol != symbol {
				continue
			}
			if nb1 != -1 && nb2 != -1 {
				panic("three numbers?")
			}
			if nb1 == -1 {
				nb1 = number.Val
			} else if nb2 == -1 {
				nb2 = number.Val
			}
		}
		if nb1 != -1 && nb2 != -1 {
			answerP2 += (nb1 * nb2)
		}
	}
	return answerP2
}

func main() {
	var matrix [][]rune

	scanner := bufio.NewScanner(os.Stdin)
	var row, col int
	for scanner.Scan() {
		line := scanner.Text()
		if line == "END" {
			break
		}
		col = len(line)
		matrix = append(matrix, []rune(line))
		row += 1
	}

	parse(matrix, row, col)
	fmt.Println(getAnswer())
}
