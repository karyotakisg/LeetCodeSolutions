class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1[len(nums1)-len(nums2) : len(nums1)]=nums2
        
        for i in range(1,len(nums1)):
            j=i
            while j>0 and (nums1[j-1]-nums1[j]>0):
                 nums1[j], nums1[j-1] = nums1[j-1], nums1[j]
                 j=j-1
        return nums1