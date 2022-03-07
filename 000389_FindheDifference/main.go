package main

import "fmt"

func findTheDifference(s string, t string) byte {
    m := make(map[byte]int, 0)

	for i := 0; i < len(s); i++ {
		m[s[i]] += 1
	}

	for i := 0; i < len(t); i++ {
		m[t[i]] -= 1
	}

	for c, n := range m {
		if n < 0 {
			return c
		}
	}

	return 0
}

func main() {
    fmt.Println(findTheDifference("abcd", "abcde"))
	fmt.Println(findTheDifference("", "y"))
}