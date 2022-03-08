package main

import "fmt"

func _f(nums []int, idx int, subset []int) [][]int {
	if idx == len(nums) {
		r := make([]int, len(subset))
		for i, v := range subset {
			r[i] = v
		}
		return [][]int{r}
	} else {
		c_1 := _f(nums, idx+1, subset)
		subset = append(subset, nums[idx])
		return append(c_1, _f(nums, idx+1, subset)...)
	}
}

func subsets(nums []int) [][]int {
	subset := make([]int, 0)
	return _f(nums, 0, subset)
}

func main() {
	fmt.Println(subsets([]int{1, 2, 3}))
	fmt.Println(subsets([]int{0}))
}
