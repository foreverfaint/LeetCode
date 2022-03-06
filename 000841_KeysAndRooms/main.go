package main

import "fmt"

type Visited struct {
	data map[int]bool
}

func New() *Visited {
	visited := new(Visited)
	visited.data = make(map[int]bool, 0)
	visited.data[0] = true
	return visited
}

func (visited *Visited) size() int {
	return len(visited.data)
}

func (visited *Visited) notVisitYet(node int) bool {
	_, has := visited.data[node]
	return has
}

func (visited *Visited) visit(node int) {
	visited.data[node] = true
}

func dfs(rooms [][]int, node int, visited *Visited) {
	for _, child := range rooms[node] {
		if !visited.notVisitYet(child) {
			visited.visit(child)
			dfs(rooms, child, visited)
		}
	}
}

func canVisitAllRooms(rooms [][]int) bool {
	visited := New()
	dfs(rooms, 0, visited)
	return visited.size() == len(rooms)
}

func main() {
	fmt.Println(canVisitAllRooms([][]int{{1}, {2}, {3}, {}}))
	fmt.Println(canVisitAllRooms([][]int{{1, 3}, {3, 0, 1}, {2}, {0}}))
}
