package main

import "fmt"

type SmallestInfiniteSet struct {
    // 数据量其实没有那么大，用黑名单记录即可
    // 好吧，其实题目里提到了，总共操作1000次，所以就是1000个数据
    // 所以其实是使用黑名单的方式来做的，使用哈希表或者有限队列
    deletedSet map[int]bool
}

func Constructor() SmallestInfiniteSet {
    // 默认包含所有正整数
    return SmallestInfiniteSet{deletedSet: map[int]bool{}}
}

func (this *SmallestInfiniteSet) PopSmallest() int {
    var min int
    min = 1
    for {
        if _, ok := this.deletedSet[min]; !ok {
            this.deletedSet[min] = true
            return min
        }
        min++
    }
}

func (this *SmallestInfiniteSet) AddBack(num int) {
    delete(this.deletedSet, num)
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * obj := Constructor()
 * param_1 := obj.PopSmallest()
 * obj.AddBack(num)
 */

func main() {
    smallestInfiniteSet := Constructor()
    smallestInfiniteSet.AddBack(2)                 // 2 已经在集合中，所以不做任何变更。
    fmt.Println(smallestInfiniteSet.PopSmallest()) // 返回 1 ，因为 1 是最小的整数，并将其从集合中移除。
    fmt.Println(smallestInfiniteSet.PopSmallest()) // 返回 2 ，并将其从集合中移除。
    fmt.Println(smallestInfiniteSet.PopSmallest()) // 返回 3 ，并将其从集合中移除。
    smallestInfiniteSet.AddBack(1)                 // 将 1 添加到该集合中。
    fmt.Println(smallestInfiniteSet.PopSmallest()) // 返回 1 ，因为 1 在上一步中被添加到集合中，
    // 且 1 是最小的整数，并将其从集合中移除。
    fmt.Println(smallestInfiniteSet.PopSmallest()) // 返回 4 ，并将其从集合中移除。
    fmt.Println(smallestInfiniteSet.PopSmallest()) // 返回 5 ，并将其从集合中移除。

}
