package main

import "fmt"

func isAlienSorted(words []string, order string) bool {
	order_ := make(map[byte]int, 0)
	for i := 0; i < len(order); i++ {
		order_[order[i]] = i
	}

	for i := 0; i < len(words)-1; i++ {
		w1 := words[i]
		w2 := words[i+1]
		for j := 0; j < len(w1); j++ {
			if j >= len(w2) {
				return false
			}
			if order_[w1[j]] > order_[w2[j]] {
				return false
			} else if order_[w1[j]] < order_[w2[j]] {
				break
			}
		}
	}
	return true
}

func main() {
	fmt.Println(isAlienSorted([]string{"hello", "leetcode"}, "hlabcdefgijkmnopqrstuvwxyz"))
	fmt.Println(isAlienSorted([]string{"word", "world", "row"}, "worldabcefghijkmnpqstuvxyz"))
	fmt.Println(isAlienSorted([]string{"apple", "app"}, "abcdefghijklmnopqrstuvwxyz"))
	fmt.Println(isAlienSorted([]string{"apple", "apple", "app"}, "abcdefghijklmnopqrstuvwxyz"))
}
