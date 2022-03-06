package main

import "fmt"

func diagonalSum(mat [][]int) int {
	sum := 0
	l := len(mat)
	for i := 0; i < l; i++ {
		sum += mat[i][i] + mat[i][l-1-i]
	}

	if l%2 == 1 {
		sum -= mat[l/2][l/2]
	}
	return sum
}

func main() {
	fmt.Println(diagonalSum([][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}))
	fmt.Println(diagonalSum([][]int{{1, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 1}}))
	fmt.Println(diagonalSum([][]int{{5}}))
}
