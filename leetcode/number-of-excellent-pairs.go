package main

import (
    "fmt"
    "math/bits"
    "strconv"
)

func countExcellentPairs2(nums []int, k int) int64 {
    // 感觉很奇怪吖。
    // 1. 先去重
    // 2. 计算重复的两个数
    // 3. 两个数排列组合
    numMap := make(map[int]int)
    for _, num := range nums {
        numMap[num]++
    }
    var total int64
    //for num := range numMap {
    //    if (checkExcellent(num&num) + checkExcellent(num|num)) >= k {
    //        total++
    //    }
    //}
    length := len(numMap)
    numList := make([]int, 0, length)
    for num := range numMap {
        numList = append(numList, num)
    }
    for i := 0; i < length; i++ {
        for j := i; j < length; j++ {
            if (checkExcellent(numList[i]&numList[j]) + checkExcellent(numList[i]|numList[j])) >= k {
                total++
                if i != j {
                    total++
                }
            }
        }
    }
    return total
}

func countExcellentPairs(nums []int, k int) int64 {
    // 两个要点吧
    // 1. 不要去实际进行操作 bitCount(a&b) + bitCount(a|b) = bitCount(a) + bitCount(b)
    // 2. 不要遍历，双重遍历 O(n^2) 太复杂了，使用哈希表查询
    // 同样的，还是需要先去重
    // 但是最后不用去重么？？？？
    var total int64
    var ok bool
    numMap := make(map[int]int)
    bitMap := make(map[int]int)

    for _, num := range nums {
        if _, ok = numMap[num]; !ok {
            bitMap[checkExcellent(num)]++
            numMap[num]++
        }
    }
    fmt.Println(bitMap)
    for i, count1 := range bitMap {
        for j, count2 := range bitMap {
            if i+j >= k {
                // 好吧，使用 哈希map 进行双重遍历的时候
                // 实际对于每一个值，也只进行了一次重复计算，比如 {1:x,2:y}
                // 对于 11, 22 都只计算了一次，还有 12, 和 21
                fmt.Println(i, j, count1, count2, count1*count2)
                total += int64(count1 * count2)
            }
        }
    }
    return total
}

func countExcellentPairs4(nums []int, k int) int64 {
    // 还是在想 and 和 or 的操作
    // bitCount(a&b) + bitCount(a|b) = bitCount(a) + bitCount(b)
    // 所以压根就不需要位运算，直接算就可以 😂
    // **然后加一个缓存**
    // 受不了了，还是超时，已经提交失败8回了
    // 还是双重遍历太超时, 结果是按照 2-sum 一样来做，再加一个哈希表
    numMap := make(map[int]int)
    for _, num := range nums {
        numMap[num]++
    }
    var total int64
    var count int
    var ok bool
    BitMap := make(map[int]int)

    length := len(numMap)
    numList := make([]int, 0, length)
    for num := range numMap {
        if count, ok = BitMap[num]; !ok {
            count = checkExcellent(num)
            BitMap[num] = count
        }
        if count >= k {
            total += int64(length)
            total += int64(length - 1)
            length--
            continue
        }
        numList = append(numList, num)
    }
    length = len(numList)
    for i := 0; i < length; i++ {
        for j := i; j < length; j++ {
            if count, ok = BitMap[numList[i]]; !ok {
                count = checkExcellent(numList[i])
            }
            if count, ok = BitMap[numList[j]]; !ok {
                count = checkExcellent(numList[j])
            }
            if BitMap[numList[i]]+BitMap[numList[j]] >= k {
                total++
                if i != j {
                    total++
                }
            }
        }
    }
    return total
}

func countExcellentPairs5(nums []int, k int) int64 {
    // 再想想 and 和 or 操作，难道就根本不需要执行？
    // 可以开始直接数的，如果直接数就大于的话，那就完全没问题
    // 但是还是会有交错，直接数不大于，交错之后可能大于可能小于
    // 都这样了，还是超时
    numMap := make(map[int]int)
    for _, num := range nums {
        numMap[num]++
    }
    var total int64

    length := len(numMap)
    numList := make([]int, 0, length)
    for num := range numMap {
        // 先数自己的个数够不够,如果自己就够了，那其他都不用算
        if compareExcellent(num, k) {
            // 这里已经加完了，就应该在 num list 中将这个数摘掉
            // fmt.Println(i, numList[i]) // +7
            total += int64(length)
            total += int64(length - 1)
            length--
            continue
        }
        numList = append(numList, num)
    }
    //fmt.Println(numList)
    length = len(numList)
    for i := 0; i < length; i++ {
        // 如果自己不够，还是需要合并计算一下的
        for j := i; j < length; j++ {
            if checkExcellentPair(numList[i], numList[j], k) {
                //fmt.Println(i, j, numList[i], numList[j])
                total++
                if i != j {
                    total++
                }
            }
        }
    }
    return total
}

