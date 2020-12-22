package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var (
		t, n, val int
		p         []int
		pmap      map[int]bool
	)

	in := bufio.NewReader(os.Stdin)

	fmt.Fscan(in, &t)

	for i := 0; i < t; i++ {
		fmt.Fscan(in, &n)

		p = make([]int, n, n)
		pmap = make(map[int]bool, n)

		for j := 0; j < 2*n; j++ {
			fmt.Fscan(in, &val)

			if !pmap[val] {
				pmap[val] = true
				p = append(p, val)
				fmt.Print(val, " ")
			}
		}
		fmt.Println()
	}
}
