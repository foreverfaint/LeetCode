package main

import "fmt"

func partitionLabels(s string) []int {
	loc := make(map[byte]int, 0)
	for i := 0; i < len(s); i++ {
		loc[s[i]] = i
	}

	r := make([]int, 0)

	start := 0
	end := loc[s[start]]
	for i := 0; i < len(s); i++ {
		if loc[s[i]] > end {
			end = loc[s[i]]
		}

		if end == i {
			r = append(r, end-start+1)
			start = i + 1
		}
	}

	return r
}

func main() {
	fmt.Println(partitionLabels("ababcbacadefegdehijhklij"))
	fmt.Println(partitionLabels("eccbbbbdec"))
}
