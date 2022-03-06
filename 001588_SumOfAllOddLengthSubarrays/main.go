package main

import "fmt"

func sumOddLengthSubarrays(arr []int) int {
	prefix_sum := make([]int, len(arr) + 1)
	prefix_sum[0] = 0
	prefix_sum[1] = arr[0]
	for i := 1; i < len(arr); i++ {
		prefix_sum[i + 1] = prefix_sum[i] + arr[i]
	}

	sum := 0
	for l := 1; l <= len(arr); l += 2 {
		for i := 0; i + l <= len(arr); i++ {
			sum += prefix_sum[i + l] - prefix_sum[i]
		}
	}
	return sum
}

func main() {
	fmt.Println(sumOddLengthSubarrays([]int{1, 4, 2, 5, 3}))
	fmt.Println(sumOddLengthSubarrays([]int{1, 2}))
	fmt.Println(sumOddLengthSubarrays([]int{10, 11, 12}))
}
