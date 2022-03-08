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

func isSame(tn1 *TreeNode, tn2 *TreeNode) bool {
	fmt.Println(tn1, tn2)
	if tn1 == nil && tn2 == nil {
		return true
	} else if tn1 == nil || tn2 == nil {
		return false
	} else {
		return tn1.Val == tn2.Val && isSame(tn1.Left, tn2.Left) && isSame(tn1.Right, tn2.Right)
	}
}

func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
	if root == nil && subRoot == nil {
		return true
	} else if root == nil || subRoot == nil {
		return false
	} else if root.Val == subRoot.Val {
		if isSame(root.Left, subRoot.Left) && isSame(root.Right, subRoot.Right) {
			return true
		}
	}

	if root.Left != nil && isSubtree(root.Left, subRoot) {
		return true
	}

	if root.Right != nil && isSubtree(root.Right, subRoot) {
		return true
	}

	return false
}

func main() {
	fmt.Println(isSubtree(fromArray([]interface{}{-1,-4,8,-6,-2,3,9,nil,-5,nil,nil,0,7}), fromArray([]interface{}{3,0,5848})))
	fmt.Println(isSubtree(fromArray([]interface{}{3, 4, 5, 1, nil, 2}), fromArray([]interface{}{3, 1, 2})))
	// fmt.Println(isSubtree(fromArray([]interface{}{3, 4, 5, 1, 2}), fromArray([]interface{}{4, 1, 2})))
	// fmt.Println(isSubtree(fromArray([]interface{}{3, 4, 5, 1, 2, nil, nil, nil, nil, 0}), fromArray([]interface{}{4, 1, 2})))
}
