package main

import "fmt"

func subarraySum(nums []int, k int) int {
	sum := make([]int, len(nums)+1)
	sum[0] = 0
	for i := 1; i <= len(nums); i++ {
		sum[i] = sum[i-1] + nums[i-1]
	}
	fmt.Println(sum)

	r := 0
	for i := 0; i < len(sum)-1; i++ {
		for j := len(sum) - 1; j > i; j-- {
			v := sum[j] - sum[i]
			if v == k {
				r++
			}
		}
	}
	return r
}

func main() {
	fmt.Println(subarraySum([]int{1,-1,0}, 0))
	fmt.Println(subarraySum([]int{-1,-1,1}, 0))
	fmt.Println(subarraySum([]int{1}, 0))
	fmt.Println(subarraySum([]int{1, 1, 1}, 2))
	fmt.Println(subarraySum([]int{1, 2, 3}, 3))
}
