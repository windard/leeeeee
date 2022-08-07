package main

import (
    "fmt"
)

type FoodRatings struct {
    // 这么精妙的设计，竟然超时了... Time Limit
    // 那没办法，只能手写排序算法了
    // 都手写排序算法了，还是超出时间限制 Time Limit
    // 说明数据量是真的大，排序是真的复杂
    // 提交六次，终于通过
    // 最终总结
    // 1. 哈希表是必须的
    // 2. food 和 rate 使用 pair 存储，不要单独再拆
    // 3. 最好能有一个平衡树 去修改挑战
    // 4. 或者用堆，最大堆，每次插入都在堆顶
    // 对吖，应该就要用堆，这样每次插入都在堆顶很方便
    // 下次可以主动尝试一下
    // redblacktree or heap

    FoodRating     map[string]int
    FoodRegion     map[string]string
    HighestRate    map[string][]int
    RegionRateFood map[string]map[int][]string
}

func Constructor(foods []string, cuisines []string, ratings []int) FoodRatings {
    highestRate := make(map[string][]int)               // 记录每个地区分数排名
    foodRating := make(map[string]int)                  // 记录食物和分数
    foodRegion := make(map[string]string)               // 记录食物和地区
    regionRateFood := make(map[string]map[int][]string) // 记录地区分数和食物
    length := len(foods)
    var ratingList []int
    var foodList []string
    var ok bool
    var rateFood map[int][]string

    for i := 0; i < length; i++ {
        food := foods[i]
        rate := ratings[i]
        region := cuisines[i]

        foodRating[food] = rate
        foodRegion[food] = region

        if ratingList, ok = highestRate[region]; !ok {
            ratingList = make([]int, 0)
        }
        ratingList = append(ratingList, rate)
        highestRate[region] = ratingList

        if rateFood, ok = regionRateFood[region]; !ok {
            rateFood = make(map[int][]string)
        }
        rateFood[rate] = append(rateFood[rate], food)
        regionRateFood[region] = rateFood
    }
    for _, ratingList = range highestRate {
        InsertSort(ratingList)
    }
    for _, rateFood = range regionRateFood {
        for _, foodList = range rateFood {
            SortString(foodList)
        }
    }
    return FoodRatings{
        FoodRating:     foodRating,
        FoodRegion:     foodRegion,
        HighestRate:    highestRate,
        RegionRateFood: regionRateFood,
    }
}

func (this *FoodRatings) ChangeRating(food string, newRating int) {
    region := this.FoodRegion[food]
    rate := this.FoodRating[food]
    // 不再使用排序算法去排 ，直接现场插入排序走一轮
    highestRates := this.HighestRate[region]

    InsertOneSort(highestRates, rate, newRating)
    //InsertSort(highestRates)

    var rateFood, newRateFood []string
    var ok bool
    if newRateFood, ok = this.RegionRateFood[region][newRating]; !ok {
        newRateFood = make([]string, 0)
    }
    newRateFood = append(newRateFood, food)
    SortString(newRateFood)

    rateFood = this.RegionRateFood[region][rate]
    var index int
    var foodName string
    for index, foodName = range rateFood {
        if food == foodName {
            break
        }
    }
    rateFood = append(rateFood[:index], rateFood[index+1:]...)
    this.RegionRateFood[region][rate] = rateFood
    this.RegionRateFood[region][newRating] = newRateFood
    this.FoodRating[food] = newRating
    return
}

func (this *FoodRatings) HighestRated(cuisine string) string {
    highestRates := this.HighestRate[cuisine]
    if len(highestRates) < 1 {
        return ""
    }
    highestRate := highestRates[0]
    highestFoods := this.RegionRateFood[cuisine][highestRate]
    if len(highestFoods) < 1 {
        return ""
    }
    return highestFoods[0]
}

func InsertOneSort(highestRates []int, rate, newRating int) {
    if rate < newRating {
        var index, rating int
        // 0 , 1 , 2 , 3 , 4 , 5
        // 87, 35, 21, 13, 11, 6
        // 87, 35, 21, 53, 11, 6
        for index, rating = range highestRates {
            if rating == rate {
                break
            }
        }
        // index = 3
        lastMin := index
        for i := 0; i < index; i++ {
            if highestRates[i] < newRating {
                lastMin = i
                break
            }
        }
        // lastMin 之前的不变，之后的往后挪一个位置
        for i := index; i > lastMin; i-- {
            highestRates[i] = highestRates[i-1]
        }
        highestRates[lastMin] = newRating

    } else if rate > newRating {
        var index, rating int
        // 0 , 1 , 2 , 3 , 4 , 5
        // 87, 35, 21, 13, 11, 6
        // 87, 35, 10, 13, 11, 6
        for index, rating = range highestRates {
            if rating == rate {
                break
            }
        }
        length := len(highestRates)
        // index = 2
        lastMin := length - 1
        for i := index; i < length; i++ {
            if highestRates[i] < newRating {
                lastMin = i - 1
                break
            }
        }
        // lastMin 之前的往前移一位，之后的不变
        for i := index; i < lastMin; i++ {
            highestRates[i] = highestRates[i+1]
        }
        highestRates[lastMin] = newRating
    } else {
        return
    }
}
func InsertSort(l []int) {
    length := len(l)
    if length < 2 {
        return
    }
    // 从大到小
    // 0,1,2,3
    // 7,5,3,1
    var i, j int
    var tmpVar, tmpIdx int
    for i = 1; i < length; i++ {
        for j = 0; j < i; j++ {
            if l[j] < l[i] {
                break
            }
        }
        tmpIdx = j
        tmpVar = l[i]
        for j = i; j > tmpIdx; j-- {
            l[j] = l[j-1]
        }
        l[tmpIdx] = tmpVar
    }
}

