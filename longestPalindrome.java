public class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.length() == 0){
            return null;
        } 
        String res = "";
        Integer max = 0;
        boolean[][] dp = new boolean[s.length()][s.length()];

        for (int j=0; j < s.length(); j++){
            for(int i=0; i<= j; i++){
                dp[i][j] = s.charAt(i) == s.charAt(j) && (j-i<=2 || dp[i+1][j-1]);
                if (dp[i][j]){
                    if (j - i + 1 > max){
                        max = j - i + 1;
                        res = s.substring(i,j+1);
                    }
                }
            }
        }

        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.print(s.longestPalindrome("babad"));
    }
}
