package main

import (
	"bytes"
	"fmt"
	"strings"
)

func reverse(s string) string {
	rns := []rune(s) // convert to rune
	for i, j := 0, len(rns)-1; i < j; i, j = i+1, j-1 {

		// swap the letters of the string,
		// like first with last and so on.
		rns[i], rns[j] = rns[j], rns[i]
	}

	// return the reversed string.
	return string(rns)
}

func byte_add_byte(n1 byte, n2 byte) (bool, byte) {
	sum := n1 - '0' + n2 - '0'
	if sum > 9 {
		return true, (sum - 10) + '0'
	} else {
		return false, sum + '0'
	}
}

func string_add_string(num1 string, num2 string) string {
	l_1 := len(num1)
	l_2 := len(num2)

	r := bytes.NewBufferString("")
	carry := false
	for i, j := l_1-1, l_2-1; i >= 0 || j >= 0; i, j = i-1, j-1 {
		if i >= 0 && j >= 0 {
			if carry {
				carry_, sum := byte_add_byte(num1[i], num2[j]+1)
				r.WriteByte(sum)
				carry = carry_
			} else {
				carry_, sum := byte_add_byte(num1[i], num2[j])
				r.WriteByte(sum)
				carry = carry_
			}
		} else if i >= 0 {
			if carry {
				carry_, sum := byte_add_byte(num1[i], '1')
				r.WriteByte(sum)
				carry = carry_
			} else {
				r.WriteByte(num1[i])
			}
		} else if j >= 0 {
			if carry {
				carry_, sum := byte_add_byte(num2[j], '1')
				r.WriteByte(sum)
				carry = carry_
			} else {
				r.WriteByte(num2[j])
			}
		}
	}

	if carry {
		r.WriteByte('1')
	}

	return reverse(r.String())
}

func byte_multiply_byte(n1 byte, n2 byte) (byte, byte) {
	mul := (n1 - '0') * (n2 - '0')
	if mul > 9 {
		return (mul / 10) + '0', (mul % 10) + '0'
	} else {
		return '0', mul + '0'
	}
}

func string_multiply_byte(num1 string, n2 byte) string {
	r := bytes.NewBufferString("")
	carry := byte('0')
	for i := len(num1) - 1; i >= 0; i-- {
		n1 := num1[i]
		carry1_, mul := byte_multiply_byte(n1, n2)
		carry2_, sum := byte_add_byte(mul, carry)
		r.WriteByte(sum)
		if carry2_ {
			_, carry = byte_add_byte(carry1_, '1')
		} else {
			carry = carry1_
		}
	}
	if carry != '0' {
		r.WriteByte(carry)
	}
	return reverse(r.String())
}

func multiply(num1 string, num2 string) string {
	add_ := make([]string, 0)

	for i := len(num2) - 1; i >= 0; i-- {
		n2 := num2[i]
		add_ = append(add_, string_multiply_byte(num1, n2))
	}

	sum_ := add_[0]
	move := "0"
	for i := 1; i < len(add_); i++ {
		t := add_[i] + move
		sum_ = string_add_string(sum_, t)
		move += "0"
	}

	sum_ = strings.TrimLeft(sum_, "0")
	if len(sum_) == 0 {
		return "0"
	}
	return sum_
}

func main() {
	b1 := string_multiply_byte("999", '9')
	fmt.Println(b1)
	b1 = string_multiply_byte("987", '8')
	fmt.Println(b1)

	fmt.Println(multiply("2", "3"))
	fmt.Println(multiply("123", "456"))
	fmt.Println(multiply("9133", "0"))
	fmt.Println(multiply("123456789", "987654321"))
}
