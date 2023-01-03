package main

func TwiceAsOld(dadYearsOld, sonYearsOld int) int {
	// Implement me
	x := 0 - (sonYearsOld - 1)
	for {
		dadNewOld := dadYearsOld + x
		sonNewOld := sonYearsOld + x
		if dadNewOld == sonNewOld*2 {
			if x < 0 {
				return -x
			}
			return x
		}
		x++
	}
}
