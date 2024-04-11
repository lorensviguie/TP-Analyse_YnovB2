package main

import (
	"encoding/csv"
	"log"
	"os"
	"strconv"
	"time"
	"work/dice"
)

func main() {
	// Ouvrir le fichier CSV en mode ajout
	file, err := os.OpenFile("donnees.csv", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		log.Fatalf("Impossible d'ouvrir le fichier : %s", err)
	}
	defer file.Close()

	// Créer un écrivain CSV
	writer := csv.NewWriter(file)
	defer writer.Flush()

	// Effectuer 1000 lancers de dé pour chaque rang du dé
	for rank := 1; rank <= 10; rank++ {
		for i := 0; i < 1000; i++ {
			seed := time.Now().UnixNano()
			result := dice.Roll_Base_Dice(rank, seed)

			row := []string{
				"base_dice",
				strconv.FormatInt(seed, 10),
				getDiceName(rank),
				strconv.Itoa(result),
			}

			if err := writer.Write(row); err != nil {
				log.Fatalf("Erreur lors de l'écriture des données dans le fichier : %s", err)
			}
		}
	}
	for rank := 1; rank <= 10; rank++ {
		for i := 0; i < 1000; i++ {
			seed := time.Now().UnixNano()
			result := dice.Roll_NormalDice(rank, seed)

			row := []string{
				"normal_dice",
				strconv.FormatInt(seed, 10),
				getDiceName(rank),
				strconv.Itoa(result),
			}

			if err := writer.Write(row); err != nil {
				log.Fatalf("Erreur lors de l'écriture des données dans le fichier : %s", err)
			}
		}
	}
	for rank := 1; rank <= 10; rank++ {
		for i := 0; i < 1000; i++ {
			seed := time.Now().UnixNano()
			result := dice.Roll_Parabole_Dice(rank, seed)

			row := []string{
				"parabole_dice",
				strconv.FormatInt(seed, 10),
				getDiceName(rank),
				strconv.Itoa(result),
			}

			if err := writer.Write(row); err != nil {
				log.Fatalf("Erreur lors de l'écriture des données dans le fichier : %s", err)
			}
		}
	}
	for rank := 1; rank <= 10; rank++ {
		for i := 0; i < 1000; i++ {
			seed := time.Now().UnixNano()
			result := dice.Power_Dice(rank, seed)

			row := []string{
				"power_dice",
				strconv.FormatInt(seed, 10),
				getDiceName(rank),
				strconv.Itoa(result),
			}

			if err := writer.Write(row); err != nil {
				log.Fatalf("Erreur lors de l'écriture des données dans le fichier : %s", err)
			}
		}
	}
	for rank := 1; rank <= 10; rank++ {
		for i := 0; i < 1000; i++ {
			seed := time.Now().UnixNano()
			result := dice.Roll_RankDice(rank, seed)

			row := []string{
				"rank_dice",
				strconv.FormatInt(seed, 10),
				getDiceName(rank),
				strconv.Itoa(result),
			}

			if err := writer.Write(row); err != nil {
				log.Fatalf("Erreur lors de l'écriture des données dans le fichier : %s", err)
			}
		}
	}
	for rank := 1; rank <= 10; rank++ {
		for i := 0; i < 1000; i++ {
			seed := time.Now().UnixNano()
			result := dice.Roll_Scaledice(rank, seed)

			row := []string{
				"scale_dice",
				strconv.FormatInt(seed, 10),
				getDiceName(rank),
				strconv.Itoa(result),
			}

			if err := writer.Write(row); err != nil {
				log.Fatalf("Erreur lors de l'écriture des données dans le fichier : %s", err)
			}
		}
	}
	for rank := 1; rank <= 10; rank++ {
		for i := 0; i < 1000; i++ {
			seed := time.Now().UnixNano()
			result := dice.Roll_unscaledice(rank, seed)

			row := []string{
				"unscale_dice",
				strconv.FormatInt(seed, 10),
				getDiceName(rank),
				strconv.Itoa(result),
			}

			if err := writer.Write(row); err != nil {
				log.Fatalf("Erreur lors de l'écriture des données dans le fichier : %s", err)
			}
		}
	}

	log.Println("Données ajoutées au fichier CSV avec succès.")
}

// getDiceName retourne le nom du dé en fonction de son rang
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
