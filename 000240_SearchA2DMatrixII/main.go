package main

import "fmt"


func searchMatrix(matrix [][]int, target int) bool {
	for y, x := 0, len(matrix[0]) - 1; y < len(matrix) && x >= 0; {
		if matrix[y][x] == target {
			return true
		} else if matrix[y][x] < target {
			y++
		} else {
			x--
		}
	}
	return false
}

func main() {
	fmt.Println(searchMatrix([][]int{
		{1, 4, 7, 11, 15}, 
		{2, 5, 8, 12, 19}, 
		{3, 6, 9, 16, 22}, 
		{10, 13, 14, 17, 24}, 
		{18, 21, 23, 26, 30}}, 5))
	fmt.Println(searchMatrix([][]int{
		{1, 4, 7, 11, 15}, 
		{2, 5, 8, 12, 19}, 
		{3, 6, 9, 16, 22}, 
		{10, 13, 14, 17, 24}, 
		{18, 21, 23, 26, 30}}, 20))
}
