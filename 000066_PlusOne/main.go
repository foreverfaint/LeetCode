package main

import "fmt"

func plusOne(digits []int) []int {
	result := make([]int, len(digits)+1)
	result[len(digits)] = 1
	for i := len(digits) - 1; i >= 0; i-- {
		result[i+1] = digits[i] + result[i+1]
		if result[i+1] > 9 {
			result[i+1] = result[i+1] - 10
			result[i] = 1
		}
	}

	if result[0] == 0 {
		return result[1:]
	}
	return result
}

func main() {
	fmt.Println(plusOne([]int{1, 2, 3}))
	fmt.Println(plusOne([]int{4, 3, 2, 1}))
	fmt.Println(plusOne([]int{9}))
}
