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
            ivt = intervals[i]
            if newInterval[1] < ivt[0]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result
            
            if newInterval[1] <= ivt[1]:
                if newInterval[0] < ivt[0]:
                    ivt[0] = newInterval[0]
                result.extend(intervals[i:])
                return result
            else:
                if newInterval[0] <= ivt[0]:
                    continue
                if newInterval[0] <= ivt[1]:
                    newInterval[0] = ivt[0]
                else:
                    result.append(ivt)
        return newInterval.append(newInterval)