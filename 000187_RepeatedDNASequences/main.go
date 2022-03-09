package main

import "fmt"

func findRepeatedDnaSequences(s string) []string {
	r := make(map[string]bool)
	m := make(map[string]bool)
	for i := 0; i + 10 <= len(s); i++ {
		substr := s[i:i + 10]
		_, has := m[substr]
		if !has {
			m[substr] = true
		} else {
			r[substr] = true
		}
	}

	k := make([]string, 0)
	for substr, _ := range r {
		k = append(k, substr)
	}
	return k
}

func main() {
	fmt.Println(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
	fmt.Println(findRepeatedDnaSequences("AAAAAAAAAAAAA"))
	fmt.Println(findRepeatedDnaSequences("AAAAAAAAAAA"))
}
