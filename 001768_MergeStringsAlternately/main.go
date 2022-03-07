package main

import (
	"bytes"
	"fmt"
)

func mergeAlternately(word1 string, word2 string) string {
	buff := bytes.NewBufferString("")
    for i, j := 0, 0; i < len(word1) || j < len(word2); {
		if i < len(word1) {
			buff.WriteByte(word1[i])
			i++
		}		

		if j < len(word2) {
			buff.WriteByte(word2[j])
			j++
		}
	}
	return buff.String()
}

func main() {
    fmt.Println(mergeAlternately("abc", "pqr"))
	fmt.Println(mergeAlternately("ab", "pqrs"))
	fmt.Println(mergeAlternately("abcd", "pq"))
}