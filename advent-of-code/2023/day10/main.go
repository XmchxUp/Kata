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
	return p.x < 0 || p.y < 0 || p.x >= width || p.y >= cntLine
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

var cntLine = 0
var width = 0
var m = make(map[Position]*Pipe)
var start Position

func parse(input string) {
	if width != 0 && width != len(input) {
		panic("not correct format")
	} else {
		width = len(input)
	}

	for x, ch := range input {
		p := Position{x, cntLine}
		switch ch {
		case '|':
			m[p] = &Pipe{p1: p.Move(N), p2: p.Move(S), typ: VerticalPipe}
		case '-':
			m[p] = &Pipe{p1: p.Move(W), p2: p.Move(E), typ: HorizontalPipe}
		case 'L':
			m[p] = &Pipe{p1: p.Move(N), p2: p.Move(E), typ: NEBend}
		case 'J':
			m[p] = &Pipe{p1: p.Move(N), p2: p.Move(W), typ: NWBend}
		case '7':
			m[p] = &Pipe{p1: p.Move(S), p2: p.Move(W), typ: SWBend}
		case 'F':
			m[p] = &Pipe{p1: p.Move(S), p2: p.Move(E), typ: SEBend}
		case '.':
			continue
		case 'S':
			start = Position{x, cntLine}
		default:
			panic("unknow flag")
		}
	}
	cntLine += 1
}

func getPhase1() int {
	res := 0

	q := []Position{}

	curP := start
	visited := make(map[Position]bool, 0)
	visited[curP] = true

	dirs := []Direction{N, W, S, E}
	for _, dir := range dirs {
		nextPos := curP.Move(dir)
		if nextPos.IsIllegal() || visited[nextPos] {
			continue
		}

		nextPipe, ok := m[nextPos]
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
			curPipe, ok := m[curPos]
			if !ok {
				continue
			}

			nextPos := curPipe.NextPosition()

			if nextPos == nil || visited[*nextPos] || nextPos.IsIllegal() {
				continue
			}

			if nextPipe, ok := m[*nextPos]; ok {
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

	fmt.Println(getPhase1())
}
