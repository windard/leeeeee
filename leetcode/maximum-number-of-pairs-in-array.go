package main

import "fmt"

func numberOfPairs(nums []int) []int {
    if len(nums) < 2 {
        return []int{0, len(nums)}
    }
    // 先排序，再筛选
    // 或者使用 哈希
    numMap := make(map[int]int, 100)
    for _, num := range nums {
        if count, ok := numMap[num]; ok {
            numMap[num] = count + 1
        } else {
            numMap[num] = 1
        }
    }
    var suc, lef int
    for _, count := range numMap {
        suc += count / 2
        lef += count % 2
    }
    return []int{suc, lef}
}

func main() {
    fmt.Println(numberOfPairs([]int{1, 3, 2, 1, 3, 2, 2})) // [3,1]
    fmt.Println(numberOfPairs([]int{1, 1}))                // [1,0]
    fmt.Println(numberOfPairs([]int{0}))                   // [0,1]
}
