package main

import "fmt"

type ListNode struct {
    Val  int
    Next *ListNode
}

func spiralMatrix(m int, n int, head *ListNode) [][]int {
    //var ms []int
    //matrix := make([][]int, 0, m)
    //for i := 0; i < m; i++ {
    //    ms = make([]int, 0, n)
    //    for j := 0; j < n; j++ {
    //        ms = append(ms, -1)
    //    }
    //    matrix = append(matrix, ms)
    //}
    // 简化构造矩阵的办法
    matrix := make([][]int, m)
    for i := 0; i < m; i++ {
        matrix[i] = make([]int, n)
        for j := 0; j < n; j++ {
            matrix[i][j] = -1
        }
    }
    var i, j int
    var mm, mn int
    mm = -1
    mn = -1
    pos := 1
    // 1=to right
    // 2=to down
    // 3=to left
    // 4=to up
    for head != nil {
        matrix[i][j] = head.Val
        head = head.Next
        if pos == 1 {
            j++
            if j == n {
                mm++

                pos = 2
                j--
                i++
            }
        } else if pos == 2 {
            i++
            if i == m {
                n--

                pos = 3
                i--
                j--
            }
        } else if pos == 3 {
            j--
            if j == mn {
                m--

                pos = 4
                j++
                i--
            }
        } else {
            i--
            if i == mm {
                mn++

                pos = 1
                i++
                j++
            }
        }
    }
    return matrix
}

func genList1(ns []int) (node *ListNode) {
    var last, start *ListNode
    for _, n := range ns {
        node = &ListNode{}
        node.Val = n
        if last != nil {
            last.Next = node
        } else {
            start = node
        }
        last = node
    }
    return start
}

func genList(ns []int) (node *ListNode) {
    if len(ns) == 0 {
        return
    }
    node = &ListNode{}
    node.Val = ns[0]
    node.Next = genList(ns[1:])
    return
}

func main() {
    fmt.Println(spiralMatrix(3, 5, genList([]int{3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0})))
    fmt.Println(spiralMatrix(1, 4, genList([]int{0, 1, 2})))
}
