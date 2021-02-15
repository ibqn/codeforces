package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var t int

	in := bufio.NewReader(os.Stdin)

	fmt.Fscan(in, &t)

	var values = [...]int{1, 3, 6, 10}
	for i := 0; i < t; i++ {
		var number string

		fmt.Fscan(in, &number)
		digit, err := strconv.Atoi(number[0:1])

		if err != nil {
			panic(err)
		}

		fmt.Println(10*(digit-1) + values[len(number)-1])

	}

}
