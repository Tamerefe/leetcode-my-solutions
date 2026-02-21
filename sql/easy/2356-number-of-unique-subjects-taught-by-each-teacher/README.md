# LeetCode 2356 – Number of Unique Subjects Taught by Each Teacher

## Problem
[LeetCode #2356 – Number of Unique Subjects Taught by Each Teacher](https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/)

## Language
MySQL

## Approach
Group the records by `teacher_id` and use  
`COUNT(DISTINCT subject_id)` to count unique subjects taught by each teacher.

## Complexity
- Time: O(n)
- Space: O(1)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Feb 21, 2026 13:31  
> ⚙ Runtime: 488 ms