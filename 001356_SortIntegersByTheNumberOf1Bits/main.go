package main

import (
	"fmt"
	"sort"
)

type Pair struct {
	NumOf1Bit int
	Value     int
}

func transform(pl []Pair, value int) []Pair {
	numOf1Bit := 0
	t_ := value
	for t_ > 0 {
		if t_%2 == 1 {
			numOf1Bit++
		}
		t_ = t_ >> 1
	}
	return append(pl, Pair{numOf1Bit, value})
}

func sortByBits(arr []int) []int {
	arr_ := make([]Pair, 0)
	for _, value := range arr {
		arr_ = transform(arr_, value)
	}

	sort.SliceStable(arr_, func (i, j int) bool {
		if arr_[i].NumOf1Bit == arr_[j].NumOf1Bit {
			return arr_[i].Value < arr_[j].Value
		} else {
			return arr_[i].NumOf1Bit < arr_[j].NumOf1Bit
		}
	})

	for i, value := range arr_ {
		arr[i] = value.Value
	}

	return arr
}

func main() {
	fmt.Println(sortByBits([]int{0, 1, 2, 3, 4, 5, 6, 7, 8}))
	fmt.Println(sortByBits([]int{1024,512,256,128,64,32,16,8,4,2,1}))
}
