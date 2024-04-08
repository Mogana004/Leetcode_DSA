class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        peak_element = 0 
        for i in range( 1 , len(arr)):
            if (arr[i] > arr[i-1]) and (arr[i] > arr[i+1]) :
                return i 
        
