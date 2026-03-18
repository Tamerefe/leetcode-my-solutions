/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function(s) {
    s = s.trim();
    let match = s.match(/^[+-]?\d+/);
    
    if (match < -2147483648) return -2147483648;
    if (match > 2147483647) return 2147483647;

    if (match) {
        return Number(match[0]);
    } else {
        return 0;
    }
};