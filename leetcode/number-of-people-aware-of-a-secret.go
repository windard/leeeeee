package main

import "fmt"

//const modNum = 1000_000_000 + 7
const modNum = 1e9 + 7

func peopleAwareOfSecret(n int, delay int, forget int) int {
    if n < 1 {
        return 0
    }
    days := make([]int, n)
    days[0] = 1

    for i := 0; i < n; i++ {
        for j := delay + i; j < forget+i && j < n; j++ {
            days[j] += days[i] % modNum
        }
    }

    var total int
    for i := n - 1; i > n-forget-1; i-- {
        total += days[i] % modNum
    }
    return total % modNum
}

func peopleAwareOfSecret2(n int, delay int, forget int) int {
    queue := make([]int, forget)
    queue[0] = 1
    var total, left int
    for i := 0; i < n-1; i++ {
        //total += queue[forget-1]
        //total %= modNum

        for j := forget - 1; j > 0; j-- {
            queue[j] = queue[j-1]
        }
        left = 0
        for j := delay; j < forget; j++ {
            left += queue[j]
        }
        queue[0] = left % modNum
    }

    for _, num := range queue {
        total += num
        total %= modNum
    }
    return total
}

func main() {
    fmt.Println(modNum)
    fmt.Println(peopleAwareOfSecret(6, 2, 4))      // 5
    fmt.Println(peopleAwareOfSecret(60, 2, 4))     // 18186515
    fmt.Println(peopleAwareOfSecret(600, 2, 4))    // 315028193
    fmt.Println(peopleAwareOfSecret(4, 1, 3))      // 6
    fmt.Println(peopleAwareOfSecret(684, 18, 496)) // 653668527
}
