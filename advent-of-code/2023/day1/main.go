package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode"
)

var (
	digitLetterToVal = map[string]uint32{
		"one":   1,
		"two":   2,
		"three": 3,
		"four":  4,
		"five":  5,
		"six":   6,
		"seven": 7,
		"eight": 8,
		"nine":  9,
	}
)

func getDigit(chs []rune, idx int, reverse bool) (uint32, bool) {
	if unicode.IsDigit(chs[idx]) {
		return uint32(chs[idx] - '0'), true
	}

	if !reverse {
		if idx+3 < len(chs) {
			digt3Str := string(chs[idx : idx+3])
			val, ok := digitLetterToVal[digt3Str]
			if ok {
				return val, true
			}
		}

		if idx+4 < len(chs) {
			digt4Str := chs[idx : idx+4]
			val, ok := digitLetterToVal[string(digt4Str)]
			if ok {
				return val, true
			}
		}

		if idx+5 < len(chs) {
			digt5Str := chs[idx : idx+5]
			val, ok := digitLetterToVal[string(digt5Str)]
			if ok {
				return val, true
			}
		}
	} else {
		if idx-3 >= 0 {
			digt3Str := string(chs[idx-2 : idx+1])
			val, ok := digitLetterToVal[digt3Str]
			if ok {
				return val, true
			}
		}

		if idx-4 >= 0 {
			digt4Str := chs[idx-3 : idx+1]
			val, ok := digitLetterToVal[string(digt4Str)]
			if ok {
				return val, true
			}
		}

		if idx-5 >= 0 {
			digt5Str := chs[idx-4 : idx+1]
			val, ok := digitLetterToVal[string(digt5Str)]
			if ok {
				return val, true
			}
		}

	}

	return 0, false
}

func getCalibrationValue(line string) uint32 {
	chs := []rune(line)
	var digt1, digt2 uint32
	var ok bool
	idx1, idx2 := 0, len(chs)-1
	for idx1 < len(line) {
		if digt1, ok = getDigit(chs, idx1, false); ok {
			break
		}
		idx1++
	}

	for idx2 > -1 {
		if digt2, ok = getDigit(chs, idx2, true); ok {
			break
		}
		idx2--
	}

	if idx2 == -1 { // no digit
		return 0
	}

	return digt1*10 + digt2
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	result := 0

	for scanner.Scan() {
		line := scanner.Text()
		if line == "END" {
			break
		}
		result += int(getCalibrationValue(line))
	}

	fmt.Println("answer is:", result)
}
