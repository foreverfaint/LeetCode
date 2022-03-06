package main

import (
	"fmt"
	"sort"
)

func eraseOverlapIntervals(intervals [][]int) int {
	sort.SliceStable(intervals, func (i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	erase := 0
	prevEnd := intervals[0][1]
	for i := 1; i < len(intervals); i++ {
		if intervals[i][0] < prevEnd {
			if intervals[i][1] < prevEnd {
				prevEnd = intervals[i][1]
			}
			erase++
		} else {
			prevEnd = intervals[i][1]
		}
	}
	return erase
}

func main() {
	fmt.Println(eraseOverlapIntervals([][]int{{1, 2}, {2, 3}, {3, 4}, {1, 3}}))
	fmt.Println(eraseOverlapIntervals([][]int{{1, 2}, {1, 2}, {1, 2}}))
	fmt.Println(eraseOverlapIntervals([][]int{{1, 2}, {2, 3}}))
}
