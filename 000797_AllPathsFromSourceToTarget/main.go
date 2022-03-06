package main

import "fmt"

type Path struct {
	data []int
}

func New() *Path {
	p := new(Path)
	p.data = make([]int, 0)
	p.push(0)
	return p
}

func (path *Path) push(node int) {
	path.data = append(path.data, node)
}

func (path *Path) pop() {
	path.data = path.data[:len(path.data)-1]
}

func (path *Path) toArray() []int {
	data := make([]int, len(path.data))
	for i, v := range path.data {
		data[i] = v
	}
	return data
}

func (path *Path) print() {
	fmt.Println(path.data)
}

type PathList struct {
	data [][]int
}

func dfs(graph [][]int, node int, path *Path, pathList *PathList) {
	if node == len(graph)-1 {
		pathList.data = append(pathList.data, path.toArray())
		return
	}

	for _, child := range graph[node] {
		path.push(child)
		dfs(graph, child, path, pathList)
		path.pop()
	}
}

func allPathsSourceTarget(graph [][]int) [][]int {
	pathList := new(PathList)
	pathList.data = make([][]int, 0)
	dfs(graph, 0, New(), pathList)
	return pathList.data
}

func main() {
	fmt.Println(allPathsSourceTarget([][]int{{1, 2}, {3}, {3}, {}}))
	fmt.Println(allPathsSourceTarget([][]int{{4, 3, 1}, {3, 2, 4}, {3}, {4}, {}}))
}
