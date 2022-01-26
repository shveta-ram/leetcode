public int[] runningSum(int[] nums) {
        int x = 0; //variable that gets iterated
        for (int i = 0; i < nums.length; i++){
            x += nums[i];
            nums[i] = x;
        }
    return nums;
    }
}
