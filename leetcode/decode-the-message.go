package main

import "fmt"

func decodeMessage2(key string, message string) string {
    decodeMap := make(map[int32]int32, 26)
    startA := 'a'
    var startI int32
    for _, c := range key {
        if c == ' ' {
            continue
        }
        if _, ok := decodeMap[c]; !ok {
            //fmt.Printf("%s:%s\n", string(c), string(startA+startI))
            decodeMap[c] = startA + startI
            startI++
        }
    }
    //fmt.Printf("decode:%d map:%+v\n", len(decodeMap), decodeMap)
    messages := make([]int32, 0, len(message))
    for _, m := range message {
        if m == ' ' {
            messages = append(messages, m)
        } else {
            messages = append(messages, decodeMap[m])
        }
    }
    return string(messages)
}

func decodeMessage(key string, message string) string {
    // little improve
    decodeMap := make(map[int32]int32, 27)
    decodeMap[' '] = ' '
    startA := 'a'
    for _, c := range key {
        if _, ok := decodeMap[c]; !ok {
            decodeMap[c] = startA
            startA++
        }
    }

    messages := make([]int32, 0, len(message))
    for _, m := range message {
        messages = append(messages, decodeMap[m])
    }
    return string(messages)
}

func main() {
    // "this is a secret"
    fmt.Println(decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))
    // "the five boxing wizards jump quickly"
    fmt.Println(decodeMessage("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"))
}
