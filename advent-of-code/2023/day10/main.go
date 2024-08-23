package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type Position struct {
	x, y int
}

func (p Position) Move(dir Direction) Position {
	switch dir {
	case N:
		return Position{p.x, p.y - 1}
	case S:
		return Position{p.x, p.y + 1}
	case W:
		return Position{p.x - 1, p.y}
	case E:
		return Position{p.x + 1, p.y}
	default:
		panic("not correct direction")
	}
}

func (p Position) IsIllegal() bool {
	return p.x < 0 || p.y < 0 || p.x >= width || p.y >= height
}

type PipeType uint8
type Direction byte

type Pipe struct {
	p1, p2  Position
	typ     PipeType
	nextPos *Position
}

func (p Pipe) NextPosition() *Position {
	return p.nextPos
}

func (p *Pipe) CalculateNextPosition(entryPos Position) {
	if entryPos == p.p1 {
		p.nextPos = &p.p2
	} else if entryPos == p.p2 {
		p.nextPos = &p.p1
	} else { // can't use pipe
		p.nextPos = nil
	}
}

const (
	VerticalPipe PipeType = iota
	HorizontalPipe
	NEBend
	NWBend
	SWBend
	SEBend
)

const (
	N Direction = iota
	S
	W
	E
)

var height = 0
var width = 0
var pipes = make(map[Position]*Pipe)
var start Position
var grid [][]rune
var dirs = []Direction{N, W, S, E}

func parse(input string) {
	if width != 0 && width != len(input) {
		panic("not correct format")
	} else {
		width = len(input)
	}

	row := make([]rune, width)
	for x, ch := range input {
		p := Position{x, height}
		row[x] = ch
		switch ch {
		case '|':
			pipes[p] = &Pipe{p1: p.Move(N), p2: p.Move(S), typ: VerticalPipe}
		case '-':
			pipes[p] = &Pipe{p1: p.Move(W), p2: p.Move(E), typ: HorizontalPipe}
		case 'L':
			pipes[p] = &Pipe{p1: p.Move(N), p2: p.Move(E), typ: NEBend}
		case 'J':
			pipes[p] = &Pipe{p1: p.Move(N), p2: p.Move(W), typ: NWBend}
		case '7':
			pipes[p] = &Pipe{p1: p.Move(S), p2: p.Move(W), typ: SWBend}
		case 'F':
			pipes[p] = &Pipe{p1: p.Move(S), p2: p.Move(E), typ: SEBend}
		case '.':
			continue
		case 'S':
			start = Position{x, height}
		default:
			panic("unknow flag")
		}
	}
	grid = append(grid, row)
	height += 1
}

func getPhase1() int {
	res := 0

	q := []Position{}

	curP := start
	visited := make(map[Position]bool, 0)
	visited[curP] = true

	for _, dir := range dirs {
		nextPos := curP.Move(dir)
		if nextPos.IsIllegal() || visited[nextPos] {
			continue
		}

		nextPipe, ok := pipes[nextPos]
		if !ok {
			continue
		}

		nextPipe.CalculateNextPosition(curP)
		if nextPipe.NextPosition() == nil { // can't use pipe
			continue
		}

		visited[nextPos] = true
		q = append(q, nextPos)
	}

	for len(q) > 0 {
		tmpQ := []Position{}

		for _, curPos := range q {
			curPipe, ok := pipes[curPos]
			if !ok {
				continue
			}

			nextPos := curPipe.NextPosition()

			if nextPos == nil || visited[*nextPos] || nextPos.IsIllegal() {
				continue
			}

			if nextPipe, ok := pipes[*nextPos]; ok {
				nextPipe.CalculateNextPosition(curPos)
			}

			visited[*nextPos] = true
			tmpQ = append(tmpQ, *nextPos)
		}

		q = tmpQ
		res++
	}

	return res
}

func getPhase2() int {
	fmt.Println(width, height)
	visited := make(map[Position]bool)

	for y := 0; y < height; y++ {
		if grid[y][0] == '.' {
			floodFill(Position{x: 0, y: y}, visited)
		}
		if grid[y][width-1] == '.' {
			floodFill(Position{x: width - 1, y: y}, visited)
		}
	}

	for x := 0; x < width; x++ {
		if grid[0][x] == '.' {
			floodFill(Position{x: x, y: 0}, visited)
		}
		if grid[height-1][x] == '.' {
			floodFill(Position{x: x, y: height - 1}, visited)
		}
	}

	floodFill(start, visited)

	res := 0
	for y := 0; y < height; y++ {
		for x := 0; x < width; x++ {
			pos := Position{x, y}
			if grid[y][x] == '.' && !visited[pos] {
				fmt.Printf("?")
				res++
			} else {
				fmt.Printf(".")
			}
		}
		fmt.Println()
	}

	return res
}

func floodFill(p Position, visited map[Position]bool) {
	if p.IsIllegal() || visited[p] {
		return
	}

	q := []Position{p}
	visited[p] = true
	fmt.Println("start ", p)

	for len(q) > 0 {
		fmt.Println(q)
		cur := q[0]
		q = q[1:]

		for _, dir := range dirs {
			nextPos := cur.Move(dir)
			if nextPos.IsIllegal() || visited[nextPos] {
				continue
			}

			if pipe, ok := pipes[nextPos]; ok {
				pipe.CalculateNextPosition(cur)
				pipeExitP := pipe.NextPosition()

				tmpVisisted := make(map[Position]bool)
				tmpVisisted[nextPos] = true

				// 一直使用管道，看看能否找到一个点
				found := false
				for {
					if pipeExitP == nil || tmpVisisted[*pipeExitP] || pipeExitP.IsIllegal() {
						break
					}

					if pp, ok := pipes[*pipeExitP]; ok {
						tmpVisisted[*pipeExitP] = true
						pp.CalculateNextPosition(*pipeExitP)
						pipeExitP = pp.NextPosition()
					} else {
						found = true
						break
					}
				}

				if found {
					visited[*pipeExitP] = true
					q = append(q, *pipeExitP)
				}
			} else {
				visited[nextPos] = true
				q = append(q, nextPos)
			}
		}
	}
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
		input = strings.TrimSpace(input)
		if len(input) == 0 {
			continue
		}
		parse(input)
	}

	// fmt.Println(getPhase1())
	fmt.Println(getPhase2())
}
