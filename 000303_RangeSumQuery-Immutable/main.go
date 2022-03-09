package main

import "fmt"

type NumArray struct {
    data []int
}


func Constructor(nums []int) NumArray {
    return NumArray{nums}
}


func (this *NumArray) SumRange(left int, right int) int {
    sum := 0
	for i := left; i <= right; i++ {
		sum += this.data[i]
	}
	return sum
}


func main() {
	arr := Constructor([]int {-2, 0, 3, -5, 2, -1})

    fmt.Println(arr.SumRange(0, 2))
	fmt.Println(arr.SumRange(2, 5))
	fmt.Println(arr.SumRange(0, 5))
}