class NodeList(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    pass

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

    def insertionSortList(self, head):
        '''
        插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
        每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
        重复直到所有输入数据插入完为止。
        '''
        n = head
        a = []
        while n:
            a.append(n.val)
            n = n.next
        a.sort()
        i = 0
        n = head
        while n:
            n.val = a[i]
            i += 1
            n = n.next
        return head

    def sortList(self, head):
        '''
        在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
        '''
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = self.sortList(slow.next)
        slow.next = None
        left = self.sortList(head)
        return self.merge_list(left, right)

    def merge_list(self, left, right):
        head = NodeList(0)
        x = head
        while left and right:
            if left.val < right.val:
                x.next = left
                left = left.next
            else:
                x.next = right
                right = right.next
            x = x.next
        if left:
            x.next = left
        if right:
            x.next = right
        return head.next

if __name__ == "__main__":
    pass