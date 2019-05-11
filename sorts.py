class Solution:
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda x:x[0])
        itv = intervals[0]
        results = []
        for i in intervals[1:]:
            if i[0] <= itv[1]:
                if i[1] > itv[1]:
                    itv[1] = i[1]
            else:
                results.append(itv)
                itv = i
        results.append(itv)
        return results

    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        result = []
        for i in range(len(intervals)):
            inter_i = intervals[i]
            if newInterval[1] < inter_i[0]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result
            if newInterval[1] <= inter_i[1]:
                if newInterval[0] < inter_i[0]:
                    inter_i[0] = newInterval[0]
                result.extend(intervals[i:])
                return result
            else:
                if newInterval[0] > inter_i[1]:
                    result.append(inter_i)
                elif inter_i[0] < newInterval[0]:
                    newInterval[0] =inter_i[0]
        result.append(newInterval)
        return result

    def sortColors(self, nums) -> None:
        l = 0
        r = len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 0:
                if i > l:
                    nums[i], nums[l] = nums[l], nums[i]
                    l += 1
                    i -= 1
            if nums[i] == 2:
                if i < r:
                    nums[i], nums[r] = nums[r], nums[i]
                    r -= 1
                    i -= 1
            i += 1

if __name__ == "__main__":
    nums = [2,0,1]
    Solution().sortColors(nums)
    print(nums)