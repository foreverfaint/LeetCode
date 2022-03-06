package main

import "fmt"

func numSubarrayProductLessThanK(nums []int, k int) int {
	r := 0

	for y := 0; y < len(nums); y++ {
		p := nums[y]
		if p >= k {
			continue
		}

		r += 1
		for x := y + 1; x < len(nums); x++ {
			p *= nums[x]
			if p >= k {
				break
			}
			r += 1
		}
	}

	return r
}

func main() {
	fmt.Println(numSubarrayProductLessThanK([]int{10, 5, 2, 6}, 100))
	fmt.Println(numSubarrayProductLessThanK([]int{1, 2, 3}, 0))
}
