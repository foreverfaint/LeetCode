package main

import "fmt"

type Node struct {
	Val   int
	Left  *Node
	Right *Node
	Next  *Node
}

func New(val int) *Node {
	return &Node{val, nil, nil, nil}
}

func fromArray(arr []interface{}) *Node {
	if len(arr) == 0 {
		return nil
	}

	root := New(arr[0].(int))

	q := make([]*Node, 0)
	q = append(q, root)

	i := 0
	for len(q) > 0 {
		top := q[0]

		i += 1
		if i < len(arr) && arr[i] != nil {
			top.Left = New(arr[i].(int))
			q = append(q, top.Left)
		}

		i += 1
		if i < len(arr) && arr[i] != nil {
			top.Right = New(arr[i].(int))
			q = append(q, top.Right)
		}

		q = q[1:]
	}

	return root
}

func (root *Node) toArray() []interface{} {
	r := make([]interface{}, 0)

	q := make([]*Node, 0)
	q = append(q, root)

	for len(q) > 0 {
		top := q[0]

		if top != nil {
			r = append(r, top.Val)
			q = append(q, top.Left)
			q = append(q, top.Right)
		} else {
			r = append(r, nil)
		}

		q = q[1:]
	}

	return r
}

func (root *Node) print() {
	if root != nil {
		fmt.Println(root.Val, root.Next)
		if root.Left != nil {
			root.Left.print()
		}
		if root.Right != nil {
			root.Right.print()
		}
	}
}

func find(root *Node) *Node {
	for root.Next != nil {
		if root.Next.Left != nil {
			return root.Next.Left
		} else if root.Next.Right != nil {
			return root.Next.Right
		}
		root = root.Next
	}
	return nil
}

func connect(root *Node) *Node {
	if root != nil {
		if root.Right != nil {
			root.Right.Next = find(root)
			connect(root.Right)
		}
		if root.Left != nil {
			if root.Right != nil {
				root.Left.Next = root.Right
			} else {
				root.Left.Next = find(root)
			}
			connect(root.Left)
		}
	}
	return root
}

func main() {
	connect(fromArray([]interface{}{1, 2, 3, 4, 5, nil, 6, 7, nil, nil, nil, nil, 8})).print()
	// connect(fromArray([]interface{}{1, 2, 3, 4, nil, nil, 5})).print()
	// connect(fromArray([]interface{} {1,2,3,4,5,nil,7})).print()
	// connect(fromArray([]interface{} {})).print()
}
