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

func sortedArrayToBST(nums []int) *TreeNode {
    if len(nums) == 1 {
		node := new(TreeNode)
		node.Val = nums[0]
		node.Left = nil
		node.Right = nil
		return node
	}

	mid := len(nums) / 2
	root := new(TreeNode)
	root.Val = nums[mid]

	left := nums[0:mid]
	if len(left) > 0 {
		root.Left = sortedArrayToBST(left)
	}
	
	right := nums[mid+1:]
	if len(right) > 0 {
		root.Right = sortedArrayToBST(right)
	}

	return root
}

func main() {
	fmt.Println(sortedArrayToBST([]int {-10,-3,0,5,9}).toArray())
	fmt.Println(sortedArrayToBST([]int {1,3}).toArray())
}