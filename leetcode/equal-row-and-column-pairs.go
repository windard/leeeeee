package main

import "fmt"

func equalPairs(grid [][]int) int {
    // 因为看错 test case，而错失两次机会
    // 我就知道有人用字符串的，不过要注意一点 separator
    // 之前就想到了，没有分割符的话，就是会连起来
    m := len(grid)
    if m < 1 {
        return 0
    }
    n := len(grid[0])
    if n < 1 {
        return 0
    }

    var total int
    var rowS, colS string
    rowHashMap := make(map[string]int, m)
    for i := 0; i < m; i++ {
        rowS = ""
        for j := 0; j < n; j++ {
            rowS += fmt.Sprintf(":%d", grid[i][j])
        }
        rowHashMap[rowS]++
    }

    for j := 0; j < n; j++ {
        colS = ""
        for i := 0; i < m; i++ {
            colS += fmt.Sprintf(":%d", grid[i][j])
        }
        total += rowHashMap[colS]
    }
    return total
}

func main() {
    // 3, 2, 1
    // 1, 7, 6
    // 2, 7, 7
    fmt.Println(equalPairs([][]int{{3, 2, 1}, {1, 7, 6}, {2, 7, 7}}))          // 1
    fmt.Println(equalPairs([][]int{{3, 3, 2, 1}, {1, 1, 7, 6}, {2, 2, 7, 7}})) // 0
    // 3, 1, 2, 2
    // 1, 4, 4, 5
    // 2, 4, 2, 2
    // 2, 4, 2, 2
    fmt.Println(equalPairs([][]int{{3, 1, 2, 2}, {1, 4, 4, 5}, {2, 4, 2, 2}, {2, 4, 2, 2}})) // 3
    // 1, 1
    // 1, 1
    fmt.Println(equalPairs([][]int{{1, 1}, {1, 1}})) // 4
    // 3, 1, 2, 2
    // 1, 4, 4, 4
    // 2, 4, 2, 2
    // 2, 5, 2, 2
    fmt.Println(equalPairs([][]int{{3, 1, 2, 2}, {1, 4, 4, 4}, {2, 4, 2, 2}, {2, 5, 2, 2}})) // 3
    // 11, 1
    // 1,  11
    fmt.Println(equalPairs([][]int{{11, 1}, {1, 11}})) // 2
}
