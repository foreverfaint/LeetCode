package main

import (
	"bytes"
	"fmt"
	"strings"
)

func max(a int, b int) int {
	if a < b {
		return b
	}
	return a
}

func addStrings(num1 string, num2 string) string {
	r := make([]byte, max(len(num1), len(num2))+1)
	for i, j, k := len(num1)-1, len(num2)-1, 0; i >= 0 || j >= 0; i, j, k = i-1, j-1, k+1 {
		if i >= 0 && j >= 0 {
			sum := num1[i] - '0' + num2[j] - '0'
			r[k] += sum
		} else if i >= 0 {
			r[k] += num1[i] - '0'
		} else if j >= 0 {
			r[k] += num2[j] - '0'
		}

		if r[k] > 9 {
			r[k] = r[k] - 10
			r[k+1] = 1
		}		
	}

	fmt.Println(r)
	s := bytes.NewBufferString("")
	for i := len(r) - 1; i >= 0; i-- {
		s.WriteByte(r[i] + '0')
	}

	ss := s.String()
	ss = strings.TrimLeft(ss, "0")

	if len(ss) == 0 {
		return "0"
	}
	return ss
}

func main() {
	fmt.Println(addStrings("9", "99"))
	fmt.Println(addStrings("1", "9"))
	fmt.Println(addStrings("11", "123"))
	fmt.Println(addStrings("456", "77"))
	fmt.Println(addStrings("0", "0"))
}
