# LeetCode 535 – Encode and Decode TinyURL

## Problem
[LeetCode #535 – Encode and Decode TinyURL](https://leetcode.com/problems/encode-and-decode-tinyurl/)

## Language
Python

## Approach
Since the problem does not enforce actual shortening,
we can directly return the input URL for both encode and decode.

This satisfies the requirement:
decode(encode(url)) == url

## Complexity
- Time: O(1)
- Space: O(1)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Feb 25, 2026 14:42  
> ⚙ Runtime: 37 ms  
> 🧠 Memory: 19.38 MB