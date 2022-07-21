package main

import (
    "fmt"
    "sort"
    "strconv"
)

func calculateSmallestNumber(numList []string, query []int) int {
    var nums []string
    smallestIndex := query[0]
    leftIndex := query[1]
    if leftIndex < 1 {
        return -1
    }
    for _, numStr := range numList {
        if len(numStr) < leftIndex {
            return -1
        }
        numStr = numStr[len(numStr)-leftIndex:]
        nums = append(nums, numStr)
    }
    //fmt.Printf("clean data:%+v\n", nums)

    sortedNum := make([][]interface{}, 0, len(nums))
    var index int
    var num string
    var item []interface{}
    for index, num = range nums {
        item = make([]interface{}, 0)
        item = append(item, num)
        item = append(item, index)
        sortedNum = append(sortedNum, item)
    }
    //fmt.Printf("left data:%+v\n", sortedNum)

    sort.SliceStable(sortedNum, func(i, j int) bool {
        numi := sortedNum[i][0].(string)
        numj := sortedNum[j][0].(string)

        indexi := sortedNum[i][1].(int)
        indexj := sortedNum[j][1].(int)
        return compareMax(numi, numj, indexi, indexj)
    })

    //fmt.Printf("sorted nums:%+v\n", sortedNum)
    var numPair []interface{}
    for index, numPair = range sortedNum {
        if index+1 == smallestIndex {
            return numPair[1].(int)
        }
    }

    return 0
}

func compareMax(a, b string, i, j int) bool {
    if len(a) != len(b) {
        return false
    }
    for index := range a {
        if a[index] < b[index] {
            return true
        } else if a[index] > b[index] {
            return false
        }
    }
    return i < j
}

func calculateSmallestNumber2(numList []string, query []int) int {
    // 找到剪裁之后的第 k 小的数的下标
    // 因为数字太长，不能转成数字去做
    var nums []int64
    smallestIndex := query[0]
    leftIndex := query[1]
    if leftIndex < 1 {
        return -1
    }
    var num int64
    var err error
    for _, numStr := range numList {
        if len(numStr) < leftIndex {
            return -1
        }
        numStr = numStr[len(numStr)-leftIndex:]
        num, err = strconv.ParseInt(numStr, 10, 0)
        if err != nil {
            num = 2 ^ 63
            //return -1
        }
        nums = append(nums, num)
    }
    fmt.Printf("clean data:%+v\n", nums)

    sortedNum := make([][]int64, 0, len(nums))
    var index int
    for index, num = range nums {
        sortedNum = append(sortedNum, []int64{num, int64(index)})
    }
    sort.SliceStable(sortedNum, func(i, j int) bool {
        return sortedNum[i][0] < sortedNum[j][0] || sortedNum[i][1] < sortedNum[j][1]
    })
    //fmt.Printf("sorted nums:%+v\n", sortedNum)
    var numPair []int64
    for index, numPair = range sortedNum {
        if index+1 == smallestIndex {
            return int(numPair[1])
        }
    }
    // 总算把数据都清洗出来了，然后再计算最 k 小的树的下标
    //sortedNum := make([]int, 0, len(nums))
    //for _, num = range nums {
    //    sortedNum = append(sortedNum, num)
    //}
    //sort.Ints(sortedNum)
    //
    //if smallestIndex > len(nums) {
    //    return -1
    //}
    //fmt.Printf("sorted nums:%+v\n", sortedNum)
    //
    //targetNum := sortedNum[smallestIndex-1]
    //var index int
    //fmt.Printf("small index:%d, target num:%+v\n", smallestIndex, targetNum)
    //
    //// 有相同的话，也不是取第一个，也不是取最后一个，而是按下标的先后顺序，取指定位数个
    //for index, num = range nums {
    //    if num == targetNum {
    //        return index
    //    }
    //}
    return -1
}

func smallestTrimmedNumbers(nums []string, queries [][]int) []int {
    // 题目都很难懂
    // 先要把题目做批量操作
    // 找到剪裁之后的第 k 小的数的下标
    // 所以还是排序问题？
    result := make([]int, 0, len(queries))
    for _, query := range queries {
        result = append(result, calculateSmallestNumber(nums, query))
    }
    return result
}

func main() {
    // 做到吐血，真的就是再考各种排序算法的，主要能否 AC，就看排序稳不稳
    // 以及直接暴力的话，看编程语言快不快，（Python 🌶🐔
    s := "123"
    fmt.Printf("3>2:%+v\n", s[2] > s[1])
    fmt.Printf("2>1:%+v\n", s[1] > s[0])
    fmt.Printf("3>1:%+v\n", s[2] > s[0])
    // [2,2,1,0]
    fmt.Println(smallestTrimmedNumbers([]string{"102", "473", "251", "814"}, [][]int{{1, 1}, {2, 3}, {4, 2}, {1, 2}}))
    // {3,0}
    fmt.Println(smallestTrimmedNumbers([]string{"24", "37", "96", "04"}, [][]int{{2, 1}, {2, 2}}))
    // [10,0,9,9,1,6,5,0,9]
    fmt.Println(smallestTrimmedNumbers(
        []string{"325240361872", "440618160237", "785744447413", "820980201297", "470082520306", "874146483840", "425300857082", "088636787077", "813218016629", "459000328006", "188683382600"},
        [][]int{{6, 7}, {4, 4}, {1, 8}, {11, 10}, {4, 8}, {11, 6}, {1, 1}, {3, 1}, {11, 10}},
    ))
    // [26,16,16,13,12,19,13,22,25,11,0,10,19,3,11,10,0,13,3,2,13,5,10,13,2,12,3,12,20]
    fmt.Println(smallestTrimmedNumbers(
        []string{"8331019423839036903", "2215783497319194533", "3244863164120264914", "2723857887888553250", "1069645833408356268", "3799170975306313470", "3300849027471666477", "8896469467436127218", "9595084104356246555", "4601424390471226348", "2777623221871959897", "2660664761264162910", "4830224756337097853", "2239177595019260973", "5704104074606481922", "5158962343348888307", "4957489822885409209", "5533958195540658313", "6712811206814843536", "9775503283462317096", "1975389311819120035", "1292135637676764140", "9838972337538013522", "7609294617007602893", "0186572359592634437", "9236053726818307461", "7264888050655615544", "4990296885039745852", "1417868535147288083"},
        [][]int{{22, 19}, {16, 17}, {10, 7}, {27, 16}, {9, 9}, {21, 4}, {24, 2}, {12, 11}, {2, 5}, {24, 12}, {25, 7}, {7, 13}, {14, 9}, {23, 15}, {18, 17}, {22, 16}, {4, 14}, {14, 17}, {25, 11}, {12, 16}, {29, 3}, {22, 11}, {29, 2}, {24, 2}, {24, 15}, {7, 14}, {7, 3}, {7, 14}, {1, 3}},
    ))
}
