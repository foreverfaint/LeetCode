package main

import "fmt"

func compare(a map[rune]int, b map[rune]int) bool {
	for k, v := range b {
		if v != a[k] {
			return false
		}
	}

	return true
}

func findAnagrams(s string, p string) []int {
	r := make([]int, 0)

	s_rune_list := []rune(s)
	p_rune_list := []rune(p)

	l_s := len(s_rune_list)
	l_p := len(p_rune_list)

	hist_p := make(map[rune]int, 0)
	for _, c := range p_rune_list {
		hist_p[c] += 1
	}

	hist_s := make(map[rune]int, 0)
	for i := 0; i < l_s; i++ {
		hist_s[s_rune_list[i]] += 1

		if i >= l_p-1 {
			if compare(hist_s, hist_p) {
				r = append(r, i-l_p+1)
			}
			hist_s[s_rune_list[i-l_p+1]] -= 1
		}
	}

	return r
}

func main() {
	fmt.Println(findAnagrams("cbaebabacd", "abc"))
	fmt.Println(findAnagrams("abab", "ab"))
}
