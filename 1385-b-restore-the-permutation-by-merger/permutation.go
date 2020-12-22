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
	)

	in := bufio.NewReader(os.Stdin)

	fmt.Fscan(in, &t)

	for i := 0; i < t; i++ {
		fmt.Fscan(in, &n)

		p = make([]int, n, n)

		for j := 0; j < 2*n; j++ {
			fmt.Fscan(in, &val)

			var flag = true
			for _, b := range p {
				if b == val {
					flag = false
				}
			}

			if flag {
				p = append(p, val)
				fmt.Print(val, " ")
			}
		}
		fmt.Println()
	}
}
