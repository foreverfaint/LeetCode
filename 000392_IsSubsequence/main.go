package main

import "fmt"

func isSubsequence(s string, t string) bool {
	l_s := len(s)
	l_t := len(t)

	if l_s == 0 {
		return true
	}

	for i_s, i_t := 0, 0; i_t < l_t; i_t++ {
		if s[i_s] == t[i_t] {
			i_s++
			if i_s == l_s {
				return true
			}
		}
	}
	return false
}

func main() {
	fmt.Println(isSubsequence("abc", "ahbgdc"))
	fmt.Println(isSubsequence("axc", "ahbgdc"))
}
