package main

import "fmt"

func repeatedCharacter(s string) byte {
    repeatedMap := make(map[int32]bool, 26)
    for _, char := range s {
        if !repeatedMap[char] {
            repeatedMap[char] = true
        } else {
            return byte(char)
        }
    }
    return 0
}

func main() {
    fmt.Println(repeatedCharacter("abccbaacz")) // c
    fmt.Println(repeatedCharacter("abcdd"))     // d
}
