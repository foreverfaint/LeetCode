package main

import "fmt"

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func minPathSum(grid [][]int) int {
    r := make([]int, len(grid[0]))
	for i := 0; i < len(r); i++ {
		if i == 0 {
			r[i] = grid[0][0]
		} else {
			r[i] = grid[0][i] + r[i - 1]
		}
	}

	fmt.Println(r)

	for i := 1; i < len(grid); i++ {
		for j := 0; j < len(r); j++ {
			if j == 0 {
				r[j] = r[j] + grid[i][0]
			} else {
				r[j] = min(r[j - 1], r[j]) + grid[i][j]
			}
		}
		fmt.Println(r)
	}

	return r[len(r) - 1]
}

func main() {
	fmt.Println(minPathSum([][]int {{1,2}, {1, 1}}))
    fmt.Println(minPathSum([][]int {{1,3,1}, {1,5,1}, {4,2,1}}))
	fmt.Println(minPathSum([][]int {{1,2,3}, {4,5,6}}))
}