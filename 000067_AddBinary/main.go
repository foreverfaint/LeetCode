package main

import "fmt"

func addBinary(a string, b string) string {
	if len(a) > len(b) {
		a, b = b, a
	}

	result := ""
	carry := false
	for a_i, b_i := len(a)-1, len(b)-1; b_i >= 0; a_i, b_i = a_i-1, b_i-1 {
		b_c := b[b_i]
		a_c := '0'
		if a_i >= 0 {
			a_c = rune(a[a_i])
		}
		if a_c == '0' && b_c == '0' {
			if carry {
				result = "1" + result
			} else {
				result = "0" + result
			}
			carry = false
		} else if a_c == '0' || b_c == '0' {
			if carry {
				result = "0" + result
				carry = true
			} else {
				result = "1" + result
				carry = false
			}
		} else {
			if carry {
				result = "1" + result
			} else {
				result = "0" + result
			}
			carry = true
		}
	}

	if (carry) {
		return "1" + result
	}

	return result
}

func main() {
	fmt.Println(addBinary("11", "1"))
	fmt.Println(addBinary("1010", "1011"))
}
