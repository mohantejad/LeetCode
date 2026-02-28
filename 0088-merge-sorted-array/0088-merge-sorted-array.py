class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Bruteforce - O(n + (m+n)log(m+n))
        nums1[m:] = nums2
        nums1.sort()