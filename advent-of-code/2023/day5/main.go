package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
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

// Range [start, end)
type Range struct {
	Start, End int
}

type Ranges []Range

func (r Ranges) Empty() bool {
	return len(r) == 0
}

// merge sorts the Ranges and merges overlapping or contiguous ranges.
// The function modifies the receiver Ranges in-place to contain the merge result.
func (r *Ranges) merge() {
	if r.Empty() {
		return
	}

	sort.Slice(*r, func(i, j int) bool {
		if (*r)[i].Start == (*r)[j].Start {
			return (*r)[i].End < (*r)[j].End
		}
		return (*r)[i].Start < (*r)[j].Start
	})

	merged := Ranges{}

	current := (*r)[0]

	for _, next := range (*r)[1:] {
		if next.Start <= current.End {
			current.End = max(current.End, next.End)
		} else {
			merged = append(merged, current)
			current = next
		}
	}

	merged = append(merged, current)

	*r = merged
}

func (r Ranges) Union(other Ranges) Ranges {
	combined := append(r, other...)

	combined.merge()

	return combined
}

func (r Ranges) Intersection(other Ranges) Ranges {
	result := Ranges{}
	for _, ra := range r {
		for _, rb := range other {
			if ra.End <= rb.Start || rb.End <= ra.Start {
				continue
			}

			result = append(result, Range{
				Start: max(ra.Start, rb.Start),
				End:   min(ra.End, rb.End),
			})
		}
	}
	return result
}

func (r Ranges) Difference(other Ranges) Ranges {
	result := Ranges{}

	for _, ra := range r {
		for _, rb := range other {
			if ra.End > rb.Start && rb.End > ra.Start { // overlaping
				if rb.Start > ra.Start {
					result = append(result, Range{Start: ra.Start, End: rb.Start})
				}
				if rb.End < ra.End {
					ra.Start = rb.End
				} else {
					ra.Start = ra.End
				}
			}
		}
		if ra.Start < ra.End {
			result = append(result, ra)
		}
	}

	return result
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
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
	// 得运行多久？
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

	for seed := range getPhase1Seeds() {
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

// getAnswerOptimaze
// 将所有操作都使用区间（交集，差集，合并），最后得出所有location的区间(排序后的)，每一个区间的start就是结果
func getAnswerOptimaze() int {
	// seeds-ranges.intersection(cur-level-ranges)
	// calculate next-level-offset-ranges
	// seeds-ranges.difference(cur-level-ranges) = diff-seeds-ranges
	// diff-seeds-ranges.union(next-level-offset-ranges) = all-next-level-ranges
	// repeat all level

	seedsRanges := Ranges{}
	for i := 0; i < len(seeds); i += 2 {
		seedsRanges = append(seedsRanges, Range{
			Start: seeds[i],
			End:   seeds[i] + seeds[i+1],
		})
	}
	// fmt.Println(seedsRanges)

	currentRanges := Ranges{}
	allNextLevelRanges := Ranges{}

	currentRanges = currentRanges.Union(seedsRanges)
	fmt.Println(currentRanges)

	for i, name := range findSeqs {
		if i == len(findSeqs)-1 {
			break
		}

		k := fmt.Sprintf("%s-to-%s", name, findSeqs[i+1])

		currLevelRanges := Ranges{}
		for _, info := range m[k].Infos {
			currLevelRanges = append(currLevelRanges, Range{
				Start: info.SrcStart,
				End:   info.SrcStart + info.Length,
			})
		}
		fmt.Println("currLevelRanges:", currLevelRanges)

		tmpRanges := currentRanges.Intersection(currLevelRanges)

		fmt.Println("tmpRanges:", tmpRanges)
		for _, r := range tmpRanges {
			for _, info := range m[k].Infos {
				if r.Start >= info.SrcStart && r.End < info.SrcStart+info.Length {
					diff := info.DstStart - info.SrcStart
					allNextLevelRanges = allNextLevelRanges.Union(Ranges{
						Range{
							Start: r.Start + diff,
							End:   r.End + diff,
						},
					})
				}
			}
		}
		fmt.Println("allNextLevelRanges:", allNextLevelRanges)

		allNextLevelRanges = allNextLevelRanges.Union(currentRanges.Difference(currLevelRanges))

		currentRanges = currentRanges.Union(allNextLevelRanges)
		fmt.Println("currentRanges:", currentRanges)
		allNextLevelRanges = Ranges{}
	}

	return currentRanges[0].Start
}

func rangeTest() {
	r1 := Ranges{Range{2, 3}, Range{4, 30}}
	r2 := Ranges{Range{2, 4}, Range{5, 20}}
	fmt.Println(r1.Union(r2))
	fmt.Println(r1.Intersection(r2))
	fmt.Println(r1.Difference(r2))
}

func main() {
	rangeTest()
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

	fmt.Println(getAnswerOptimaze())
}
