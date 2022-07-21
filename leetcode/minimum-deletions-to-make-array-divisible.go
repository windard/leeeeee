package main

import (
    "fmt"
    "sort"
)

func minOperations3(nums []int, numsDivide []int) int {
    // 不但要把除数排序
    // 我们把被除数也排个序，如果能够整除，那肯定比被除数中最小的还要小
    // 这个数据更长，还是超时

    // 先去个重吧
    numMap := make(map[int]int)
    divideMap := make(map[int]int)
    for _, num := range nums {
        numMap[num]++
    }
    for _, num := range numsDivide {
        divideMap[num]++
    }
    nums = make([]int, 0, len(numMap))
    for num := range numMap {
        nums = append(nums, num)
    }
    numsDivide = make([]int, 0, len(divideMap))
    for num := range divideMap {
        numsDivide = append(numsDivide, num)
    }
    sort.Ints(nums)
    fmt.Printf("sorted nums:%+v\n", nums)
    sort.Ints(numsDivide)
    fmt.Printf("sorted numsDivide:%+v\n", numsDivide)

    if len(numsDivide) < 1 {
        return -1
    }
    if len(nums) < 1 {
        return 0
    }
    var index int
    var flag bool
    var total int
    for i := 1; i <= numsDivide[0]; i++ {
        flag = true
        for _, div := range numsDivide {
            if div%i != 0 {
                flag = false
                break
            }
        }
        if flag {
            // i 是一个除数
            for {
                if nums[index] < i {
                    total += numMap[nums[index]]
                } else if nums[index] == i {
                    return total
                } else {
                    break
                }
                index++
            }
        }
    }
    return -1
}

func gcd3(a, b int) int {
    if a%b == 0 {
        return b
    }
    return gcd3(b, a%b)
}

func gcd(a, b int) int {
    for b != 0 {
        a, b = b, a%b
    }
    return a
}

func minOperations(nums []int, numsDivide []int) int {
    // 但是，最快的方法，还是用 gcd
    numMap := make(map[int]int)
    divideMap := make(map[int]int)
    for _, num := range nums {
        numMap[num]++
    }
    for _, num := range numsDivide {
        divideMap[num]++
    }
    nums = make([]int, 0, len(numMap))
    for num := range numMap {
        nums = append(nums, num)
    }
    // 需要再排个序
    sort.Ints(nums)

    minFactor := 0
    for num := range divideMap {
        minFactor = gcd(minFactor, num)
    }

    // 只要求出最大公约数，后面就是直接算，也是 O(n) 的复杂度，并没有很难
    fmt.Printf("gcd min:%d\n", minFactor)
    var total int

    for _, num := range nums {
        if minFactor%num == 0 {
            return total
        } else {
            total += numMap[num]
        }
    }
    return -1
}

func minOperations2(nums []int, numsDivide []int) int {
    // 没太看懂题目，难道是先排序，再删除最小元素？
    // 说明做的没错，思路是对的，第一次在 Golang 里竟然也遇到超时
    // Time Limited
    numMap := make(map[int]int)
    divideMap := make(map[int]int)
    for _, num := range nums {
        numMap[num]++
    }
    for _, num := range numsDivide {
        divideMap[num]++
    }
    nums = make([]int, 0, len(numMap))
    for num := range numMap {
        nums = append(nums, num)
    }
    numsDivide = make([]int, 0, len(divideMap))
    for num := range divideMap {
        numsDivide = append(numsDivide, num)
    }
    sort.Ints(nums)
    fmt.Printf("sorted nums:%+v\n", nums)
    //sort.Ints(numsDivide)
    fmt.Printf("sorted numsDivide:%+v\n", numsDivide)

    // 真的没想到吖，方法是对的，就是去重一下就好了
    // 那这个的复杂度和上面的相比呢？
    // 其实还是上面的复杂性高一点，除非他能快速求素数
    //fmt.Printf("sorted nums:%+v\n", nums)
    var flag bool
    var total int
    for index, num := range nums {
        flag = true
        for _, div := range numsDivide {
            if div%num != 0 {
                flag = false
                break
            }
        }
        if flag {
            return total
        }
        total += numMap[nums[index]]
    }
    return -1
}

func main() {
    fmt.Println(minOperations([]int{2, 3, 2, 4, 3}, []int{9, 6, 9, 3, 15}))    // 2
    fmt.Println(minOperations([]int{1, 2, 3, 2, 4, 3}, []int{9, 6, 9, 3, 15})) // 0
    fmt.Println(minOperations([]int{4, 3, 6}, []int{8, 2, 6, 10}))             // -1
    fmt.Println(gcd(1, 2))
    fmt.Println(gcd(1, 3))
    fmt.Println(gcd(2, 22))
    fmt.Println(gcd(2, 3))
    fmt.Println(gcd(3, 3))
    fmt.Println(gcd(3, 2))
}
