package main

import "fmt"

type ListNode struct {
	Val int
	Next *ListNode
} 

func fromArray(arr []int) *ListNode {
	if len(arr) == 0 {
		return nil
	}
	return &ListNode{ arr[0], fromArray(arr[1:]) }
}

func (head *ListNode) toArray() []int {
	var s []int

	if head == nil {
		return s
	}
	
	return append(append(s, head.Val), head.Next.toArray()...)
}

func getDecimalValue(head *ListNode) int {
    r := 0
	for head != nil {
		r <<= 1
		if head.Val == 1 {
			r += 1
		}
		head = head.Next
	}
	return r
}

func main() {
	fmt.Println(getDecimalValue(fromArray([]int {1,0,1})))
	fmt.Println(getDecimalValue(fromArray([]int {0})))
}
