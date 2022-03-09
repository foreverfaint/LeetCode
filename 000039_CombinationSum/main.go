package main

import (
	"fmt"
	"sort"
)

func combinationSum(candidates []int, target int) [][]int {
	sort.SliceStable(candidates, func(i, j int) bool { return candidates[i] < candidates[j] })

	r := make([][]int, 0)
	for i, n := range candidates {
		if n == target {
			r = append(r, []int{n})
		} else if n < target {
			for _, arr := range combinationSum(candidates[i:], target-n) {
				r = append(r, append(arr, n))
			}
		}
	}
	return r
}

func main() {
	fmt.Println(combinationSum([]int{2, 3, 6, 7}, 7))
	fmt.Println(combinationSum([]int{2, 3, 5}, 8))
	fmt.Println(combinationSum([]int{2}, 1))
}
