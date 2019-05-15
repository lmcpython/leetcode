class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        '''
        给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
        请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
        你可以假设 nums1 和 nums2 不会同时为空。
        '''
        m = len(nums1)
        n = len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError

        imax = m
        imin = 0
        half = (m + n + 1) // 2
        while imin <= imax:    
            i = (imax + imin) // 2
            j = half - i            
            if i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0: max_left = nums2[j-1]
                elif j == 0: max_left = nums1[i-1]
                else: max_left = max(nums1[i-1], nums2[j-1])
                if (m+n) % 2 == 1:
                    return max_left             # 当m+n为奇数时，左边部分包含中位数
                
                if i == m: max_right = nums2[j]
                elif j == n: max_right = nums1[i]
                else: max_right = min(nums1[i], nums2[j])
                
                return (max_left + max_right) / 2

    def longestPalindrome(self, s: str) -> str:
        '''
        给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
        '''
        if len(s) < 2: return s
        start = end = 0
        for i in range(len(s)):
            len1 = self.get_expand_length(i, i, s)
            len2 = self.get_expand_length(i, i+1, s)
            maxlen = max(len1, len2)
            if maxlen > end - start:
                start = i - (maxlen-1) // 2
                end = i + maxlen // 2 + 1
        return s[start:end]

    def get_expand_length(self, left, right, s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

if __name__ == "__main__":
    so = Solution()
    print(so.longestPalindrome('sfwegabcbahsajkwiv'))