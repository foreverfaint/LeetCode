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

func isSameTree(p *TreeNode, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	} else if p == nil || q == nil {
		return false
	} else if p.Val != q.Val {
		return false
	}
	return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
}

func main() {
	fmt.Println(fromArray([]interface{}{1, nil, 2}).toArray())
	fmt.Println(isSameTree(fromArray([]interface{}{1, 2, 3}), fromArray([]interface{}{1, 2, 3})))
	fmt.Println(isSameTree(fromArray([]interface{}{1, 2}), fromArray([]interface{}{1, nil, 2})))
	fmt.Println(isSameTree(fromArray([]interface{}{1, 2, 1}), fromArray([]interface{}{1, 1, 2})))
}
