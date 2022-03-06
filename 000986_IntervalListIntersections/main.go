package main

import "fmt"

func printMatrix(matrix [][]int) {
	for _, row := range matrix {
		fmt.Println((row))
	}
}

func intervalIntersection(firstList [][]int, secondList [][]int) [][]int {
	// printMatrix(firstList)
	// fmt.Println("****")
	// printMatrix(secondList)
	// fmt.Println("====")

	if len(firstList) == 0 || len(secondList) == 0 {
		return [][]int {}
	}

	first := firstList[0]
	second := secondList[0]
	if first[0] > second[0] {
		second, first = first, second
		secondList, firstList = firstList, secondList
	}

	if first[1] < second[0] {
		return intervalIntersection(firstList[1:], secondList)
	} else if first[1] > second[1] {
		return append([][]int {second}, intervalIntersection(firstList, secondList[1:])...)
	} else {
		return append([][]int {{second[0], first[1]}}, intervalIntersection(firstList[1:], secondList)...)
	}
}

func main() {
	printMatrix(intervalIntersection(
		[][]int{{0, 2}, {5, 10}, {13, 23}, {24, 25}},
		[][]int{{1, 5}, {8, 12}, {15, 24}, {25, 26}}))

	fmt.Println("----")

	printMatrix(intervalIntersection(
		[][]int{{1, 3}, {5, 9}},
		[][]int{}))
}
