package main

import (
	"bufio"
	"os"
	"strconv"
)

func main() {
	defer writer.Flush()
	scanner.Split(bufio.ScanWords)
	n := ReadUint64()
	m := ReadUint64()
	a := ReadUint8()
	b := ReadUint8()
	if n%m == 0 {
		WriteLineUint64(0)
		return
	}
	div := n / m
	floor := m * div
	destroyPrice := (n - floor) * uint64(b)
	buildPrice := (floor + m - n) * uint64(a)
	WriteLineUint64(Min(destroyPrice, buildPrice))
}

// Min returns min of two uint64
func Min(a uint64, b uint64) uint64 {
	if a < b {
		return a
	}
	return b
}

var scanner = bufio.NewScanner(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)

// WriteLineUint64 write to Stdout uint64 as dec
func WriteLineUint64(a uint64) {
	writer.WriteString(strconv.FormatUint(a, 10) + "\n")
}

// ReadString read string from Stdin
func ReadString() string {
	scanner.Scan()
	return scanner.Text()
}

// ReadUint64 read uint64 from Stdin
func ReadUint64() uint64 {
	ans, _ := strconv.ParseUint(ReadString(), 10, 64)
	return ans
}

// ReadUint8 read uint8 (byte) from Stdin
func ReadUint8() uint8 {
	ans, _ := strconv.ParseUint(ReadString(), 10, 8)
	return uint8(ans)
}
