package main
import "bufio"
import "os"
import "strings"
import "strconv"

var scanner *bufio.Scanner = bufio.NewScanner(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

func ReadInt32() int {
    scanner.Scan()
    ans, _ := strconv.Atoi(scanner.Text())
    return ans
}

func PrintInts(ints ...int) {
    for _, value := range ints {
        writer.WriteString(strconv.Itoa(value))
        writer.WriteByte(' ')
	}
}

func main() {
	defer writer.Flush()
	scanner.Split(bufio.ScanWords)
	var x, h, m, result int = ReadInt32(), ReadInt32(), ReadInt32(), 0
	for !strings.Contains(strings.Join([]string {strconv.Itoa(h), strconv.Itoa(m)}, ""), "7") {
		result++
		m -= x
		if m < 0 {
			m += 60
			h -= 1
			if (h < 0) {
				h += 24
			}
		}
	}
	PrintInts(result)
	writer.WriteByte('\n')
}