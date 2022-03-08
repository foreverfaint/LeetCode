package main

import "fmt"

func canReach(arr []int, start int) bool {
	d := arr[start]
	if d == -1 {
		return false
	}

	if d == 0 {
		return true
	}

	arr[start] = -1

	if start+d < len(arr) {
		if canReach(arr, start+d) {
			return true
		}
	}

	if start-d >= 0 {
		if canReach(arr, start-d) {
			return true
		}
	}

	return false
}

func main() {
	fmt.Println(canReach([]int{4, 2, 3, 0, 3, 1, 2}, 5))
	fmt.Println(canReach([]int{4, 2, 3, 0, 3, 1, 2}, 0))
	fmt.Println(canReach([]int{3, 0, 2, 1, 2}, 2))
}
