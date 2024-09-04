package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type Galaxy struct {
	x int
	y int
}

var width int = 0
var height int = 0

var universe [][]byte

func init() {
	universe = make([][]byte, 0)
}

func expansion() {
	newUniverse := make([][]byte, height)
	tmp := make([]byte, width)
	tw := 0
	th := 0
	for i := 0; i < width; i++ {
		hasGalaxy := false
		for j := 0; j < height; j++ {
			if universe[j][i] == '#' {
				hasGalaxy = true
			}
		}
		if !hasGalaxy {
			// expansion
		} else {
		}
	}
	universe = newUniverse
}

func getAnswerPhase1() int {
	expansion()
	fmt.Println(universe)
	return 0
}

func main() {
	if len(os.Args) != 2 {
		panic("Usage: ./main <file-path>")
	}

	file, err := os.Open(os.Args[1])
	if err != nil {
		panic(err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		input := scanner.Text()
		parse(input)
	}

	fmt.Println(getAnswerPhase1())
}

func parse(input string) {
	if width == 0 {
		width = len(input)
	}

	hasGalaxy := strings.ContainsAny(input, "#")
	tmp := []byte(input)

	if hasGalaxy {
		universe = append(universe, tmp)
		height += 1
	} else {
		// expansion
		universe = append(universe, tmp)
		universe = append(universe, tmp)
		height += 2
	}
}
