package main
import "fmt"
func main() {
	var n, k int
	fmt.Scan(&n)
	fmt.Scan(&k)
	r, a := 1, make([]int, n)
	for i := range a { fmt.Scan(&a[i]) }
	for _, ai := range a {
		if ai <= k && k % ai == 0 && ai > r { r = ai }
	}
	fmt.Println(k / r)
}