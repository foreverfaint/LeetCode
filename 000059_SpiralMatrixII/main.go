package main

import "fmt"

func printMatrix(matrix [][]int) {
	for _, row := range matrix {
		fmt.Println((row))
	}
	fmt.Println("---")
}

func _generateMatrix(matrix *[][]int, start int, l int, i int) {
	if l < 1 {
		return
	}

	if l == 1 {
		(*matrix)[start][start] = i
		return
	}

	n := start + l
	for y, x := start, start; x < n; x++ {
		(*matrix)[y][x] = i
		i++
	}

	for y, x := start+1, n-1; y < n; y++ {
		(*matrix)[y][x] = i
		i++
	}

	for y, x := n-1, n-2; x >= start; x-- {
		(*matrix)[y][x] = i
		i++
	}

	for y, x := n-2, start; y >= start+1; y-- {
		(*matrix)[y][x] = i
		i++
	}

	_generateMatrix(matrix, start+1, l-2, i)
}

func generateMatrix(n int) [][]int {
	matrix := make([][]int, n)
	for y := 0; y < n; y++ {
		matrix[y] = make([]int, n)
	}

	_generateMatrix(&matrix, 0, n, 1)
	return matrix
}

func main() {
	printMatrix(generateMatrix(1))
	printMatrix(generateMatrix(3))
	printMatrix(generateMatrix(5))
	printMatrix(generateMatrix(7))
	printMatrix(generateMatrix(8))
}
