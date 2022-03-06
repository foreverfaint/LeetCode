package main

import "fmt"

func lengthOfLastWord(s string) int {
	i := len(s) - 1
	for ; s[i] == ' '; i-- { }
	l := 0
	for ; i >= 0 && s[i] != ' '; l, i = l + 1, i - 1 {}
	return l
}

func main() {
	fmt.Println(lengthOfLastWord("a"))
    fmt.Println(lengthOfLastWord("Hello World"))
	fmt.Println(lengthOfLastWord("   fly me   to   the moon  "))
	fmt.Println(lengthOfLastWord("luffy is still joyboy"))
}