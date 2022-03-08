package main

import (
	"fmt"
	"sort"
)

func h(str string) string {
	b := []byte(str)
	sort.Slice(b, func(i, j int) bool { return b[i] < b[j] })
	return string(b)
}

func groupAnagrams(strs []string) [][]string {
	m := make(map[string][]string, 0)
	for _, str := range strs {
		h_ := h(str)

		arr, has := m[h_]
		if !has {
			arr = make([]string, 0)
		}
		m[h_] = append(arr, str)
	}

	r := make([][]string, 0)
	for _, arr := range m {
		r = append(r, arr)
	}

	return r
}

func main() {
	fmt.Println(groupAnagrams([]string{"eat", "tea", "tan", "ate", "nat", "bat"}))
	fmt.Println(groupAnagrams([]string{""}))
	fmt.Println(groupAnagrams([]string{"a"}))
}
