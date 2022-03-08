package main

import "fmt"

func numOfMinutes(n int, headID int, manager []int, informTime []int) int {
	direct_managers := make(map[int][]int, n)
	for i := 0; i < n; i++ {
		arr, has := direct_managers[manager[i]]
		if !has {
			arr = make([]int, 0)
		}
		direct_managers[manager[i]] = append(arr, i)
	}

	cost := -1

	q := make([][]int, 0)
	q = append(q, []int{headID, informTime[headID]})

	for len(q) > 0 {
		t := q[0]

		cost_ := t[1]
		if cost_ > cost {
			cost = cost_
		}

		direct_manager := t[0]
		for _, sub := range direct_managers[direct_manager] {
			q = append(q, []int{sub, cost_ + informTime[sub]})
		}

		q = q[1:]
	}

	return cost
}

func main() {
	fmt.Println(numOfMinutes(1, 0, []int{-1}, []int{0}))
	fmt.Println(numOfMinutes(6, 2, []int{2, 2, -1, 2, 2, 2}, []int{0, 0, 1, 0, 0, 0}))
	fmt.Println(numOfMinutes(8, 0, []int{-1, 5, 0, 6, 7, 0, 0, 0}, []int{89, 0, 0, 0, 0, 523, 241, 519}))
}
