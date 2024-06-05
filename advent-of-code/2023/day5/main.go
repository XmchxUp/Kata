package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type ParseState int

const (
	SeedToSill ParseState = iota
	SoilToFertilizer
	FertilizerToWater
	WaterToLight
	LightToTemperature
	TemperatureToHumidity
	HumidityToLocation
	EmptyState
)

type Info struct {
	SrcStart int
	DstStart int
	Length   int
}

type InfoMap struct {
	Infos []Info
}

var seeds []int
var currInfoMap *InfoMap

var m map[string]*InfoMap = make(map[string]*InfoMap)

var findSeqs = []string{
	"seed",
	"soil",
	"fertilizer",
	"water",
	"light",
	"temperature",
	"humidity",
	"location",
}

func init() {
	for i, name := range findSeqs {
		if i == len(findSeqs)-1 {
			break
		}
		m[fmt.Sprintf("%s-to-%s", name, findSeqs[i+1])] = &InfoMap{}
	}
}

func parseInput(input string) {
	if strings.HasPrefix(input, "seeds") {
		tmps := strings.Split(input, " ")
		for i, tmp := range tmps {
			if i < 1 { // skip head
				continue
			}
			v, _ := strconv.Atoi(tmp)
			seeds = append(seeds, v)
		}
		return
	}

	if currInfoMap == nil {
		k := strings.TrimSpace(strings.ReplaceAll(input, " map:", ""))
		currInfoMap = m[k]
	} else {

		if currInfoMap == nil {
			panic("not correct input")
		}

		tmps := strings.Split(input, " ")

		dstStart, _ := strconv.Atoi(tmps[0])
		srcStart, _ := strconv.Atoi(tmps[1])
		length, _ := strconv.Atoi(tmps[2])

		currInfoMap.Infos = append(currInfoMap.Infos, Info{DstStart: dstStart, SrcStart: srcStart, Length: length})
	}
}

func getPhase1Seeds() []int {
	return seeds
}

func getPhase2Seeds() <-chan int {
	out := make(chan int)
	go func() {
		defer close(out)
		for i := 0; i < len(seeds); i += 2 {
			for k := seeds[i]; k < seeds[i]+seeds[i+1]; k++ {
				out <- k
			}
		}
	}()

	return out
}

func getAnswer() int {
	lowestLocationNumber := -1

	for seed := range getPhase2Seeds() {
		curK := seed
		for i, name := range findSeqs {
			if i == len(findSeqs)-1 {
				break
			}
			k := fmt.Sprintf("%s-to-%s", name, findSeqs[i+1])
			for _, info := range m[k].Infos {
				if curK >= info.SrcStart && curK < info.SrcStart+info.Length {
					curK = info.DstStart + (curK - info.SrcStart)
					break
				}
			}
		}
		if curK < lowestLocationNumber || lowestLocationNumber == -1 {
			lowestLocationNumber = curK
		}
	}

	return lowestLocationNumber
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		line = strings.TrimSpace(line)

		if line == "" {
			currInfoMap = nil
			continue
		}

		if line == "END" {
			break
		}

		parseInput(line)
	}

	fmt.Println(getAnswer())
}
