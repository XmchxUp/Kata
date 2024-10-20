package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"sync"
)

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

	fmt.Println(getAnswer())
}

type Line struct {
	nums []int
}

func (l *Line) getPredNextValue() int {
	var allSteps [][]int
	allSteps = append(allSteps, l.nums)

	curNums := l.nums
	for {
		diffs := make([]int, len(curNums)-1)
		for i := 1; i < len(curNums); i++ {
			diffs[i-1] = curNums[i] - curNums[i-1]
		}
		allSteps = append(allSteps, diffs)

		curNums = diffs

		ok := true
		for _, v := range diffs {
			if v != 0 {
				ok = false
				break
			}
		}

		if ok {
			break
		}
	}

	v := 0
	for i := len(allSteps) - 1; i >= 0; i-- {
		// phase1
		// v += allSteps[i][len(allSteps[i])-1]
		// phase2
		v = allSteps[i][0] - v
	}

	return v
}

var lines []Line

func parse(line string) {
	line = strings.TrimSpace(line)
	if line == "" {
		return
	}

	vals := strings.Split(line, " ")
	l := Line{
		nums: make([]int, len(vals)),
	}

	for i, val := range vals {
		v, _ := strconv.Atoi(val)
		l.nums[i] = v
	}
	lines = append(lines, l)
}

func getAnswer() int {
	var wg sync.WaitGroup

	ch := make(chan int, len(lines))

	for _, line := range lines {
		wg.Add(1)
		go func() {
			defer wg.Done()
			ch <- line.getPredNextValue()
		}()
	}

	go func() {
		wg.Wait()
		close(ch)
	}()

	res := 0
	for v := range ch {
		res += v
	}

	return res
}
