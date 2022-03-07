package main

import (
	"bytes"
	"fmt"
)

func interpret(command string) string {
    buff := bytes.NewBufferString("")

	for i, l := 0, len(command); ; {
		if i + 3 < l && command[i:i+4] == "(al)" {
			buff.WriteString("al")
			i += 4
		} else if i + 1 < l && command[i:i+2] == "()" {
			buff.WriteString("o")
			i += 2
		} else if i < l && command[i] == 'G' {
			buff.WriteByte('G')
			i += 1
		} else {
			break
		}
	}

	return buff.String()
}

func main() {
    fmt.Println(interpret("G()(al)"))
	fmt.Println(interpret("G()()()()(al)"))
	fmt.Println(interpret("(al)G(al)()()G"))
}