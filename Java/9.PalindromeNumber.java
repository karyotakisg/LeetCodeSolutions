class Solution {
    public boolean isPalindrome(int x) {
        boolean flag = false;
        int temp, sum, r;
        temp = x;
        sum = 0;
        while(x>0){
            r = x % 10;
            sum = (sum*10) + r;
            x = x/10;
        }
        if (temp == sum){
            flag = true;
        }
        return flag;
    }
}