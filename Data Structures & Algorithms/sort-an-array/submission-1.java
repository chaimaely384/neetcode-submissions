class Solution {
    public int[] sortArray(int[] nums) {

        return mergeSorted(nums, 0, nums.length-1);
    }

    private void merge(int[] arr, int L, int R){
        int M = L+(R-L)/2;

        int[] left = Arrays.copyOfRange(arr, L, M + 1);
        int[] right = Arrays.copyOfRange(arr, M + 1, R + 1);

        int i=L, j=0, k=0;

        while(j<left.length && k<right.length){
            if(left[j]<=right[k]){
                arr[i++]=left[j++];
            }
            else {
                arr[i++]=right[k++];
            }
        }
        while(j<left.length){
            arr[i++]=left[j++];
        }

        while(k<right.length){
            arr[i++]=right[k++];
        }

    }

    private int[] mergeSorted (int[] arr, int l, int r) {
        if (l==r) return arr;
        int m = l+(r-l)/2 ;
        mergeSorted(arr, l, m);
        mergeSorted(arr, m+1, r);
        merge(arr, l, r);
        return arr;
    }
}