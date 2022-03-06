package main

import "fmt"
import "math"

func checkStraightLine(coordinates [][]int) bool {
	if len(coordinates) == 0 {
		return true
	}

	x_0 := coordinates[0][0]
	y_0 := coordinates[0][1]
	k_i := 0.0
	is_vertical := false
	for i := 1; i < len(coordinates); i++ {
		x_i := coordinates[i][0]
		y_i := coordinates[i][1]

		if i == 1 {
			if x_0 == x_i {
				is_vertical = true
			} else {
				k_i = float64(y_i - y_0) / float64(x_i - x_0)
			}
		} else {
			if is_vertical && x_0 != x_i {
				return false
			}

			if !is_vertical && math.Abs(float64(y_i - y_0) / float64(x_i - x_0) - k_i) > 1e-5 {
				return false
			}
		}
	}

	return true
}

func main() {
	fmt.Println(checkStraightLine([][]int{{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}}))
	fmt.Println(checkStraightLine([][]int{{1, 1}, {2, 2}, {3, 4}, {4, 5}, {5, 6}, {6, 7}}))
}
