class Solution:
    def maxArea(self, height: list) -> int:
        '''
        给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
        在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
        找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
        解法1：暴力搜索，但是会超出时间限制
        maxarea = 0
        for i in range(0, len(height)-1):
            for j in range(i+1, len(height)):
                maxarea = max(maxarea, (j-i)*min(height[i], height[j]))
        return maxarea
        '''
        # 解法2，双指针：
        maxarea, left, right = 0, 0, len(height)-1
        while left < right:
            maxarea = max(maxarea, (right-left)*min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxarea
    
    def threeSum(self, nums: list) -> list:
        '''
        求三数之和，取数组中取三个数，和为0，返回所有这样的三元组，不能重复
        '''
        res = []
        cnt = len(nums)
        if cnt < 3: return res      # 数组个数小于3直接返回空
        nums.sort()                 # 先排序
        for left in range(0, cnt-2):                        # 从数组中最小的数遍历至导数第三个
            if left > 0 and nums[left] == nums[left-1]:     # 如果left和前一个相等跳过，因为完全一样
                continue
            if nums[left] > 0: break                        # left>0返回，因为三个大于零的数和必然大于0
            mid = left + 1
            right = cnt - 1
            while mid < right:
                s = nums[left] + nums[mid] + nums[right]
                if s == 0:
                    res.append((nums[left], nums[mid], nums[right]))
                    while mid < right and nums[mid] == nums[mid+1]:
                        mid += 1                            # 跳过相同的数字，避免重复
                    while right > mid and nums[right] == nums[right-1]: 
                        right -= 1                              
                    mid += 1
                    right -= 1
                elif s < 0:
                    mid += 1
                else:
                    right -= 1
                    if nums[right] < 0: break               # right<0跳出，三个小于零的数和必然小于零
        return res

if __name__ == "__main__":
    so = Solution()