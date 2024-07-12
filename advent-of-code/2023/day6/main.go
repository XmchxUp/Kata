package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Attr int

const (
	Time     Attr = iota
	Distance Attr = iota
)

type Race struct {
	Time     int
	Distance int
}

func (r Race) getDifferentWays() int {
	res := 0
	for i := 0; i <= r.Time/2; i++ {
		if r.Distance <= (r.Time-i)*i {
			res += 2
		}
	}
	return res
}

var races []Race

func getAnswer() int {
	res := 1
	for _, r := range races {
		res *= r.getDifferentWays()
	}
	return res
}

func initRacesPhase1With(attr Attr, parts []string) {
	if len(races) == 0 {
		races = make([]Race, len(parts))
		for i := 0; i < len(parts); i++ {
			races[i] = Race{}
		}
	}

	if len(races) != len(parts) {
		panic("Invalid input")
	}

	for i, p := range parts {
		v, _ := strconv.Atoi(strings.TrimSpace(p))
		if attr == Time {
			races[i].Time = v
		} else if attr == Distance {
			races[i].Distance = v
		}
	}
}

func initRacesPhase2With(attr Attr, parts []string) {
	if len(races) == 0 {
		races = append(races, Race{})
	}

	vStr := strings.Join(parts, "")

	v, _ := strconv.Atoi(strings.TrimSpace(vStr))
	if attr == Time {
		races[0].Time = v
	} else if attr == Distance {
		races[0].Distance = v
	}
}

func parseInput(line string) {
	parts := strings.Fields(line)[1:]
	if strings.HasPrefix(line, "Time:") {
		initRacesPhase2With(Time, parts)
	} else if strings.HasPrefix(line, "Distance:") {
		initRacesPhase2With(Distance, parts)
	} else {
		panic("Invalid input")
	}
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		line = strings.TrimSpace(line)
		if line == "END" {
			break
		}

		parseInput(line)
	}

	fmt.Println(getAnswer())
}
