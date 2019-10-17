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

- 暴力 Brute Force (容易 Time Limit)
- 迭代 iteration
- 遍历 traversal
- 递归 recursion
- 分治 Divide-and-Conquer 
- 动态规划 Dynamic Programming (注意 Memory Error)
- 二分查找 Binary-Search (数组必须有序)
- 贪心 Greedy Algorithm
- 回溯 backtrack

### LeetCode 注意

1. 同样的参数递归可以缓存加速
2. 不要用全部变量，会有影响
3. 使用 LeetCode 定义的结构体类会比用自己定义的慢
4. LeetCode 的 solution 比 Discuss 有更好的解法
5. list 是有序的，set 是无序的
6. list 的 pop 和 remove 都是非常耗时的
7. xrange 比 range 快，在 python2 中
8. HashMap is good, 即 dict，查找元素的时间复杂度可以认为是 O(1)

### 排列组合

- 所有排序 m**n                                  
    > `9*9*9*9 = 6561`
- 全排列 permutations A(n/m) = m!/(m-n)!             
    > A(4/9) = `9*8*7*6 = 3024`
- 全组合 combinations C(n/m) = m!/(m-n)!n!           
    > C(4/9) = `9*8*7*6/4*3*2*1 = 126`
- 可重复的全组合 combinations_with_replacement H(n/m) = C(n/m+n-1) = (m+n-1)!/n!(m-1)!
    > H(4/9) = `12!/4!8! = 12*11*10*9/4*3*2*1 = 495`

### divmod

divisor = (m + n) / 10
left    = (m + n) % 10

divisor, left = divmod(m+n, 10)

### 神奇的操作

#### 乘法不用乘法

题目描述：求1+2+3+…+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

```
def f(n):
    if n == 0:
        return n
    else:
        return f(n-1) + n

```

但还是用到了 if else，如果这都不用，只能换其他语言了。

```
	public Integer f(Integer n){
		Integer t = n;
		Boolean b = n != 0 && (t += f(n-1)) != 0;
		return t;
	}
```

#### 加法不用加法

题目描述：写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

已知

```
a + b = a ^ b + (a & b) << 1。
```

59 = 111011
33 = 100001

92 = 59 + 33 = 011010 + 1000010 = 26 + 66 = 92

释义：
a ^ b 表示 a + b , 不计算进位的结果
a & b 表示 a + b , 需要进位的结果，然后左移进位

```
def f(a, b):
    return a ^ b + ((a & b) << 1)

```

### 乘法不用循环

题目描述：实现两个整数的相乘，不能使用乘法运算符和循环

不用循环，那就递归

```
def mul(a, b):
    if b == 0:
        return 0
    return a + mul(a, b - 1)


def multi(a, b):
    tem = mul(a, abs(b))
    return -tem if b < 0 else tem

```

但是这样不能计算小数的乘法

或者用除法  

```
def mul(a, b):
    if b != 0:
        return a / (1.0 / b)
    return 0
```

### BST

二叉搜索树 Binary Search Tree 

特性
1. 当前节点大于等于左子节点及其所有节点
2. 当前节点小于右子节点及其所有节点
3. 中序遍历结果为有序数组

#### 遍历

- preorder traversal  先序遍历，中左右
- inorder traversal   中序遍历，左中右
- postorder traversal 后序遍历，左右中

### 排列组合的各种骚操作

1. 递归
2. 迭代
3. 回溯
4. 剪枝
5. DFS
6. BFS

### longest 与 maximum 系列

套路，全都是套路

- substring: 连续子字符串
- subsequence: 不用连续的子序列
- subarray: 连续的子数组

- longest palindromic substring 最长回文字符串
- longest common subsequence 最长公共序列
- longest increasing subsequence 最长增长序列
- maximum subarray 最大数组
