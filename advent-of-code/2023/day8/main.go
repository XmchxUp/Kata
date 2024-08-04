package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strings"
	"sync"
)

type Command int

const (
	Left Command = iota
	Right

	mapPattern string = `(\w+) = \((\w+), (\w+)\)`
)

type Map struct {
	Name  string
	Left  string
	Right string
}

var maps map[string]Map
var mapPatternRe *regexp.Regexp
var commands []Command
var starts []string

func getAnswer1(startName string, isEnd func(name string) bool) int {
	curName := startName
	steps := 0
	idx := 0
	for !isEnd(curName) {
		c := commands[idx]
		steps += 1
		if c == Left {
			curName = maps[curName].Left
		} else if c == Right {
			curName = maps[curName].Right
		}
		idx = (idx + 1) % len(commands)
	}
	fmt.Println(startName, steps)
	return steps
}

func getAnswer2() int {
	// 分别计算每一个start到endpoint的步数，然后求最大公倍数
	ch := make(chan int, len(starts))
	var wg sync.WaitGroup

	for _, n := range starts {
		wg.Add(1)
		go func(name string) {
			defer wg.Done()
			ch <- getAnswer1(name, func(t string) bool {
				return strings.HasSuffix(t, "Z")
			})
		}(n)
	}

	curV := -1
	go func() {
		wg.Wait()
		close(ch)
	}()

	for v := range ch {
		if curV == -1 {
			curV = v
		} else {
			curV = lcm(v, curV)
		}
	}
	return curV
}

func gcd(a, b int) int {
	if a < b {
		return gcd(b, a)
	}
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func lcm(a, b int) int {
	return a / gcd(a, b) * b
}

func parse(line string) {
	line = strings.TrimSpace(line)
	if line == "" {
		return
	}

	if strings.Contains(line, "=") {
		matches := mapPatternRe.FindStringSubmatch(line)
		if len(matches) <= 3 {
			panic("map format error")
		}

		m := Map{Name: matches[1], Left: matches[2], Right: matches[3]}
		maps[m.Name] = m
		if strings.HasSuffix(m.Name, "A") {
			starts = append(starts, m.Name)
		}
	} else {
		for _, c := range line {
			if c == 'L' {
				commands = append(commands, Left)
			} else if c == 'R' {
				commands = append(commands, Right)
			} else {
				panic("unknow command")
			}
		}
	}

}

func init() {
	mapPatternRe = regexp.MustCompile(mapPattern)
	maps = make(map[string]Map)
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
		line := scanner.Text()
		parse(line)
	}

	// fmt.Println(getAnswer1("AAA", func(name string) bool {
	// 	return name == "ZZZ"
	// }))
	fmt.Println(getAnswer2())
}
