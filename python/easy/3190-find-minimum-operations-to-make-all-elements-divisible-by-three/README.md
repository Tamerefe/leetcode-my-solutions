# LeetCode 3190 – Find Minimum Operations to Make All Elements Divisible by Three

## Problem
[LeetCode #3190 – Find Minimum Operations to Make All Elements Divisible by Three](https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/)

## Language
Python

## Approach
Each element only needs to be checked modulo 3. 
If a number is not divisible by 3, it can always be made divisible using exactly one operation by either adding or subtracting 1.
Therefore, the answer is the count of elements whose value is not divisible by 3.

## Complexity
- Time: O(n)
- Space: O(1)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Dec 17, 2025 20:59  
> ⚙ Runtime: 0 ms  
> 🧠 Memory: 17.92 MB