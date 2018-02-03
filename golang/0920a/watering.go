package main

import (
	"bufio"
	"os"
	"strconv"
)

func main() {
	defer writer.Flush()
	scanner.Split(bufio.ScanWords)
	testsCount := ReadInt32()
	for testNumber := 1; testNumber <= testsCount; testNumber++ {
		bedsCount := ReadInt32()
		tapsCount := ReadInt32()
		answer := ReadInt32()
		preveousTapPosition := answer
		for tapNumber := 2; tapNumber <= tapsCount; tapNumber++ {
			tapPosition := ReadInt32()
			answer = max(answer, 1+(tapPosition-preveousTapPosition)/2)
			preveousTapPosition = tapPosition
		}
		writer.WriteString(strconv.Itoa(max(answer, 1+bedsCount-preveousTapPosition))+"\n")
	}
}

func max(x int, y int) int {
	if x > y {
		return x
	}
	return y
}

var scanner *bufio.Scanner = bufio.NewScanner(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

func ReadInt32() int {
	scanner.Scan()
	ans, _ := strconv.Atoi(scanner.Text())
	return ans
}
