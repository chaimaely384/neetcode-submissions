class Solution{

	public List<List<String>> groupAnagrams(String[] strs) {
		Map<String, List<String>> map = new HashMap<>();
		
		for( String s : strs) {
			int[] count = new int[26];
			for(int i =0; i<s.length(); i++){
				count[s.charAt(i)-'a']+=1;
			}
			String countstr= Arrays.toString(count);
			map.putIfAbsent(countstr, new ArrayList<>());
			map.get(countstr).add(s);
		}
		return new ArrayList<>(map.values());
	}
}