func SortString(sl []string) {
    length := len(sl)
    if length < 2 {
        return
    }
    // 从小到大
    var i, j int
    var tmpIdx int
    var tmpVar string
    for i = 1; i < length; i++ {
        for j = 0; j < i; j++ {
            if sl[j] > sl[i] {
                break
            }
        }
        tmpIdx = j
        tmpVar = sl[i]
        for j = i; j > tmpIdx; j-- {
            sl[j] = sl[j-1]
        }
        sl[tmpIdx] = tmpVar
    }
}

func main() {
    inl := []int{87, 35, 21, 13, 11, 6}
    InsertOneSort(inl, 13, 53)
    fmt.Println(inl)
    inl = []int{76, 35, 21, 12, 11}
    InsertOneSort(inl, 12, 2)
    fmt.Println(inl)

    obj := Constructor(
        []string{"kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"},
        []string{"korean", "japanese", "japanese", "greek", "japanese", "korean"},
        []int{9, 12, 8, 15, 14, 7},
    )
    fmt.Println(obj.HighestRated("korean"))   // kimchi
    fmt.Println(obj.HighestRated("japanese")) // ramen
    obj.ChangeRating("sushi", 16)
    fmt.Println(obj.HighestRated("japanese")) // sushi
    obj.ChangeRating("ramen", 16)
    fmt.Println(obj.HighestRated("japanese")) // ramen

    sl := []int{1}
    fmt.Println(append(sl[0:], sl[1:]...))
    obj2 := Constructor(
        []string{"biihw"},
        []string{"okxsrcqn"},
        []int{13},
    )
    fmt.Println(obj2.HighestRated("okxsrcqn")) // biihw
    obj2.ChangeRating("biihw", 9)
    obj2.ChangeRating("biihw", 6)
    fmt.Println(obj2.HighestRated("okxsrcqn")) // biihw

    obj3 := Constructor(
        []string{"cpctxzh", "bryvgjqmj", "wedqhqrmyc", "ee", "lafzximxh", "lojzxfel", "flhs"},
        []string{"wbhdgqphq", "wbhdgqphq", "mxxajogm", "wbhdgqphq", "wbhdgqphq", "mxxajogm", "mxxajogm"},
        []int{15, 5, 7, 16, 16, 10, 13},
    )
    obj3.ChangeRating("lojzxfel", 1)
    fmt.Println(obj3.HighestRated("mxxajogm"))  // flhs
    fmt.Println(obj3.HighestRated("wbhdgqphq")) // ee
    fmt.Println(obj3.HighestRated("mxxajogm"))  // flhs

    // ["FoodRatings","highestRated","highestRated","changeRating","changeRating","highestRated","changeRating","highestRated","highestRated","highestRated","highestRated"]
    // [[[],[],[]],[""],[""],["",14],["",11],[""],["",8],[""],[""],[""],[""]]
    // [null,"","",null,null,"",null,"","","",""]
    obj4 := Constructor(
        []string{"pwdgjvphy", "tiwlr", "mqpdbl", "jjhmgnxt", "dmlymzufx"},
        []string{"dsyujtjljz", "eluxblkt", "dsyujtjljz", "dsyujtjljz", "eluxblkt"},
        []int{15, 10, 5, 16, 18},
    )
    fmt.Println(obj4.HighestRated("dsyujtjljz")) // jjhmgnxt
    fmt.Println(obj4.HighestRated("eluxblkt"))   // dmlymzufx
    obj4.ChangeRating("dmlymzufx", 14)
    obj4.ChangeRating("tiwlr", 11)
    fmt.Println(obj4.HighestRated("eluxblkt")) // dmlymzufx
    obj4.ChangeRating("tiwlr", 8)
    fmt.Println(obj4.HighestRated("eluxblkt"))   // dmlymzufx
    fmt.Println(obj4.HighestRated("dsyujtjljz")) // jjhmgnxt
    fmt.Println(obj4.HighestRated("dsyujtjljz")) // jjhmgnxt
    fmt.Println(obj4.HighestRated("eluxblkt"))   // dmlymzufx

    ul := []int{32, 56, 2, 5, 1, 5, 2, 545, 2, 53}
    InsertSort(ul)
    fmt.Println(ul)
    fmt.Println(append(ul[:3], ul[4:]...))
    fmt.Println("a" > "b")
    fmt.Println("aa" < "ab")

}
