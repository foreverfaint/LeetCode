package main

import "fmt"

func min(a int, b int, c int) int {
	if a <= b && a <= c {
		return a
	} else if b <= a && b <= c {
		return b
	} else {
		return c
	}
}

func minDistance(word1 string, word2 string) int {
	l_1 := len(word1)
	l_2 := len(word2)

	if l_1 == 0 {
		return l_2
	}

	if l_2 == 0 {
		return l_1
	}

	cost := make([][]int, l_1 + 1)
	for y := 0; y <= l_1; y++ {
		cost[y] = make([]int, l_2 + 1)
		for x:= 0; x <= l_2; x++ {
			cost[y][x] = x
		}
		cost[y][0] = y
	}

	for y := 0; y < l_1; y++ {
		for x := 0; x < l_2; x++ {
			if word1[y] == word2[x] {
				cost[y + 1][x + 1] = cost[y][x]
			} else {
				cost[y + 1][x + 1]= min(cost[y][x], cost[y][x + 1], cost[y+1][x]) + 1
			}
		}
	}

	return cost[l_1][l_2]
}

func main() {
	fmt.Println(minDistance("sea", "ate"))
	fmt.Println(minDistance("horse", "ros"))
	fmt.Println(minDistance("intention", "execution"))
}
