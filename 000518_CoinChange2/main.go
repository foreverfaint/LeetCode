package main

import "fmt"

func change(amount int, coins []int) int {
	if amount <= 0 {
		return 0
	}

	last_dp := make([]int, amount+1)
	last_dp[0] = 1

	for j := 0; j < len(coins); j++ {
		coin := coins[j]
		curr_dp := make([]int, amount+1)
		curr_dp[0] = 1

		for i := 1; i <= amount; i++ {
			curr_dp[i] = last_dp[i]
			k := i - coin
			if k >= 0 {
				curr_dp[i] += curr_dp[k]
			}
		}

		last_dp = curr_dp
	}

	return last_dp[amount]
}

func main() {
	fmt.Println(change(3, []int{1, 2}))
	fmt.Println(change(5, []int{1, 2, 5}))
	fmt.Println(change(3, []int{2}))
	fmt.Println(change(10, []int{10}))
}
