package main

import (
	"fmt"
	"sort"
)

func _f(nums []int) [][]int {
	if len(nums) == 0 {
		return [][]int{}
	}

	if len(nums) == 1 {
		return [][]int{{nums[0]}}
	}

	r := make([][]int, 0)
	for i := 0; i < len(nums); i++ {
		if i == 0 || nums[i] != nums[i-1] {
			r = append(r, []int{nums[i]})
			for _, arr := range _f(nums[i+1:]) {
				arr = append(arr, nums[i])
				r = append(r, arr)
			}
		}
	}

	return r
}

func subsetsWithDup(nums []int) [][]int {
	sort.SliceStable(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})
	return append(_f(nums), []int {})
}

func main() {
	fmt.Println(subsetsWithDup([]int{1, 2, 2}))
	fmt.Println(subsetsWithDup([]int{0}))
}
