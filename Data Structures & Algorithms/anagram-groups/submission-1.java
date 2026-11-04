class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result = new ArrayList<>();

        Map<String, List<String>> map = new HashMap<>();
        int category;

        for(int i=0; i<strs.length; i++){
            char[] chars = strs[i].toCharArray();
            Arrays.sort(chars);
            String s= new String(chars);
            map.putIfAbsent(s, new ArrayList<>());
            map.get(s).add(strs[i]);
        }

        for (String key : map.keySet()){
            result.add(map.get(key));
        }

        return result;


    }
}
