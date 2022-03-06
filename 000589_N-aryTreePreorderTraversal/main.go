package main

import "fmt"

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

func preorder(root *Node) []int {
	if root == nil {
		return []int{}
	}

	r := []int{root.Val}

	if root.Children != nil {
		for _, child := range root.Children {
			r = append(r, preorder(child)...)
		}
	}

	return r
}

func main() {
	fmt.Println(preorder(fromArray([]interface{}{1, nil, 3, 2, 4, nil, 5, 6})))
	fmt.Println(preorder(fromArray([]interface{}{1, nil, 2, 3, 4, 5, nil, nil, 6, 7, nil, 8, nil, 9, 10, nil, nil, 11, nil, 12, nil, 13, nil, nil, 14})))
}
