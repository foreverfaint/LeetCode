package main

import "fmt"

func minReorder(n int, connections [][]int) int {

}

func main() {
	fmt.Println(minReorder(6, [][]int{{0, 1}, {1, 3}, {2, 3}, {4, 0}, {4, 5}}))
	fmt.Println(minReorder(5, [][]int{{1, 0}, {1, 2}, {3, 2}, {3, 4}}))
	fmt.Println(minReorder(3, [][]int{{1, 0}, {2, 0}}))
}
