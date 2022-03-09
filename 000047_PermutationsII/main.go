package main

import (
	"fmt"
)

type Pair struct {
	n1 int
	n2 int
}

func permuteUnique(nums []int) [][]int {
	if len(nums) == 1 {
		return [][]int{{nums[0]}}
	}

	m := make(map[Pair]bool, 0)
	r := make([][]int, 0)
	for i := 0; i < len(nums); i++ {
		_, has := m[Pair{nums[0], nums[i]}]
		if !has {
			m[Pair{nums[0], nums[i]}] = true
			nums[0], nums[i] = nums[i], nums[0]
			for _, arr := range permuteUnique(nums[1:]) {
				r = append(r, append([]int{nums[0]}, arr...))
			}
			nums[0], nums[i] = nums[i], nums[0]
		}
	}
	return r
}

func verify(solutions [][]int) {
	for i := 0; i < len(solutions); i++ {
		for j := i + 1; j < len(solutions); j++ {
			flag := true
			for k, v := range solutions[i] {
				if solutions[j][k] != v {
					flag = false
					break
				}
			}

			if flag {
				fmt.Println(i, j, solutions[i])
				return
			}
		}
	}
}

func main() {
	// [-1,-1,2,-1,1,1,2,2]
	verify(permuteUnique([]int{-1, 2, -1, 2, 1, -1, 2, 1}))
	// fmt.Println(permuteUnique([]int{-1, 2, -1, 2, 1, -1, 2, 1}))
	// fmt.Println(permuteUnique([]int{1, 1, 2}))
	// fmt.Println(permuteUnique([]int{1, 2, 3}))
}
