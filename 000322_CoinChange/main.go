package main

import (
	"fmt"
)

func min(a int, b int, c int) int {
	if a <= b && a <= c {
		return a
	} else if b <= a && b <= c {
		return b
	} else {
		return c
	}
}

func coinChange(coins []int, amount int) int {
	r := make([]int, amount+1)
	r[0] = 0
	for i := 1; i < len(r); i++ {
		r[i] = -1
	}

	for i := 1; i <= amount; i++ {
		for j := 0; j < len(coins); j++ {
			if coins[j] == i {
				r[i] = 1
			} else if coins[j] < i {
				dp := r[i-coins[j]]
				if dp > -1 {
					if r[i] == -1 || r[i] > dp+1 {
						r[i] = dp + 1
					}
				}
			}
		}
	}
	return r[amount]
}

func main() {
	fmt.Println(coinChange([]int{1, 2, 5}, 11))
	fmt.Println(coinChange([]int{2}, 3))
	fmt.Println(coinChange([]int{1}, 0))
}
