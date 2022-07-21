package main

import "fmt"

func countDigits(num int) int {
    var total int
    for num != 0 {
        total += num % 10
        num = num / 10
    }
    return total
}
func min(a, b int) int {
    if a > b {
        return b
    }
    return a
}

func countMaxTwoSum(nums []int) int {
    if len(nums) < 2 {
        return 0
    }

    var sum, minNum, LastMin int
    sum = nums[0] + nums[1]
    LastMin = min(nums[0], nums[1])
    for _, num := range nums[2:] {
        minNum = min(num, min(LastMin, sum-LastMin))
        if minNum < LastMin {
            continue
        }
        sum -= minNum
        sum += num
        LastMin = min(num, sum-num)
    }
    return sum
}

func maximumSum2(nums []int) int {
    if len(nums) < 2 {
        return -1
    }
    numMap := make(map[int][]int)
    var numList []int
    var ok bool
    var digits int
    for _, num := range nums {
        digits = countDigits(num)

        if numList, ok = numMap[digits]; !ok {
            numList = make([]int, 0)
        }
        numList = append(numList, num)
        numMap[digits] = numList
    }
    var sum, maxSum int

    //fmt.Println(numMap)
    var countOnce bool
    for _, numList = range numMap {
        sum = 0
        if len(numList) < 2 {
            continue
        }
        countOnce = true

        sum = countMaxTwoSum(numList)
        if sum > maxSum {
            maxSum = sum
        }
    }
    if !countOnce {
        return -1
    }
    return maxSum
}

func maximumSum4(nums []int) int {
    ans := -1
    mx := map[int]int{}
    for _, v := range nums {
        s := 0
        for x := v; x > 0; x /= 10 {
            s += x % 10
        }
        if mx[s] > 0 {
            ans = max(ans, mx[s]+v)
        }
        mx[s] = max(mx[s], v)
    }
    return ans
}

func maximumSum(nums []int) int {
    // maxMap 永远只记录最大的单个值
    maxMap := make(map[int]int)
    maxSum := -1
    numCount := 0
    for _, num := range nums {
        numCount = 0
        for i := num; i > 0; i = i / 10 {
            numCount += i % 10
        }
        if _, ok := maxMap[numCount]; ok {
            maxSum = max(maxSum, maxMap[numCount]+num)
        }
        maxMap[numCount] = max(maxMap[numCount], num)
    }
    return maxSum
}

func max(a, b int) int {
    if b > a {
        return b
    }
    return a
}

func main() {
    fmt.Println(maximumSum([]int{18, 43, 36, 63, 7})) // 54
    fmt.Println(maximumSum([]int{18, 43, 36, 13, 7})) // 54
    fmt.Println(maximumSum([]int{10, 12, 19, 14}))    // -1
    // 1925075390
    fmt.Println(maximumSum([]int{314593573, 110074004, 699559522, 673146088, 942819791, 869240392, 882704685, 539112585, 403921998, 255500178, 844178479, 767111119, 892897819, 885553426, 992987422, 914189130, 977810434, 152598980, 453977488, 389624268, 428531796, 839330802, 310252480, 378105000, 847373518, 934908066, 401794474, 663507194, 319531245, 614248496, 887058076, 278608939, 932087968, 282329958, 863096195, 98031682, 778619077, 471900584, 647816311, 469918315, 168055925, 550222361, 650029951, 280019987, 600359910, 803792276}))
    fmt.Println(countMaxTwoSum([]int{699559522, 844178479, 992987422, 278608939, 932087968, 778619077}))
}
