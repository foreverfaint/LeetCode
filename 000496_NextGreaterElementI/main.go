package main

import "fmt"

func nextGreaterElement(nums1 []int, nums2 []int) []int {
    m := make(map[int]int)
    for i, v := range nums2 {
        m[v] = -1
        for j := i + 1; j < len(nums2); j++ {
            if nums2[j] > v {
                m[v] = nums2[j]
                break
            }
        }
    }

    r := make([]int, len(nums1))
    for i, v := range nums1 {
        r[i] = m[v]
    }

    return r
}

func main() {
    fmt.Println(nextGreaterElement([]int {4,1,2}, []int {1,3,4,2}))
    fmt.Println(nextGreaterElement([]int {2,4}, []int {1,2,3,4}))
}