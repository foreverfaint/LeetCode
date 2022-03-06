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

func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil {
		return head
	}

	removed := false

	for head.Next != nil {
		if head.Val == head.Next.Val {
			head = head.Next
			removed = true
		} else if removed {
			return deleteDuplicates(head.Next)
		} else {
			head.Next = deleteDuplicates(head.Next)
			return head
		}
	}

	if removed {
		return head.Next
	}
    return head
}

func main() {
	fmt.Println(deleteDuplicates(fromArray([]int {})).toArray())
	fmt.Println(deleteDuplicates(fromArray([]int {1, 2, 3, 3, 4, 4, 5})).toArray())
	fmt.Println(deleteDuplicates(fromArray([]int {1,1,1,2,3})).toArray())
}