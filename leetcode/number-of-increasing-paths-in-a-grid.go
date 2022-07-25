package main

import "fmt"

const modNum = 1e9 + 7

func countPaths(grid [][]int) int {
    // 还是需要一个快速寻找法
    // 那就用 DP 吧
    // 每个点记录下自己能够 touch 到的数量
    // 也就是说以自己为起点的数量
    // 之前是记录的以自己为终点的数量
    // 那就需要用到回溯
    if len(grid) == 0 {
        return 0
    }
    m := len(grid)
    if len(grid[0]) == 0 {
        return 0
    }
    n := len(grid[0])

    matrix := make([][]int, m)
    for i := 0; i < m; i++ {
        matrix[i] = make([]int, n)
        for j := 0; j < n; j++ {
            matrix[i][j] = 0
        }
    }
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            countPath(i, j, grid, matrix)
        }
    }
    var total int
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            total += matrix[i][j] % modNum
        }
    }

    return total % modNum
}

func countPath(i, j int, grid, matrix [][]int) (count int) {
    if i < 0 || j < 0 {
        return
    }
    if i >= len(grid) || j >= len(grid[0]) {
        return
    }
    if matrix[i][j] != 0 {
        return matrix[i][j]
    }

    count = 1
    if i-1 >= 0 {
        if grid[i][j] < grid[i-1][j] {
            count += countPath(i-1, j, grid, matrix) % modNum
        }
    }

    // 下
    if i+1 < len(grid) {
        if grid[i][j] < grid[i+1][j] {
            count += countPath(i+1, j, grid, matrix) % modNum
        }
    }
    // 左
    if j-1 >= 0 {
        if grid[i][j] < grid[i][j-1] {
            count += countPath(i, j-1, grid, matrix) % modNum
        }
    }
    // 右
    if j+1 < len(grid[0]) {
        if grid[i][j] < grid[i][j+1] {
            count += countPath(i, j+1, grid, matrix) % modNum
        }
    }
    count %= modNum
    matrix[i][j] = count
    return count
}

func countPaths3(grid [][]int) int {
    // 想到的另一个办法就是
    // 每个数从自己周围开始找，依次找到较大的数，去加1
    // 还是超时 Time Limit
    if len(grid) == 0 {
        return 0
    }
    m := len(grid)
    if len(grid[0]) == 0 {
        return 0
    }
    n := len(grid[0])

    matrix := make([][]int, m)
    for i := 0; i < m; i++ {
        matrix[i] = make([]int, n)
        for j := 0; j < n; j++ {
            matrix[i][j] = 1
        }
    }
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            expendMatrix(i, j, grid, matrix)
        }
    }
    var total int
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            total += matrix[i][j] % modNum
        }
    }

    return total % modNum
}

func expendMatrix(i, j int, grid, matrix [][]int) {
    if i < 0 || j < 0 {
        return
    }
    if i >= len(grid) || j >= len(grid[0]) {
        return
    }

    // 上
    if i-1 >= 0 {
        if grid[i][j] < grid[i-1][j] {
            matrix[i-1][j]++
            matrix[i-1][j] %= modNum
            expendMatrix(i-1, j, grid, matrix)
        }
    }

    // 下
    if i+1 < len(grid) {
        if grid[i][j] < grid[i+1][j] {
            matrix[i+1][j]++
            matrix[i+1][j] %= modNum

            expendMatrix(i+1, j, grid, matrix)
        }
    }
    // 左
    if j-1 >= 0 {
        if grid[i][j] < grid[i][j-1] {
            matrix[i][j-1]++
            matrix[i][j-1] %= modNum

            expendMatrix(i, j-1, grid, matrix)
        }
    }
    // 右
    if j+1 < len(grid[0]) {
        if grid[i][j] < grid[i][j+1] {
            matrix[i][j+1]++
            matrix[i][j+1] %= modNum
            expendMatrix(i, j+1, grid, matrix)
        }
    }
    return
}

func countPaths2(grid [][]int) int {
    // Time Limit
    // 思路没问题，我就知道，Hard 的题目，怎么可能这么简单
    // m^2*n^2
    if len(grid) == 0 {
        return 0
    }
    m := len(grid)
    if len(grid[0]) == 0 {
        return 0
    }
    n := len(grid[0])

    matrix := make([][]int, m)
    oldMatrix := make([][]int, m)
    for i := 0; i < m; i++ {
        matrix[i] = make([]int, n)
        oldMatrix[i] = make([]int, n)
        for j := 0; j < n; j++ {
            matrix[i][j] = 1
        }
    }

    total := m * n
    var count int
    flag := true
    for flag {
        for i := 0; i < m; i++ {
            for j := 0; j < n; j++ {
                oldMatrix[i][j] = matrix[i][j]
            }
        }

        flag = false
        for i := 0; i < m; i++ {
            for j := 0; j < n; j++ {

                count = 0
                if i > 0 && grid[i][j] > grid[i-1][j] {
                    count += oldMatrix[i-1][j]
                }
                if j > 0 && grid[i][j] > grid[i][j-1] {
                    count += oldMatrix[i][j-1]
                }
                if i < m-1 && grid[i][j] > grid[i+1][j] {
                    count += oldMatrix[i+1][j]
                }
                if j < n-1 && grid[i][j] > grid[i][j+1] {
                    count += oldMatrix[i][j+1]
                }
                matrix[i][j] = count % modNum
                total += matrix[i][j]
                if count != 0 {
                    flag = true
                }
            }
        }
    }
    return total % modNum
}

func main() {
    fmt.Println(countPaths([][]int{{1, 1}, {3, 4}})) // 8
    fmt.Println(countPaths([][]int{{1}, {2}}))       // 3
}
