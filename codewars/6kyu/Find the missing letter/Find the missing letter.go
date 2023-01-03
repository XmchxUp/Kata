package main

func FindMissingLetter(chars []rune) rune {
	for i := 0; i < len(chars)-1; i++ {
		if chars[i]+1 != chars[i+1] {
			return chars[i] + 1
		}
	}
	return chars[len(chars)-1] + 1
}

func main() {

}
