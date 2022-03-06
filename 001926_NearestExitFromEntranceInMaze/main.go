package main

import "fmt"

func printMatrix(matrix [][]byte) {
	for _, row := range matrix {
		fmt.Println((row))
	}
	fmt.Println("----")
}

type LevelCoord struct {
	y   int
	x   int
	lvl int
}

type Queue struct {
	data []LevelCoord
}

func New() *Queue {
	q := new(Queue)
	q.data = make([]LevelCoord, 0)
	return q
}

func (q *Queue) empty() bool {
	return len(q.data) == 0
}

func (q *Queue) appendAtTail(LevelCoord LevelCoord) {
	q.data = append(q.data, LevelCoord)
}

func (q *Queue) removeFromHead() LevelCoord {
	first := q.data[0]
	q.data = q.data[1:]
	return first
}

func nearestExit(maze [][]byte, entrance []int) int {
	const empty = 46
	const wall = 43

	h := len(maze)
	w := len(maze[0])

	q := New()
	q.appendAtTail(LevelCoord{entrance[0], entrance[1], 0})
	maze[entrance[0]][entrance[1]] = wall

	for !q.empty() {
		levelCoord := q.removeFromHead()

		for _, d := range [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}} {
			d_y := d[0]
			d_x := d[1]
			n_y := levelCoord.y + d_y
			n_x := levelCoord.x + d_x
			if 0 <= n_y && n_y < h && 0 <= n_x && n_x < w && maze[n_y][n_x] == empty {
				if n_x == w-1 || n_x == 0 || n_y == h-1 || n_y == 0 {
					return levelCoord.lvl + 1
				}
				q.appendAtTail(LevelCoord{n_y, n_x, levelCoord.lvl + 1})
				maze[n_y][n_x] = wall
			}
		}
	}

	return -1
}

func main() {
	fmt.Println(nearestExit([][]byte{{'+', '+', '.', '+'}, {'.', '.', '.', '+'}, {'+', '+', '+', '.'}}, []int{1, 2}))
	fmt.Println(nearestExit([][]byte{{'+', '+', '+'}, {'.', '.', '.'}, {'+', '+', '+'}}, []int{1, 0}))
	fmt.Println(nearestExit([][]byte{{'.', '+'}}, []int{0, 0}))
}
