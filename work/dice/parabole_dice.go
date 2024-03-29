package dice

import "math/rand"


func Roll_Parabole_Dice(rank int,seed int64) int {
	rand.Seed(seed)
    switch rank {
    case 1:
        if rand.Float64()*100 <= 50 {
            return rand.Intn(11) + 10
        }
    case 2:
        if rand.Float64()*100 <= 25 {
            return rand.Intn(11) + 10
        }
    case 3:
        if rand.Float64()*100 <= 12.5 {
            return rand.Intn(11) + 10
        }
    case 4:
        if rand.Float64()*100 <= 8.25 {
            return rand.Intn(11) + 10
        }
    case 5:
        if rand.Float64()*100 <= 4.125 {
            return rand.Intn(11) + 10
        }
    case 6:
        if rand.Float64()*100 <= 8.25 {
            return rand.Intn(11) + 10
        }
    case 7:
        if rand.Float64()*100 <= 12.5 {
            return rand.Intn(11) + 10
        }
    case 8:
        if rand.Float64()*100 <= 25 {
            return rand.Intn(11) + 10
        }
    case 9:
        if rand.Float64()*100 <= 50 {
            return rand.Intn(11) + 10
        }
    case 10:
        if rand.Float64()*100 <= 25 {
            return rand.Intn(11) + 10
        }
    }
    return 0
}