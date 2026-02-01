/**
 * LeetCode 2723 - Add Two Promises
 * Language: JavaScript
 *
 * Time Complexity: O(1)
 * Space Complexity: O(1)
 */

var addTwoPromises = async function (promise1, promise2) {
    return await promise1 + await promise2
};
