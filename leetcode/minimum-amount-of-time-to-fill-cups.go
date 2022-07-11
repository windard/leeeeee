package main

import (
    "fmt"
    "sort"
)

func fillCups2(amount []int) int {
    // 辗转相除法
    if len(amount) < 1 {
        return 0
    }
    sort.Slice(amount, func(i, j int) bool {
        return amount[i] > amount[j]
    })

    var total int
    first := amount[0]
    for _, num := range amount[1:] {
        if first > num {
            total += num
            first = first - num
        } else {
            total += first
            first = num - first
        }
    }
    return total + first
}

func fillCups(amount []int) int {
    // 还是用分类讨论的方案
    if len(amount) < 3 {
        return 0
    }
    a, b, c := amount[0], amount[1], amount[2]
    maxValue := max(max(a, b), c)
    totalValue := a + b + c
    if totalValue-maxValue <= maxValue {
        return maxValue
    }
    // 上面的很好理解，当最大值，大于剩下两个值之和的时候，结果就是最大值
    // 下面的也可以计算得出，直接给结论就是能凑和到一起
    //return (totalValue-maxValue*2+1)/2 + maxValue
    // 或者另一种说法，叫肯定能匹配上，就是全量+1除2的结果
    return (totalValue + 1) / 2
}

func fillCups4(amount []int) int {
    // 永远用最大的两个数去凑
    if len(amount) < 2 {
        return 0
    }
    var total int
    for {
        sort.Slice(amount, func(i, j int) bool {
            return amount[i] > amount[j]
        })
        if amount[0] > 0 && amount[1] > 0 {
            amount[0]--
            amount[1]--
            total++
        } else {
            total += amount[0]
            return total
        }
    }
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func main() {
    fmt.Println(fillCups([]int{1, 3, 4}))
    fmt.Println(fillCups([]int{1, 2, 4}))
    fmt.Println(fillCups([]int{5, 4, 4})) // 7
    fmt.Println(fillCups([]int{5, 3, 5})) // 7
    fmt.Println(fillCups([]int{5, 0, 0}))
}

// 3 +(4,3) + 3 + 1
// 5, 8,
