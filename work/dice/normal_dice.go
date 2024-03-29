package dice

import "math/rand"

func Roll_NormalDice(rank int, seed int64) int {
	rank++
	rand.Seed(seed)
	return rand.Intn(20) + 1
}
