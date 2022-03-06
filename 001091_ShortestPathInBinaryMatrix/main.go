package main

import (
	"fmt"
)

type ValuedCoord struct {
	y      int
	x      int
	length int
}

func shortestPathBinaryMatrix(grid [][]int) int {
	h := len(grid)
	w := len(grid[0])

	if grid[0][0] == 1 || grid[h-1][w-1] == 1 {
		return -1
	}

	q := make([]ValuedCoord, 0)
	q = append(q, ValuedCoord{0, 0, 1})

	for len(q) > 0 {
		// BFS garauntees the shortest path reaches the end first.
		first := q[0]

		if first.y == h-1 && first.x == w-1 {
			return first.length
		}

		for _, d_y := range []int{-1, 0, 1} {
			for _, d_x := range []int{-1, 0, 1} {
				if d_y == 0 && d_x == 0 {
					continue
				}

				new_y := first.y + d_y
				new_x := first.x + d_x
				if new_y < 0 || new_y >= h || new_x < 0 || new_x >= w || grid[new_y][new_x] == 1 {
					continue
				}

				// The later visit must generate a longer path than the first visit
				// So no need to revisit the node, just set it to 1
				grid[new_y][new_x] = 1
				q = append(q, ValuedCoord{new_y, new_x, first.length + 1})
			}
		}

		q = q[1:]
	}

	return -1
}

func main() {
	fmt.Println(shortestPathBinaryMatrix([][]int{
		{0, 1, 1, 0, 0, 0},
		{0, 1, 0, 1, 1, 0},
		{0, 1, 1, 0, 1, 0},
		{0, 0, 0, 1, 1, 0},
		{1, 1, 1, 1, 1, 0},
		{1, 1, 1, 1, 1, 0}}))
	fmt.Println(shortestPathBinaryMatrix([][]int{
		{0, 0, 1, 1, 0, 0},
		{0, 0, 0, 0, 1, 1},
		{1, 0, 1, 1, 0, 0},
		{0, 0, 1, 1, 0, 0},
		{0, 0, 0, 0, 0, 0},
		{0, 0, 1, 0, 0, 0}}))
	fmt.Println(shortestPathBinaryMatrix([][]int{{0, 0, 0}, {0, 1, 0}, {0, 0, 0}}))
	fmt.Println(shortestPathBinaryMatrix([][]int{{0, 0, 0}, {1, 0, 0}, {1, 1, 0}}))
	fmt.Println(shortestPathBinaryMatrix([][]int{{0, 1}, {1, 0}}))
	fmt.Println(shortestPathBinaryMatrix([][]int{{0, 0, 0}, {1, 1, 0}, {1, 1, 0}}))
	fmt.Println(shortestPathBinaryMatrix([][]int{{1, 0, 0}, {1, 1, 0}, {1, 1, 0}}))
}
