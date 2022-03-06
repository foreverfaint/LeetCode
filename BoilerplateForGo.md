# Boilerplate for Go

## Basic

```go
package main

import "fmt"

func fun() int {

}

func main() {
    fmt.Println(fun())
}
```

## Matrix 

```go
package main

import "fmt"

func printMatrix(matrix [][]int) {
	for _, row := range matrix {
		fmt.Println((row))
	}
	fmt.Println("----")
}

type Coord struct {
	y int
	x int
}

type Queue struct {
	data []Coord
}

func New() *Queue {
	q := new(Queue)
	q.data = make([]Coord, 0)
	return q
}

func (q *Queue) empty() bool {
	return len(q.data) == 0
}

func (q *Queue) appendAtTail(coord Coord) {
	q.data = append(q.data, coord)
}

func (q *Queue) removeFromHead() Coord {
	first := q.data[0]
	q.data = q.data[1:]
	return first
}

func fun() int {

}

func main() {
    fmt.Println(fun())
}
```

## ListNode


```go
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

func fun(head *ListNode) *ListNode {
    return head
}

func main() {
	fmt.Println(fun(fromArray([]int {1, 2, 3, 3, 4, 4, 5})).toArray())
}
```

## BST

```go
package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func New(val int) *TreeNode {
	return &TreeNode{val, nil, nil}
}

func fromArray(arr []interface{}) *TreeNode {
	if len(arr) == 0 {
		return nil
	}

	root := New(arr[0].(int))

	q := make([]*TreeNode, 0)
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

func (root *TreeNode) toArray() []interface{} {
	r := make([]interface{}, 0)

	q := make([]*TreeNode, 0)
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

func main() {
	fmt.Println(fun(fromArray([]int {1, 2, 3, 3, 4, 4, 5})).toArray())
}
```

## N-ary Tree

```go
type Node struct {
	Val      int
	Children []*Node
}

func (head *Node) toArray() []interface{} {
	if head == nil {
		return []interface{}{}
	}

	r := make([]interface{}, 0)
	r = append(r, head.Val)

	q := make([]*Node, 0)
	q = append(q, head)

	for len(q) > 0 {
		top := q[0]

		r = append(r, nil)

		if top.Children != nil {
			for _, child := range top.Children {
				q = append(q, child)
				r = append(r, child.Val)
			}
		}

		q = q[1:]
	}

	return r
}

func fromArray(arr []interface{}) *Node {
	if len(arr) == 0 {
		return nil
	}

	r := Node{arr[0].(int), nil}

	q := make([]*Node, 0)
	q = append(q, &r)

	i := 2
	l := len(arr)
	for len(q) > 0 {

		root := q[0]

		children := make([]*Node, 0)
		for ; i < l && arr[i] != nil; i++ {
			child := Node{arr[i].(int), nil}
			q = append(q, &child)
			children = append(children, &child)
		}
		i++

		if len(children) > 0 {
			root.Children = children
		}

		q = q[1:]
	}

	return &r
}

func fun(root *Node) []int {
	return []int {}
}

func main() {
	fmt.Println(fun(fromArray([]interface{}{1, nil, 3, 2, 4, nil, 5, 6})))
}

```