class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        i = 0
        maxlen = 0
        dic = {}
        for j in range(len(s)):
            c = s[j]
            if dic.__contains__(c):
                j_prev = dic[c]
                for k in range(i, j_prev):
                    del dic[s[k]]
                if j - i > maxlen:
                    maxlen = j - i
                i = j_prev + 1
            dic[c] = j
        return max(maxlen, j - i + 1)

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


def crt_sieving(mods, remainders):
    dic = {}
    for m, r in zip(mods, remainders):
        dic[m] = r              # 把模和余数放进字典里，key是模，value是余数
    mods.sort(reverse=True)     # 把模倒序
    adding = mods[0]            # 取最大的模，作为每次的加数
    num = dic[adding]           # 其余数作为初始数字
    for mod in mods[1:]:        # 依次取剩下的模
        re = dic[mod]           # 及其余数
        while num % mod != re:  # num对mod的余数满足条件为止
            num += adding       # 不满足则一直加上adding
        adding *= mod           # 满足后就讲adding乘上mod
    return num


if __name__ == "__main__":
    pass