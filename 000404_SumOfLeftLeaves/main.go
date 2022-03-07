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

func _sum(root *TreeNode, isLeft bool) int {
	if root.Left == nil && root.Right == nil {
		if isLeft {
			return root.Val
		}
		return 0
	} else if root.Left == nil {
		return _sum(root.Right, false)
	} else if root.Right == nil {
		return _sum(root.Left, true)
	} else {
		return _sum(root.Left, true) + _sum(root.Right, false)
	}
}

func sumOfLeftLeaves(root *TreeNode) int {
	if root == nil {
		return 0
	}

	return _sum(root, false)
}

func main() {
	fmt.Println(sumOfLeftLeaves(fromArray([]interface{}{3, 9, 20, nil, nil, 15, 7})))
	fmt.Println(sumOfLeftLeaves(fromArray([]interface{}{1})))
}
