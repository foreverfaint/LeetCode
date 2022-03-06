package main

import "fmt"

func printMatrix(matrix [][]int) {
	for _, row := range matrix {
		fmt.Println((row))
	}
	fmt.Println("----")
}

type Coord struct {
	y int
	x int
}

type Queue struct {
	data []Coord
}

func New() *Queue {
	q := new(Queue)
	q.data = make([]Coord, 0)
	return q
}

func (q *Queue) empty() bool {
	return len(q.data) == 0
}

func (q *Queue) appendAtTail(coord Coord) {
	q.data = append(q.data, coord)
}

func (q *Queue) removeFromHead() Coord {
	first := q.data[0]
	q.data = q.data[1:]
	return first
}

func shortestBridge(grid [][]int) int {
	h := len(grid)
	w := len(grid[0])

	for y := 0; y < h; y++ {
		for x := 0; x < w; x++ {
			if grid[y][x] != 1 {
				continue
			}

			q := New()
			q.appendAtTail(Coord{y, x})

			island_1 := New()
			island_1.appendAtTail(Coord{y, x})

			for !q.empty() {
				coord := q.removeFromHead()
				if grid[coord.y][coord.x] != 1 {
					continue
				}

				grid[coord.y][coord.x] = 2
				for _, d := range [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}} {
					d_y := d[0]
					d_x := d[1]
					n_y := coord.y + d_y
					n_x := coord.x + d_x
					if 0 <= n_y && n_y < h && 0 <= n_x && n_x < w && grid[n_y][n_x] == 1 {
						q.appendAtTail(Coord{n_y, n_x})
						island_1.appendAtTail(Coord{n_y, n_x})
					}
				}
			}

			for !island_1.empty() {
				coord := island_1.removeFromHead()

				for _, d := range [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}} {
					d_y := d[0]
					d_x := d[1]
					n_y := coord.y + d_y
					n_x := coord.x + d_x
					if 0 <= n_y && n_y < h && 0 <= n_x && n_x < w {
						if grid[n_y][n_x] == 1 {
							return grid[coord.y][coord.x] - 2
						} else if grid[n_y][n_x] == 0 {
							grid[n_y][n_x] = grid[coord.y][coord.x] + 1
							island_1.appendAtTail(Coord{n_y, n_x})
						}
					}
				}
			}
		}
	}

	return -1
}

func main() {
	fmt.Println(shortestBridge([][]int{{0, 1}, {1, 0}}))
	fmt.Println(shortestBridge([][]int{{0, 1, 0}, {0, 0, 0}, {0, 0, 1}}))
	fmt.Println(shortestBridge([][]int{{1, 1, 1, 1, 1}, {1, 0, 0, 0, 1}, {1, 0, 1, 0, 1}, {1, 0, 0, 0, 1}, {1, 1, 1, 1, 1}}))
}
