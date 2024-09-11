package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strings"
)

type Point struct {
	x  int
	y  int
	ch byte
}

type Galaxy struct {
	Point
}

func (g Galaxy) shortPathWith(ga Galaxy) int {
	return int(math.Abs(float64(g.x-ga.x)) + math.Abs(float64(g.y-ga.y)))
}

var epHeight int = 0
var height int = 0

var universe [][]*Point
var galaxies []Galaxy

// part 1
// const expansionTimes = 2
// const expansionTimes = 10
// const expansionTimes = 100

// part2
const expansionTimes = 1_000_000

func init() {
	universe = make([][]*Point, 0)
}

func checkAndExpansionWidth() {
	tmpWidths := []int{}
	width := len(universe[0])
	for i := 0; i < width; i++ {
		hasGalaxy := false
		for j := 0; j < height; j++ {
			if universe[j][i].ch == '#' {
				hasGalaxy = true
				break
			}
		}
		if !hasGalaxy {
			tmpWidths = append(tmpWidths, i)
		}
	}

	for _, i := range tmpWidths {
		for ni := i; ni < width; ni++ {
			for j := 0; j < height; j++ {
				universe[j][ni].x += (expansionTimes - 1)
			}
		}
	}
}

func getAnswerPhase1() int {
	checkAndExpansionWidth()

	for i := range universe {
		for j := range universe[i] {
			if universe[i][j].ch == '#' {
				galaxies = append(galaxies, Galaxy{*universe[i][j]})
				// fmt.Println(universe[i][j].x, universe[i][j].y)
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
	hasGalaxy := strings.ContainsAny(input, "#")

	universe = append(universe, []*Point{})

	for i, ch := range input {
		universe[height] = append(universe[height], &Point{x: i, y: epHeight, ch: byte(ch)})

	}
	height += 1
	if hasGalaxy {
		epHeight += 1
	} else {
		// expansion height
		epHeight += expansionTimes
	}
}
