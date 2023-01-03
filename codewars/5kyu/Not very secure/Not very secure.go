package main

import "unicode"

func alphanumeric(str string) bool {
	if len(str) == 0 {
		return false
	}

	for _, c := range str {
		if !(unicode.IsLetter(c) || unicode.IsDigit(c)) {
			return false
		}
	}
	return true
}
