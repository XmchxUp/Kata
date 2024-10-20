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
	"J": 1, // phase2 is weakest
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

// phase2
func (h *Hand) updateType2(m map[string]int, pairCnt int, hasThree bool) {
	if h.CCT == FiveOfAKind {
		return
	}

	v, ok := m["J"]
	if !ok {
		return
	}

	if h.CCT == FourOfAKind {
		h.CCT = FiveOfAKind
		return
	}

	switch v {
	case 1:
		if hasThree {
			h.CCT = FourOfAKind
		} else if pairCnt == 0 {
			h.CCT = OnePair
		} else if pairCnt == 1 {
			h.CCT = ThreeOfAKind
		} else if pairCnt == 2 {
			h.CCT = FullHouse
		}
	case 2:
		if hasThree {
			h.CCT = FiveOfAKind
		} else if pairCnt == 0 {
			h.CCT = ThreeOfAKind
		} else if pairCnt == 1 {
			h.CCT = ThreeOfAKind
		} else if pairCnt == 2 {
			h.CCT = FourOfAKind
		}
	case 3:
		if pairCnt == 0 {
			h.CCT = FourOfAKind
		} else if pairCnt == 1 {
			h.CCT = FiveOfAKind
		}
	case 4:
		h.CCT = FiveOfAKind
	}
}

func (h *Hand) updateType() {
	m := make(map[string]int, 0)

	for _, c := range h.Cards {
		m[string(c)] += 1
	}

	pairCnt := 0
	hasThree := false

	if len(m) == 1 {
		h.CCT = FiveOfAKind
	} else if len(m) == 5 {
		h.CCT = HighCard
	} else if len(m) == 4 {
		h.CCT = OnePair
		pairCnt = 1
	} else {
		// 22221
		// 22233
		// 33221
		// 33312
		for _, v := range m {
			if v == 3 {
				hasThree = true
			} else if v == 2 {
				pairCnt += 1
			} else if v == 4 {
				h.CCT = FourOfAKind
				break
			}
		}

		if h.CCT != FourOfAKind {
			if hasThree {
				if pairCnt == 1 {
					h.CCT = FullHouse
				} else {
					h.CCT = ThreeOfAKind
				}
			} else if pairCnt == 2 {
				h.CCT = TwoPair
			}
		}
	}

	h.updateType2(m, pairCnt, hasThree)
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

func getAnswer() uint32 {
	var res uint32

	sort.Slice(hands, func(i, j int) bool {
		return hands[i].Compare(hands[j])
	})

	for i, h := range hands {
		// fmt.Println(i+1, h.Bid, h.Cards, h.CCT)
		res += uint32(i+1) * uint32(h.Bid)
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
