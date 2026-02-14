class Solution {
    public int[] recoverOrder(int[] order, int[] friends) {
        int[] nums = {};
        for (int i = 0; i < order.length; i++) {
            for (int j = 0; j < friends.length; j++) {
                if (order[i] == friends[j]) {
                    nums = Arrays.copyOf(nums, nums.length + 1);
                    nums[nums.length - 1] = order[i];
                }
            }
        }
        return nums;
    }
}