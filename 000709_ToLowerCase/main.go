package main

import (
	"bytes"
	"fmt"
)

func toLowerCase(s string) string {
	r := bytes.NewBufferString("")
    for i:=0; i < len(s); i++ {
		if 'A' <= s[i] && s[i] <= 'Z' {
			r.WriteByte(s[i] - 'A' + 'a')
		} else {
			r.WriteByte(s[i])
		}
	}
	return r.String()
}

func main() {
    fmt.Println(toLowerCase("Hello"))
	fmt.Println(toLowerCase("here"))
	fmt.Println(toLowerCase("LOVELY"))
}