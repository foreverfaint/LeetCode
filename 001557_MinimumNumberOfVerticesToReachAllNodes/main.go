package main

import "fmt"

func findSmallestSetOfVertices(n int, edges [][]int) []int {
	connected := make([]int, n)
	for i := 0; i < n; i++ {
		connected[i] = i
	}

	for _, e := range edges {
		sn := e[0]
		en := e[1]
		new_sn := connected[sn]
		old_sn := connected[en]
		if old_sn == en {
			for i := 0; i < n; i++ {
				if connected[i] == old_sn {
					connected[i] = new_sn
				}
			}
		}
	}

	seen := make(map[int]bool)
	for i := 0; i < n; i++ {
		seen[connected[i]] = true
	}

	keys := make([]int, 0)
	for key, _ := range seen {
		keys = append(keys, key)
	}

	return keys
}

func main() {
	fmt.Println(findSmallestSetOfVertices(5, [][]int{{1,3},{2,0},{2,3},{1,0},{4,1},{0,3}}))
	fmt.Println(findSmallestSetOfVertices(6, [][]int{{0, 1}, {0, 2}, {2, 5}, {3, 4}, {4, 2}}))
	fmt.Println(findSmallestSetOfVertices(5, [][]int{{0, 1}, {2, 1}, {3, 1}, {1, 4}, {2, 4}}))
}
