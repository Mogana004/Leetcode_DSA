class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length 
        nums[:] = nums[-k:] + nums[:-k]  # Modify the original nums list in-place
