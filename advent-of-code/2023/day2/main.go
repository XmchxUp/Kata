package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	RedCnt   = 12
	GreenCnt = 13
	BlueCnt  = 14
)

type SubInfo struct {
	Blue  int
	Green int
	Red   int
}

type GameInformation struct {
	ID       int
	BlueMax  int
	GreenMax int
	RedMax   int
	Subsets  []SubInfo
}

var gameInfos []GameInformation

func parseGameInfo(line string) {
	gi := GameInformation{
		Subsets: make([]SubInfo, 0),
	}

	strs := strings.Split(line, ":")
	id, _ := strconv.Atoi(strs[0][5:])
	gi.ID = id

	subStrs := strings.Split(strs[1], ";")
	var blueMax, greenMax, redMax int

	for _, subStr := range subStrs {
		tmpStrs := strings.Split(strings.TrimSpace(subStr), ",")
		var si SubInfo
		for _, tmpStr := range tmpStrs {
			vals := strings.Split(strings.TrimSpace(tmpStr), " ")
			val, _ := strconv.Atoi(vals[0])
			if vals[1] == "blue" {
				si.Blue = val
			} else if vals[1] == "green" {
				si.Green = val
			} else if vals[1] == "red" {
				si.Red = val
			} else {
				panic(fmt.Sprintf("error color %s", vals[1]))
			}
		}
		blueMax = max(blueMax, si.Blue)
		greenMax = max(greenMax, si.Green)
		redMax = max(redMax, si.Red)
		gi.Subsets = append(gi.Subsets, si)
	}

	gi.BlueMax = blueMax
	gi.GreenMax = greenMax
	gi.RedMax = redMax
	gameInfos = append(gameInfos, gi)
}

func getAnswer() int {
	answerP1 := 0
	answerP2 := 0
	for _, gi := range gameInfos {
		answerP2 += gi.BlueMax * gi.GreenMax * gi.RedMax
		if gi.BlueMax > BlueCnt || gi.GreenMax > GreenCnt || gi.RedMax > RedCnt {
			continue
		}
		answerP1 += gi.ID
	}
	return answerP2
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		input := scanner.Text()
		if input == "END" {
			break
		}
		parseGameInfo(input)
	}

	fmt.Println("answer is :", getAnswer())
}
