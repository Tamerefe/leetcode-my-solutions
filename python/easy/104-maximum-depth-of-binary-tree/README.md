# LeetCode 104 – Maximum Depth of Binary Tree

## Problem
[LeetCode #104 – Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

## Language
Python

## Approach
Use recursion (DFS).

For each node:
- Recursively compute the depth of the left subtree
- Recursively compute the depth of the right subtree
- Return `1 + max(leftDepth, rightDepth)`

If the node is `None`, return `0`.

## Complexity
- Time: O(n)
- Space: O(h)  (h = tree height)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Mar 15, 2026 15:22  
> ⚙ Runtime: 0 ms  
> 🧠 Memory: 20.39 MB