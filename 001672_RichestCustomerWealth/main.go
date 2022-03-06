package main

import "fmt"

func sum(a []int) int {
	r := 0
	for _, v := range a {
		r += v
	}
	return r
}

func maximumWealth(accounts [][]int) int {
	max_wealth := sum(accounts[0])
    for _, money_list := range accounts {
		wealth := sum(money_list)
		if wealth > max_wealth {
			max_wealth = wealth
		}
	}
	return max_wealth
}

func main() {
    fmt.Println(maximumWealth([][]int {{ 1,2,3},{3,2,1 }}))
	fmt.Println(maximumWealth([][]int {{ 1,5},{7,3},{3,5}}))
	fmt.Println(maximumWealth([][]int {{ 2,8,7},{7,1,3},{1,9,5 }}))
}