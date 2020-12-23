package main

import (
	"bufio"
	"fmt"
	"os"
)

func max(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}

func min(a, b int64) int64 {
	if a > b {
		return b
	}
	return a
}

func main() {
	var n, a, b int64

	in := bufio.NewReader(os.Stdin)

	fmt.Fscan(in, &n, &a, &b)

	if 6*n > a*b {
		sixn := 6 * n

		var minv, maxv int64

		minv = min(a, b)
		maxv = max(a, b)

		r1 := max(a, (sixn+b-1)/b)
		r2 := max(b, (sixn+a-1)/a)
		sixtop := min(r1*b, r2*a)

	out:
		for j := sixn; j <= sixtop; j++ {
			for i := minv; j/i >= maxv && i*i <= j; i++ {
				if j%i == 0 {
					if b > a {
						a = min(i, j/i)
						b = max(i, j/i)
					} else {
						b = min(i, j/i)
						a = max(i, j/i)
					}
					break out
				}
			}
		}
	}

	fmt.Printf("%d\n%d %d\n", a*b, a, b)
}
