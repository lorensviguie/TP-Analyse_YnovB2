package main

import (
	"encoding/csv"
	"log"
	"os"
	"strconv"
	"time"
	"work/dice"
)

var roll = 1000

func main() {
	file, err := os.OpenFile("donnees.csv", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		log.Fatalf("Impossible d'ouvrir le fichier : %s", err)
	}
	defer file.Close()
	writer := csv.NewWriter(file)
	defer writer.Flush()
	header := []string{"Nom_dé", "Seed", "Rank", "Résultat"}
	if err := writer.Write(header); err != nil {
		log.Fatalf("Impossible d'écrire l'en-tête : %s", err)
	}
	writeDiceData := func(diceType string, rollFunc func(rank int, seed int64) int) {
		for rank := 1; rank <= 10; rank++ {
			for i := 0; i < roll; i++ {
				seed := time.Now().UnixNano()
				result := rollFunc(rank, seed)

				row := []string{
					diceType,
					strconv.FormatInt(seed, 10),
					getDiceName(rank),
					strconv.Itoa(result),
				}
				if err := writer.Write(row); err != nil {
					log.Fatalf("Erreur lors de l'écriture des données dans le fichier : %s", err)
				}
			}
		}
	}
	writeDiceData("base_dice", dice.Roll_Base_Dice)
	writeDiceData("normal_dice", dice.Roll_NormalDice)
	writeDiceData("parabole_dice", dice.Roll_Parabole_Dice)
	writeDiceData("power_dice", dice.Power_Dice)
	writeDiceData("rank_dice", dice.Roll_RankDice)
	writeDiceData("scale_dice", dice.Roll_Scaledice)
	writeDiceData("unscale_dice", dice.Roll_unscaledice)
	log.Println("Données ajoutées au fichier CSV avec succès.")
}

func getDiceName(rank int) string {
	switch rank {
	case 1:
		return "Iron"
	case 2:
		return "Bronze"
	case 3:
		return "Silver"
	case 4:
		return "Gold"
	case 5:
		return "Platinum"
	case 6:
		return "Emerald"
	case 7:
		return "Diamond"
	case 8:
		return "Master"
	case 9:
		return "Grand Master"
	case 10:
		return "Challenger"
	default:
		return ""
	}
}
