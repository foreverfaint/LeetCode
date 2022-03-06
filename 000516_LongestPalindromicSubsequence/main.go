package main

import "fmt"

func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func lcs(a string, b string) int {
	lcs_1 := make([]int, len(b))
	lcs_2 := make([]int, len(b))

	for x := 0; x < len(b); x++ {
		if a[0] == b[x] {
			lcs_1[x] = 1
		} else if x == 0 {
            lcs_1[x] = 0
        } else {
			lcs_1[x] = lcs_1[x-1]
		}
	}

	for y := 1; y < len(a); y++ {
		if a[y] == b[0] {
			lcs_2[0] = 1
		} else {
			lcs_2[0] = lcs_1[0]
		}

		for x := 1; x < len(b); x++ {
			if a[y] == b[x] {
				lcs_2[x] = lcs_1[x-1] + 1
			} else {
				if lcs_2[x-1] > lcs_1[x] {
					lcs_2[x] = lcs_2[x-1]
				} else {
					lcs_2[x] = lcs_1[x]
				}
			}
		}

		for i, v := range lcs_2 {
			lcs_1[i] = v
		}
	}

	return lcs_1[len(b)-1]
}

func longestPalindromeSubseq(s string) int {
	return lcs(s, Reverse(s))
}

func main() {
	fmt.Println(longestPalindromeSubseq("abaababaab"))
	fmt.Println(longestPalindromeSubseq("bbbab"))
	fmt.Println(longestPalindromeSubseq("cbbd"))
}
