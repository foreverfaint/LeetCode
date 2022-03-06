package main

import "fmt"
func printMatrix(matrix [][]byte) {
	h := len(matrix)
	for y := 0; y < h; y++ {
		fmt.Println(matrix[y])
	}
}

func genSubMatrix(matrix [][]byte) [][]byte {
	h := len(matrix)
	w := len(matrix[0])

	subM := make([][]byte, h-1)
	for y := 1; y < h; y++ {
		subM[y-1] = make([]byte, w-1)
		for x := 1; x < w; x++ {
			if matrix[y-1][x-1] == 1 && matrix[y-1][x] == 1 && matrix[y][x-1] == 1 && matrix[y][x] == 1 {
				subM[y-1][x-1] = 1
			} else {
				subM[y-1][x-1] = 0
			}
		}
	}
	return subM
}

func countOnes(matrix [][]byte) int {
	h := len(matrix)
  if h == 0 {
    return 0  
  }
  
	w := len(matrix[0])
  if w == 0 {
    return 0
  }
  
	c := 0
	for y := 0; y < h; y++ {
		for x := 0; x < w; x++ {
			if matrix[y][x] == 1 {
				c++
			}
		}
	}
	return c
}

func maximalSquare(matrix [][]byte) int {
	h := len(matrix)
	w := len(matrix[0])
	for y := 0; y < h; y++ {
		for x := 0; x < w; x++ {
			matrix[y][x] = matrix[y][x] - 48
		}
	}

	area := 1
	subM := matrix
	ones := countOnes(matrix)
	for ; ones > 0; area++ {
		subM = genSubMatrix(subM)
		ones = countOnes(subM)
	}
	return (area - 1) * (area - 1)
}

func main() {
	fmt.Println(maximalSquare([][]byte{
		{1, 0, 1, 0, 0}, 
		{1, 0, 1, 1, 1}, 
		{1, 1, 1, 1, 1}, 
		{1, 0, 0, 1, 0}}))
	// fmt.Println(maximalSquare([][]byte{{1, 0, 1, 0, 0}, {1, 0, 1, 1, 1}, {1, 1, 1, 1, 1}, {1, 0, 0, 1, 0}}))
	// fmt.Println(maximalSquare([][]byte{{0, 1}, {1, 0}}))
	// fmt.Println(maximalSquare([][]byte{{0}}))
}
