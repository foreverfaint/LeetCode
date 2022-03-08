package main

import "fmt"

func longestPalindrome(s string) int {
	chars := make(map[byte]int, 0)

	for i := 0; i < len(s); i++ {
		chars[s[i]] += 1
	}

	l := 0
	has_odd := false
	for _, v := range chars {
		if v%2 == 0 {
			l += v
		} else {
			l += v - 1
			has_odd = true
		}
	}

	if has_odd {
		return l + 1
	}
	return l
}

func main() {
	fmt.Println(longestPalindrome("abccccdd"))
	fmt.Println(longestPalindrome("a"))
	fmt.Println(longestPalindrome("bb"))
}
