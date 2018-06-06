package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
	"strings"
)

type byLength []string

func main() {
	defer writer.Flush()
	scanner.Split(bufio.ScanWords)
	stringsCount := ReadInt32()
	inputs := make([]string, stringsCount)
	for stringIndex := 0; stringIndex < stringsCount; stringIndex++ {
		inputs[stringIndex] = ReadString()
	}
	sort.Sort(byLength(inputs))
	answer := true
	for stringIndex := 1; stringIndex < stringsCount; stringIndex++ {
		if !strings.Contains(inputs[stringIndex], inputs[stringIndex-1]) {
			answer = false
			break
		}
	}
	if !answer {
		writer.WriteString("NO\n")
	} else {
		writer.WriteString("YES\n")
		for stringIndex := 0; stringIndex < stringsCount; stringIndex++ {
			writer.WriteString(inputs[stringIndex] + "\n")
		}
	}
}

var scanner *bufio.Scanner = bufio.NewScanner(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

func (s byLength) Len() int {
	return len(s)
}

func (s byLength) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func (s byLength) Less(i, j int) bool {
	return len(s[i]) < len(s[j])
}

func ReadString() string {
	scanner.Scan()
	return scanner.Text()
}

func ReadInt32() int {
	ans, _ := strconv.Atoi(ReadString())
	return ans
}
