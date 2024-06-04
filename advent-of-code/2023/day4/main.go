package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type Card struct {
	ID          int
	WinningNums []int
	HasNums     []int
}

func (c Card) Score() int {
	nums := intersection(c.WinningNums, c.HasNums)
	return int(math.Pow(2, float64(len(nums)-1)))
}

var cache map[int]int = map[int]int{1: 1}

func getRecursive(m map[int][]int, id int) int {
	if val, ok := cache[id]; ok {
		return val
	}

	res := 1
	for _, v := range m[id] {
		res += getRecursive(m, v)
	}
	return res
}

func (c Card) Score2(m map[int][]int) int {
	if c.ID == 1 {
		return 1
	}

	return getRecursive(m, c.ID)
}

func intersection(nums1, nums2 []int) []int {
	m := make(map[int]struct{})
	res := []int{}
	for _, ele := range nums1 {
		m[ele] = struct{}{}
	}
	for _, ele := range nums2 {
		if _, ok := m[ele]; ok {
			res = append(res, ele)
		}
	}
	return res
}

var cards []Card

func getAnswer() int {
	ansP1 := 0
	for _, card := range cards {
		ansP1 += card.Score()
	}

	// 记录CardID可以由哪些CardID来生成
	m := map[int][]int{}

	for i := 0; i < len(cards); i++ {
		copyWidth := len(intersection(cards[i].HasNums, cards[i].WinningNums))
		for j := 0; j < copyWidth; j++ {
			m[j+1+i+1] = append(m[j+1+i+1], i+1)
		}
	}

	ansP2 := 0
	for _, c := range cards {
		ansP2 += c.Score2(m)
	}
	return ansP2
}

func parseNumbers(numsStr string, nums *[]int) {
	tmps := strings.Split(strings.TrimSpace(numsStr), " ")
	for _, tmp := range tmps {
		val, err := strconv.Atoi(tmp)
		if err != nil {
			continue
		}
		*nums = append(*nums, val)
	}
}

func parse(line string) {
	card := Card{}
	tmps := strings.Split(line, ": ")
	idStr := strings.TrimSpace(strings.ReplaceAll(tmps[0], "Card", ""))
	id, _ := strconv.Atoi(idStr)

	tmps2 := strings.Split(tmps[1], " | ")

	parseNumbers(tmps2[0], &card.WinningNums)
	parseNumbers(tmps2[1], &card.HasNums)

	card.ID = id

	cards = append(cards, card)
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		if line == "END" {
			break
		}
		parse(line)
	}
	fmt.Println(getAnswer())
}
