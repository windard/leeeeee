/*
 * @lc app=leetcode id=974 lang=golang
 *
 * [974] Subarray Sums Divisible by K
 *
 * https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
 *
 * algorithms
 * Medium (47.31%)
 * Total Accepted:    56.2K
 * Total Submissions: 110.2K
 * Testcase Example:  '[4,5,0,-2,-3,1]\n5'
 *
 * Given an array A of integers, return the number of (contiguous, non-empty)
 * subarrays that have a sum divisible by K.
 * 
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: A = [4,5,0,-2,-3,1], K = 5
 * Output: 7
 * Explanation: There are 7 subarrays with a sum divisible by K = 5:
 * [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2,
 * -3]
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= A.length <= 30000
 * -10000 <= A[i] <= 10000
 * 2 <= K <= 10000
 * 
 * 
 */

// 我去，Golang 都超时了，TLE
func subarraysDivByK2(A []int, K int) int {
	var preSum []int
	preSum = append(preSum, 0)
	var total, count int
	for _, num := range A {
		total += num
		preSum = append(preSum, total)
	}

	for i := 0; i < len(preSum); i++ {
		for j := i + 1; j < len(preSum); j++ {
			if (preSum[j]-preSum[i])%K == 0 {
				count++
			}
		}
	}
	return count
}

func mod(a, b int) int {
	return (a%b + b) % b
}

func subarraysDivByK(A []int, K int) int {
	preSumDiv := map[int]int{0: 1}
	var total, count int
	for _, num := range A {
		total += num
		div := mod(total, K)
		count += preSumDiv[div]
		preSumDiv[div]++
	}
	return count
}