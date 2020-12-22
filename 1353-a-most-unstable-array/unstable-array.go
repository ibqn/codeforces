package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var t, n, m int

	in := bufio.NewReader(os.Stdin)
	fmt.Fscan(in, &t)

	for i := 0; i < t; i++ {
		fmt.Fscan(in, &n, &m)

		switch n {
		case 1:
			fmt.Println(0)
		case 2:
			fmt.Println(m)
		default:
			fmt.Println(2 * m)
		}
	}

}
