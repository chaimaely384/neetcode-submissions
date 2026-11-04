class Solution {
    public String longestCommonPrefix(String[] strs) {

        if (strs == null || strs.length == 0) return "";

        String result = "";

        for(int i=0; i<strs[0].length(); i++){
            for(String str : strs){
                if(i>=str.length() || str.charAt(i)!=strs[0].charAt(i)){
                    return result;
                }
            }
            result+=strs[0].charAt(i);
        }
        return result;
        
    }
}