func compareExcellent(num, k int) bool {
    var count int
    for num > 0 {
        if num%2 == 1 {
            count++
        }
        if count >= k {
            return true
        }
        num /= 2
    }
    return count >= k
}

func countExcellentPairs3(nums []int, k int) int64 {
    // 我就知道，Hard 难度的题目，很多都是超时问题
    // 其实简单做也可以，就是太慢了
    // 难道非要我去数1的个数？
    // 还是 Time Limit
    numMap := make(map[int]int)
    for _, num := range nums {
        numMap[num]++
    }
    var total int64

    length := len(numMap)
    numList := make([]int, 0, length)
    for num := range numMap {
        numList = append(numList, num)
    }
    for i := 0; i < length; i++ {
        for j := i; j < length; j++ {
            if countExcellentPair(numList[i], numList[j], k) {
                total++
                if i != j {
                    total++
                }
            }
        }
    }
    return total
}

func countExcellentPair(m, n, k int) bool {
    var num string
    var count int
    num = strconv.FormatInt(int64(m&n), 2)
    for _, s := range num {
        if s == '1' {
            count++
        }
        if count >= k {
            return true
        }
    }

    num = strconv.FormatInt(int64(m|n), 2)
    for _, s := range num {
        if s == '1' {
            count++
        }
        if count >= k {
            return true
        }
    }
    return count >= k
}

func checkPairBitCount(m, n, k int) bool {
    var num, count int
    num = m
    for num > 0 {
        if num%2 == 1 {
            count++
        }
        if count >= k {
            return true
        }
        num /= 2
    }

    num = n
    for num > 0 {
        if num%2 == 1 {
            count++
        }
        if count >= k {
            return true
        }
        num /= 2
    }
    return count >= k
}

func checkExcellentPair(m, n, k int) bool {
    var num, count int
    num = m & n
    for num > 0 {
        if num%2 == 1 {
            count++
        }
        if count >= k {
            return true
        }
        num /= 2
    }

    num = m | n
    for num > 0 {
        if num%2 == 1 {
            count++
        }
        if count >= k {
            return true
        }
        num /= 2
    }
    return count >= k
}

func checkExcellent(num int) int {
    var count int
    for num > 0 {
        if num%2 == 1 {
            count++
        }
        num /= 2
    }
    return count
}

func main() {
    fmt.Println(countExcellentPairs([]int{1, 2, 3, 1}, 3)) // 5
    //fmt.Println(countExcellentPairs([]int{5, 1, 1}, 10))                         // 0
    //fmt.Println(countExcellentPairs([]int{1, 2, 4, 8, 16, 32, 64, 128, 256}, 2)) // 81
    // 536870911,1,2,3
    // -  , 01, 10, 11
    // 4+3+2+2+1
    //fmt.Println(countExcellentPairs([]int{1, 2, 3, 1, 536870911}, 3))            // 12 为什么这个数字在跳，不稳定
    //fmt.Println(countExcellentPairs([]int{1, 2, 3, 1, 536870911, 536870911}, 3)) // 12 为什么这个数字在跳，不稳定
    // 7568 为什么这个数字也在跳，不稳定，而且上一个还能偶尔跳到正确的结果，这个就是硬跳不出来
    //fmt.Println(countExcellentPairs([]int{745123522, 780161922, 911692878, 291515362, 14407582, 800657985, 624198170, 327318213, 585359689, 475046415, 253647481, 607006144, 193773180, 740345687, 288638626, 62148920, 195444115, 567630485, 675976710, 404053108, 815429249, 394651351, 204402513, 196037308, 435520151, 69326238, 900657931, 417009691, 788087674, 89101495, 147261023, 179147246, 391108168, 261006719, 947442692, 869519137, 557287962, 204511054, 150454379, 508441073, 917846620, 789335735, 999055845, 810841158, 663483743, 712002146, 49711011, 551107101, 823259177, 756685512, 305977547, 214707124, 798707203, 575883326, 312001764, 296144914, 445448565, 572453004, 517300168, 771625989, 73238714, 922313152, 848421606, 525431023, 399862870, 392370160, 355935135, 455468812, 609775395, 270125020, 574119054, 37201941, 984483544, 96695229, 839848442, 251453685, 324213598, 269361289, 613270367, 359845759, 495008173, 982883976, 870123636, 560164536, 275413875, 462592203, 775982309}, 19))
    fmt.Println(bits.OnesCount(536870911))
}
