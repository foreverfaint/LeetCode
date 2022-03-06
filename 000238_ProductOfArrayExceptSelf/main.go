package main

import "fmt"

func productExceptSelf(nums []int) []int {
	p_prefix := make([]int, len(nums))
	p_prefix[0] = nums[0]

	p_suffix := make([]int, len(nums))
	p_suffix[len(nums)-1] = nums[len(nums)-1]

	for i, j := 1, len(nums)-2; i < len(nums); i, j = i+1, j-1 {
		p_prefix[i] = nums[i] * p_prefix[i-1]
		p_suffix[j] = nums[j] * p_suffix[j+1]
	}

	ans := make([]int, len(nums))
	for i := 0; i < len(nums); i++ {
		ans[i] = 1
		if i - 1 >= 0 {
			ans[i] *= p_prefix[i - 1]
		}
		if i + 1 < len(nums) {
			ans[i] *= p_suffix[i + 1]
		}
	}
	return ans
}

func main() {
	fmt.Println(productExceptSelf([]int{1, 2, 3, 4}))
	fmt.Println(productExceptSelf([]int{-1, 1, 0, -3, 3}))
}
