class Solution {
    public int maxDistinct(String s) {
        int num = 0;
        for (char mycharacter = 'a'; mycharacter <= 'z'; mycharacter++) {
            if (s.contains(String.valueOf(mycharacter))) {
                num += 1;
            }
        }
        return num;
    }
}