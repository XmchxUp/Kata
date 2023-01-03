package main

func IsValidWalk(walk []rune) bool {
	if len(walk) != 10 {
		return false
	}
	i, j := 0, 0
	for _, dir := range walk {
		switch dir {
		case 'n':
			i++
		case 's':
			i--
		case 'w':
			j--
		case 'e':
			j++
		}
	}
	return i == 0 && j == 0
}
