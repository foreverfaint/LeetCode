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

func solve(board [][]byte) {
	h := len(board)
	w := len(board[0])

	q := New()

	for x := 0; x < w; x++ {
		if board[0][x] == 'O' {
			q.appendAtTail(Coord{0, x})
		}
		if board[h-1][x] == 'O' {
			q.appendAtTail(Coord{h - 1, x})
		}
	}

	for y := 1; y < h-1; y++ {
		if board[y][0] == 'O' {
			q.appendAtTail(Coord{y, 0})
		}
		if board[y][w-1] == 'O' {
			q.appendAtTail(Coord{y, w - 1})
		}
	}

	for !q.empty() {
		coord := q.removeFromHead()
		board[coord.y][coord.x] = 'K'

		for _, dir := range []Coord{{-1, 0}, {1, 0}, {0, -1}, {0, 1}} {
			new_y := coord.y + dir.y
			new_x := coord.x + dir.x
			if 0 <= new_y && new_y <= h-1 && 0 <= new_x && new_x <= w-1 && board[new_y][new_x] == 'O' {
				q.appendAtTail(Coord{new_y, new_x})
			}
		}
	}

	for y := 0; y < h; y++ {
		for x := 0; x < w; x++ {
			if board[y][x] == 'O' {
				board[y][x] = 'X'
			}
		}
	}

	for y := 0; y < h; y++ {
		for x := 0; x < w; x++ {
			if board[y][x] == 'K' {
				board[y][x] = 'O'
			}
		}
	}
}

func main() {
	board := [][]byte{{byte('X'), byte('X'), byte('X'), byte('X')}, {byte('X'), byte('O'), byte('O'), byte('X')}, {byte('X'), byte('X'), byte('O'), byte('X')}, {byte('X'), byte('O'), byte('X'), byte('X')}}
	solve(board)
	fmt.Println(board)

	board = [][]byte{{byte('X')}}
	solve(board)
	fmt.Println(board)
}
