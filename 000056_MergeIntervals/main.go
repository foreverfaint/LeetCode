package main

import (
	"fmt"
	"sort"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func merge(intervals [][]int) [][]int {
	sort.Slice(intervals, func(i, j int) bool {
		p1 := intervals[i]
		p2 := intervals[j]
		if p1[0] == p2[0] {
			return p1[1] < p2[1]
		} else {
			return p1[0] < p2[0]
		}
	})

	r := [][]int{}

	m := intervals[0]
	for i := 1; i < len(intervals); i++ {
		if m[1] < intervals[i][0] {
			r = append(r, m)
			m = intervals[i]
		} else {
			m = []int{m[0], max(intervals[i][1], m[1])}
		}
	}

	return append(r, m)
}

func main() {
	fmt.Println(merge([][]int{{1, 3}, {2, 6}, {8, 10}, {15, 18}}))
	fmt.Println(merge([][]int{{1, 4}, {4, 5}}))
}
