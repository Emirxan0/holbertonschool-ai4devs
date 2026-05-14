package main
import ("fmt"; "sync")
func main() {
    var wg sync.WaitGroup
    wg.Add(1)
    go func() { defer wg.Done(); fmt.Println("Processing data...") }()
    wg.Wait()
    fmt.Println("Main function finished")
}
