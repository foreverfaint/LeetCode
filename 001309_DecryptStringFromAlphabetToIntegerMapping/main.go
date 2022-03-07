package main

import (
	"bytes"
	"fmt"
	"strconv"
)

func freqAlphabets(s string) string {
    r := bytes.NewBufferString("")

	for i, l := 0, len(s); ; {
		if i + 2 < l && s[i+2] == '#' {
			x, _ := strconv.Atoi(s[i:i+2])
			r.WriteByte('j' + byte(x - 10))
			i += 3
		} else if i < l {
			r.WriteByte(s[i] - '1' + 'a')
			i += 1
		} else {
			break
		}
	}

	return r.String()
}

func main() {
    fmt.Println(freqAlphabets("10#11#12"))
	fmt.Println(freqAlphabets("1326#"))
}