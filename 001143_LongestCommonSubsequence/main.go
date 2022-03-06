package main

import "fmt"

func longestCommonSubsequence(text1 string, text2 string) int {
	t_1 := make([]int, len(text2))
	for i := 0; i < len(text2); i++ {
		t_1[i] = 0
	}

	t_2 := make([]int, len(text2))
	for i_1 := 0; i_1 < len(text1); i_1++ {
		if text1[i_1] == text2[0] {
			t_2[0] = 1
		} else {
			t_2[0] = t_1[0]
		}

		for i_2 := 1; i_2 < len(text2); i_2++ {
			if text1[i_1] == text2[i_2] {
				t_2[i_2] = t_1[i_2-1] + 1
			} else if t_1[i_2] > t_2[i_2-1] {
				t_2[i_2] = t_1[i_2]
			} else {
				t_2[i_2] = t_2[i_2-1]
			}
		}
		
		for i, v := range t_2 {
			t_1[i] = v
		}
	}

	return t_1[len(text2)-1]
}

func main() {
	fmt.Println(longestCommonSubsequence("abcba", "abcbcba"))
	fmt.Println(longestCommonSubsequence("abcde", "ace"))
	fmt.Println(longestCommonSubsequence("abc", "abc"))
	fmt.Println(longestCommonSubsequence("abc", "def"))
}
