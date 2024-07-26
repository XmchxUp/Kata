package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type CamelCardType int
type Card string

const (
	FiveOfAKind CamelCardType = iota
	FourOfAKind
	FullHouse
	ThreeOfAKind
	TwoPair
	OnePair
	HighCard
)

var cardValues = map[Card]int{
	"2": 2,
	"3": 3,
	"4": 4,
	"5": 5,
	"6": 6,
	"7": 7,
	"8": 8,
	"9": 9,
	"T": 10,
	"J": 11,
	"Q": 12,
	"K": 13,
	"A": 14, // Ace is high
}

type Hand struct {
	Cards []Card
	CCT   CamelCardType
	Bid   int
}

func NewHand(cards []Card, bid int) *Hand {
	h := &Hand{Cards: cards, Bid: bid}
	h.updateType()
	return h
}

func (h *Hand) updateType() {

}

func (h *Hand) Compare(another *Hand) bool {
	if h.CCT == another.CCT {
		for i, c := range h.Cards {
			if c == another.Cards[i] {
				continue
			}
			return cardValues[c] < cardValues[another.Cards[i]]
		}
	}
	return h.CCT > another.CCT
}

var hands []*Hand

func parseInput(input string) {
	parts := strings.Split(input, " ")
	if len(parts) != 2 {
		return
	}

	cardStr := strings.Split(parts[0], "")
	cards := make([]Card, 0)
	for _, c := range cardStr {
		cards = append(cards, Card(c))
	}

	bid, err := strconv.Atoi(parts[1])
	if err != nil {
		fmt.Print(err)
		return
	}

	hands = append(hands, NewHand(cards, bid))
}

func getAnswer() int {
	res := 0

	sort.Slice(hands, func(i, j int) bool {
		return hands[i].Compare(hands[j])
	})

	for i, h := range hands {
		fmt.Println(i, h.Bid)
		res += (i + 1) * h.Bid
	}

	return res
}

func main() {

	s := bufio.NewScanner(os.Stdin)
	for s.Scan() {
		line := s.Text()
		line = strings.TrimSpace(line)
		if line == "END" {
			break
		}
		parseInput(line)
	}
	fmt.Println(getAnswer())
}
