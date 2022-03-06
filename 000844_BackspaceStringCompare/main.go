package main

import (
	"fmt"
)

type Stack struct {
	data []rune
}

func New() *Stack {
	p := new(Stack)
	p.data = make([]rune, 0)
	return p
}

func (s *Stack) size() int {
	return len(s.data)
}

func (s *Stack) empty() bool {
	return s.size() == 0
}

func (s *Stack) push(c rune) {
	s.data = append(s.data, c)
}

func (s *Stack) top() rune {
	return s.data[s.size()-1]
}

func (s *Stack) pop() rune {
	top := s.top()
	s.data = s.data[:s.size()-1]
	return top
}

func backspaceCompare(s string, t string) bool {
	s_stack := New()

	for _, c := range s {
		if c == '#' {
			if !s_stack.empty() {
				s_stack.pop()
			}
		} else {
            s_stack.push(c)
        }
	}

	t_stack := New()

	for _, c := range t {
		if c == '#' {
			if !t_stack.empty() {
				t_stack.pop()
			}
		} else {
            t_stack.push(c)
        }
	}

    for true {
        if s_stack.empty() && t_stack.empty() {
            break
        } else if s_stack.empty() {
            return false
        } else if t_stack.empty() {
            return false
        } else {
            t_c := t_stack.pop()
            s_c := s_stack.pop()
            if t_c != s_c {
                return false
            }
        }
    }

    return true
}

func main() {
	fmt.Println(backspaceCompare("ab#c", "ad#c"))
	fmt.Println(backspaceCompare("ab##", "c#d#"))
	fmt.Println(backspaceCompare("a#c", "b"))
}
