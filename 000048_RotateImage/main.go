package main

import "fmt"

func printMatrix(matrix [][]int) {
	for _, row := range matrix {
		fmt.Println((row))
	}
	fmt.Println("----")
}

func _rotate(matrix [][]int, start_y int, start_x int, l int) {
	if l <= 1 {
		return
	}

	for x := start_x; x < start_x+l-1; x++ {
		y_ := start_y
		x_ := x
		t := matrix[y_][x_]
		for i := 0; i < 4; i++ {
			new_y := x_
			new_x := len(matrix) - 1 - y_
			t, matrix[new_y][new_x] = matrix[new_y][new_x], t
			x_ = new_x
			y_ = new_y
		}
	}

	_rotate(matrix, start_y+1, start_x+1, l-2)
}

func rotate(matrix [][]int) {
	_rotate(matrix, 0, 0, len(matrix))
}

func main() {
	matrix := [][]int{{1}}
	rotate(matrix)
	printMatrix(matrix)

	matrix = [][]int{{1, 2}, {4, 5}}
	rotate(matrix)
	printMatrix(matrix)

	matrix = [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	rotate(matrix)
	printMatrix(matrix)

	matrix = [][]int{{5,1,9,11},{2,4,8,10},{13,3,6,7},{15,14,12,16}}
	rotate(matrix)
	printMatrix(matrix)
}
