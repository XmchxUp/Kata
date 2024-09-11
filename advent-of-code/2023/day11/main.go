package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strings"
)

type Galaxy struct {
	x int
	y int
}

func (g Galaxy) shortPathWith(ga Galaxy) int {
	return int(math.Abs(float64(g.x-ga.x)) + math.Abs(float64(g.y-ga.y)))
}

var width int = 0
var height int = 0

var universe [][]byte
var galaxies []Galaxy

func init() {
	universe = make([][]byte, 0)
}

func checkAndExpansionWidth() {
	tmpWidths := []int{}
	for i := 0; i < width; i++ {
		hasGalaxy := false
		for j := 0; j < height; j++ {
			if universe[j][i] == '#' {
				hasGalaxy = true
				break
			}
		}
		if !hasGalaxy {
			tmpWidths = append(tmpWidths, i)
		}
	}

	newUniverse := make([][]byte, height)
	newWidth := width + len(tmpWidths)
	for i := range newUniverse {
		newUniverse[i] = make([]byte, newWidth)
	}

	ni := 0
	idx := 0

	for i := 0; i < width; i++ {
		for j := 0; j < height; j++ {
			newUniverse[j][ni] = universe[j][i]
		}
		ni += 1

		if idx < len(tmpWidths) && tmpWidths[idx] == i {
			for j := 0; j < height; j++ {
				newUniverse[j][ni] = universe[j][i]
			}
			idx++
			ni += 1
		}
	}

	universe = newUniverse
	width = newWidth
}

func getAnswerPhase1() int {
	checkAndExpansionWidth()

	for j := 0; j < height; j++ {
		for i := 0; i < width; i++ {
			if universe[j][i] == '#' {
				galaxies = append(galaxies, Galaxy{x: i, y: j})
			}
		}
	}

	res := 0
	for i := 0; i < len(galaxies); i++ {
		for j := i + 1; j < len(galaxies); j++ {
			res += galaxies[i].shortPathWith(galaxies[j])
		}
	}

	return res
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
		// expansion height
		universe = append(universe, tmp)
		universe = append(universe, tmp)
		height += 2
	}
}
