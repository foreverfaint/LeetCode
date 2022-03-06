package main

import "fmt"

func sortColors(nums []int) {
	i := 0
	j := len(nums)
	for ; i < j; i++ {
		if nums[i] > 0 {
			for ; i < j; j-- {
				if nums[j-1] == 0 {
					nums[i], nums[j-1] = nums[j-1], nums[i]
					break
				}
			}
		}
	}

	i = j
	j = len(nums)
	for ; i < j; i++ {
		if nums[i] > 1 {
			for ; i < j; j-- {
				if nums[j-1] == 1 {
					nums[i], nums[j-1] = nums[j-1], nums[i]
					break
				}
			}
		}
	}
}

func main() {
	nums := []int{2, 0, 2, 1, 1, 0}
	sortColors(nums)
	fmt.Println(nums)

	nums = []int{2, 0, 1}
	sortColors(nums)
	fmt.Println(nums)
}
