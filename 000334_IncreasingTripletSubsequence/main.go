package main

import "fmt"


func increasingTriplet(nums []int) bool {
	l := len(nums)
	if l < 3 {
		return false
	}

	min := make([]int, l)
	max := make([]int, l)

	min[0] = nums[0]
	for i := 1; i < l; i++ {
		if min[i-1] > nums[i] {
			min[i] = nums[i]
		} else {
			min[i] = min[i-1]
		}
	}

	max[l-1] = nums[l-1]
	for i := l - 2; i >= 0; i-- {
		if max[i+1] < nums[i] {
			max[i] = nums[i]
		} else {
			max[i] = max[i+1]
		}
	}

	for i := 1; i < l-1; i++ {
		if nums[i] > min[i] && nums[i] < max[i] {
			return true
		}
	}

	return false
}

func main() {
	fmt.Println(increasingTriplet([]int{1, 2, 3, 4, 5}))
	fmt.Println(increasingTriplet([]int{5, 4, 3, 2, 1}))
	fmt.Println(increasingTriplet([]int{2, 1, 5, 0, 4, 6}))
}
