package main

import (
	"fmt"
	"strings"
)

func wordPattern(pattern string, s string) bool {
	splits_s := strings.Split(s, " ")
	if len(splits_s) != len(pattern) {
		return false
	}

	m_b2s := make(map[byte]string, 0)
	m_s2b := make(map[string]byte, 0)
	for i := 0; i < len(pattern); i++ {
		w, has := m_b2s[pattern[i]]
		if !has {
			_, has := m_s2b[splits_s[i]]
			if has {
				return false
			}
			m_s2b[splits_s[i]] = pattern[i]
			m_b2s[pattern[i]] = splits_s[i]
		} else if w != splits_s[i] {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(wordPattern("abba", "dog cat cat dog"))
	fmt.Println(wordPattern("abba", "dog cat cat fish"))
	fmt.Println(wordPattern("aaaa", "dog cat cat dog"))
}
