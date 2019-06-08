## leeeeee

LeetCode Folder

### algorithms

`pip install algorithms`

python 算法库

### 算法复杂度

算法复杂度包括时间复杂度和空间复杂度。

时间复杂度 T(n) 指算法在运行过程中需要的时间消耗和参数系数n的关系

空间复杂度 S(n) 指算法在运行过程中需要的内存占用和参数系数n的关系

算法复杂度一般用大O表示法表示，即 O(n)

一般常见的算法复杂度
1. T(n) = O(n)
2. T(n) = O(logn)
3. T(n) = O(n^2)
4. T(n) = O(1)

算法复杂度比较

O(1) < O(logn) < O(n) < O(n^2)

> O(logn) 的一个常见场景,长度为n的直线，日取其半，终长为1，需要几天

### 算法思想

- 迭代 iteration
- 遍历 traversal
- 递归 recursion
- 分治
- 动态规划 Dynamic Programming
- 二分
- 贪心 Greedy Algorithm

### LeetCode 注意

1. 同样的参数递归可以缓存加速
2. 不要用全部变量，会有影响
3. 使用 LeetCode 定义的结构体类会比用自己定义的慢
4. LeetCode 的 solution 比 Discuss 有更好的解法
5. list 是有序的，set 是无序的
6. list 的 pop 和 remove 都是非常耗时的
7. xrange 比 range 快，在 python2 中

### 排列组合

- 所有排序 m**n                                  
    > `9*9*9*9 = 6561`
- 全排列 A(n/m) = m!/(m-n)!             
    > A(4/9) = `9*8*7*6 = 3024`
- 全组合 C(n/m) = m!/(m-n)!n!           
    > C(4/9) = `9*8*7*6/4*3*2*1 = 126`
- 可重复的全组合 H(n/m) = C(n/m+n-1) = (m+n-1)!/n!(m-1)!
    > H(4/9) = `12!/4!8! = 12*11*10*9/4*3*2*1 = 495`

### divmod

divisor = (m + n) / 10
left    = (m + n) % 10

divisor, left = divmod(m+n, 10)
