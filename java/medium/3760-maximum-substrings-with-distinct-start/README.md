# LeetCode 3760 – Maximum Substrings With Distinct Start

## Problem
[LeetCode #3760 – Maximum Substrings With Distinct Start](https://leetcode.com/problems/maximum-substrings-with-distinct-start/)

## Language
Java

## Approach
Iterate over letters `a` to `z` and count how many of them appear at least once in the string.
This gives the number of distinct starting characters.

## Complexity
- Time: O(26 * n)
- Space: O(1)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Feb 10, 2026 01:15  
> ⚙ Runtime: 20 ms  
> 🧠 Memory: 47.73 MB