package main

import "fmt"

func minSubArrayLen(target int, nums []int) int {
    r := 0
	for i:=0; i <len(nums); i++ {
		s := nums[i]
		if s >= target {
			return 1
		}

		for j:=i+1; j < len(nums); j++ {
			s += nums[j]
			if s >= target {
				l := j - i + 1
				if r == 0 {
					r = l
				} else if r > l {
					r = l
				}
			}
		}
	}
	return r
}

func main() {
    fmt.Println(minSubArrayLen(7, []int {2,3,1,2,4,3}))
    fmt.Println(minSubArrayLen(4, []int {1,4,4}))
	fmt.Println(minSubArrayLen(11, []int {1,1,1,1,1,1,1,1}))
}