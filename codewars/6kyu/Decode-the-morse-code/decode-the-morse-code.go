package main

import (
	"fmt"
	"strings"
)

const (
	A         = ".-"
	B         = "-..."
	C         = "-.-."
	D         = "-.."
	E         = "."
	AccentedE = "..-.."
	F         = "..-."
	G         = "--."
	H         = "...."
	I         = ".."
	J         = ".---"
	K         = "-.-"
	L         = ".-.."
	M         = "--"
	N         = "-."
	O         = "---"
	P         = ".--."
	Q         = "--.-"
	R         = ".-."
	S         = "..."
	T         = "-"
	U         = "..-"
	V         = "...-"
	W         = ".--"
	X         = "-..-"
	Y         = "-.--"
	Z         = "--.."

	One   = ".----"
	Two   = "..---"
	Three = "...--"
	Four  = "....-"
	Five  = "....."
	Six   = "-...."
	Seven = "--..."
	Eight = "---.."
	Nine  = "----."
	Zero  = "-----"

	Period       = ".-.-.-" //.
	Comma        = "--..--" //,
	Colon        = "---..." //:
	QuestionMark = "..--.." //?
	Apostrophe   = ".----." //'
	Hyphen       = "-....-" //-
	Division     = "-..-."  ///
	LeftBracket  = "-.--."  //(
	RightBracket = "-.--.-" //)
	IvertedComma = ".-..-." //“ ”
	DoubleHyphen = "-...-"  //=
	Cross        = ".-.-."  //+
	CommercialAt = ".--.-." //@

	Understood           = "...-."
	Error                = "........"
	InvitationToTransmit = "-.-"
	Wait                 = ".-..."
	EndOfWork            = "...-.-"
	StartingSignal       = "-.-.-"
	SOS                  = "...---..."

	Space = " "
)

var SpecialMoseDictionary = map[string]string{
	"SOS": SOS,
}

var ReversedSpecialMoseDictionary = reverseMorseDictionary(SpecialMoseDictionary)

var DefaultMoseDictionary = map[rune]string{
	'A': A,
	'B': B,
	'C': C,
	'D': D,
	'E': E,
	'F': F,
	'G': G,
	'H': H,
	'I': I,
	'J': J,
	'K': K,
	'L': L,
	'M': M,
	'N': N,
	'O': O,
	'P': P,
	'Q': Q,
	'R': R,
	'S': S,
	'T': T,
	'U': U,
	'V': V,
	'W': W,
	'X': X,
	'Y': Y,
	'Z': Z,

	'1': ".----",
	'2': "..---",
	'3': "...--",
	'4': "....-",
	'5': ".....",
	'6': "-....",
	'7': "--...",
	'8': "---..",
	'9': "----.",
	'0': "-----",

	'.':  ".-.-.-",
	',':  "--..--",
	':':  "---...",
	'?':  "..--..",
	'\'': ".----.",
	'-':  "-....-",
	'/':  "-..-.",
	'(':  "-.--.",
	')':  "-.--.-",
	'“':  ".-..-.",
	'=':  "-...-",
	'+':  ".-.-.",
	'@':  ".--.-.",
	'!':  "-.-.--",
	' ':  Space,
}

var ReversedDefaultMoseDictionary = reverseMorseDictionary(DefaultMoseDictionary)

func reverseMorseDictionary[T comparable, U comparable](m map[T]U) map[U]T {
	res := make(map[U]T)
	for k, v := range m {
		res[v] = k
	}
	return res
}

func DecodeMorse(morseCode string) string {
	var sb strings.Builder

	words := strings.Split(morseCode, Space+Space+Space)

	for _, word := range words {
		chs := strings.Split(strings.TrimSpace(word), Space)
		for _, ch := range chs {
			if text, ok := ReversedDefaultMoseDictionary[ch]; ok {
				sb.WriteRune(text)
				continue
			}

			if text, ok := ReversedSpecialMoseDictionary[ch]; ok {
				sb.WriteString(text)
				continue
			}
		}
		sb.WriteRune(' ')
	}

	return strings.TrimSpace(sb.String())
}

func main() {
	fmt.Println(DecodeMorse(".... . -.--   .--- ..- -.. ."))
	fmt.Println(DecodeMorse("      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-"))
}
