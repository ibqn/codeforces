package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n int
	in := bufio.NewReader(os.Stdin)

	fmt.Fscan(in, &n)

	arr := make([][]int, n)

	for i := range arr {
		arr[i] = make([]int, i+1)
	}

	for i := 0; i < n; i++ {
		arr[i][0] = 1
	}

	for i := 1; i < n; i++ {
		for j := 1; j < i; j++ {
			arr[i][j] = arr[i-1][j] + arr[i][j-1]
		}
		arr[i][i] = 2 * arr[i][i-1]
	}

	fmt.Println(arr[n-1][n-1])
}
