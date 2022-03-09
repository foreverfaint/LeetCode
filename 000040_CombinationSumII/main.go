package main

import (
	"fmt"
	"sort"
)

func combinationSum2(candidates []int, target int) [][]int {
	sort.SliceStable(candidates, func(i, j int) bool { return candidates[i] < candidates[j] })

	r := make([][]int, 0)
	for i, n := range candidates {
		if n == target {
			if i == 0 || candidates[i] != candidates[i-1] {
				r = append(r, []int{n})
			}
		} else if n < target {
			if i == 0 || candidates[i] != candidates[i-1] {
				for _, arr := range combinationSum2(candidates[i+1:], target-n) {
					// fmt.Println(candidates, target, candidates[i+1:], target-n, arr)
					r = append(r, append([]int{n}, arr...))
				}
			}
		}
	}
	return r
}

func main() {
	fmt.Println(combinationSum2([]int {10,1,2,7,6,1,5}, 8))
	fmt.Println(combinationSum2([]int {2,5,2,1,2}, 5))
	fmt.Println(combinationSum2([]int{2, 5, 2, 1, 2}, 4))
}
