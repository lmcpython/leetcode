def traverseTree(node):
    '''
    遍历二叉树，返回最大深度
    '''
    left_depth = 0 if not node.left else traverseTree(node.left)
    right_depth = 0 if not node.right else traverseTree(node.right)
    return max(left_depth, right_depth) + 1

def getExpandLength(left, right, s):
    '''
    中心展开求回文字符串长度
    '''
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

def generateTree(nums):
    '''
    根据数据产生一个二叉树
    '''
    head = TreeNode(0)
    queue = [head]
    is_right = True
    for num in nums:
        node = queue.pop(0)
        if num != None:
            new_node = TreeNode(num)
            queue.append(new_node)
            queue.append(new_node)
        else:
            new_node = None
        if is_right:
            is_right = False
            node.right = new_node
        else:
            is_right = True
            node.left = new_node
    return head.right


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MinStack:
    '''
    最小栈，要求在常数时间内返回栈的最小值
    解法1：一个栈，但是不单纯的存储整数，而是存储一个元组，
    其第一个元素是要存储的整数，第二个元素是记录以来的最小元素
    '''
    # def __init__(self):
    #     self.data = [(None, float('inf'))]        

    # def push(self, x: int) -> None:
    #     self.data.append((x, min(x, self.data[-1][1])))     # 遇到更小的元素添加进来时，更新元组的第二项

    # def pop(self) -> None:
    #     if len(self.data) > 1: self.data.pop()

    # def top(self) -> int:
    #     return self.data[-1][0]

    # def getMin(self) -> int:
    #     return self.data[-1][1]
    '''
    解法2：两个栈，一个正常栈，一个存记录的最小值
    '''
    def __init__(self):
        self.data = []
        self.mins = []      

    def push(self, x: int) -> None:
        if self.data:
            self.mins.append(min(x, self.mins[-1]))
        else:
            self.mins.append(x)
        self.data.append(x)

    def pop(self) -> None:
        self.data.pop()
        self.mins.pop()

    def top(self) -> int:
        if self.data: return self.data[-1]

    def getMin(self) -> int:
        if self.mins: return self.mins[-1]


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
        解法1：中心展开方法遍历所有字符串
        '''
        # if len(s) < 2: return s
        # start = end = 0
        # for i in range(len(s)):
        #     len1 = getExpandLength(i, i, s)
        #     len2 = getExpandLength(i, i+1, s)
        #     maxlen = max(len1, len2)
        #     if maxlen > end - start:
        #         start = i - (maxlen-1) // 2
        #         end = i + maxlen // 2 + 1
        # return s[start:end]
        '''
        解法2：manacher算法
        '''
        if len(s) < 2: return s
        s = '#' + '#'.join(list(s)) + '#'
        p = [0 for x in range(len(s))]
        max_id = -1
        max_radio = -1
        c = -1
        mx = -1
        for i in range(len(s)):
            if i > mx:
                radio = getExpandLength(i, i, s) // 2
                p[i] = radio
                c = i
                mx = i + radio
                if radio > max_radio:
                    max_id, max_radio = i, radio
            else:
                j = 2*c - i
                if j - p[j] > 2 * c - mx:
                    p[i] = p[j]
                elif j - p[j] < 2 * c - mx:
                    p[i] = mx - i
                else:
                    radio = getExpandLength(i-p[j]-1, i+p[j]+1, s) // 2
                    p[i] = radio
                    if i + radio > mx:
                        c = i
                        mx = i + radio
                    if radio > max_radio:
                        max_id, max_radio = i, radio
        return s[max_id-max_radio:max_id+max_radio+1].replace('#', '')

    def deleteNode(self, node):
        '''
        删除某个链表中给定的（非末尾）节点，node是单向链表，且只给出要求被删除的节点而没有上游节点。
        node.next非空（因为非末尾），所以直接把next的所有内容复制过来就可以了
        '''
        nextnode = node.next
        node.val = nextnode.val
        node.next = nextnode.next
        pass

    def maxDepth(self, root) -> int:
        '''
        给定一个二叉树，找出其最大深度。二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
        '''
        return traverseTree(root) if root else 0
        
    def canWinNim(self, n: int) -> bool:
        '''
        你和你的朋友，两个人一起玩Nim游戏：桌子上有一堆石头，每次你们轮流拿掉1-3块石头。
        拿掉最后一块石头的人就是获胜者。你作为先手。你们是聪明人，每一步都是最优解。
        编写一个函数，来判断你是否可以在给定石头数量的情况下赢得游戏。
        分析：当还剩4个石头时，a无论是拿1个，2个还是3个，都会被接下来的b直接拿光
        所以，b需要保证在上一轮时石头只剩4个。然而当上一轮石头剩5-7个的时候，a都可以拿到只剩4个，另b陷入被动。
        那么只有当石头剩8个时，a无论拿几个，b都可以使剩余的石头为4个。
        所以，当石头为4个倍数时，作为后手的b胜利，其余情况则为a胜利
        '''
        return bool(n & 3)

    def reverseWords(self, s: str) -> str:
        '''
        给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
        输入: "Let's take LeetCode contest"
        输出: "s'teL ekat edoCteeL tsetnoc" 
        注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
        '''
        # if not s: return s
        # lis = list(s)
        # lis.append(' ')
        # start = 0
        # for i in range(len(lis)):
        #     if lis[i] == ' ':
        #         left = start
        #         right = i-1
        #         while left < right:
        #             lis[left], lis[right] = lis[right], lis[left]
        #             left += 1
        #             right -= 1
        #         start = i + 1
        # lis.pop()
        # return ''.join(lis)
        '''
        两次翻转，第一个分割成词组后逆转词组的顺序（单词本身没变）
        然后以空格连接再整个翻转
        '''
        return ' '.join(s.split(' ')[::-1])[::-1]

    def reverseList(self, head: ListNode) -> ListNode:
        '''
        反转一个单链表。示例:
        输入: 1->2->3->4->5->NULL
        输出: 5->4->3->2->1->NULL
        解法1：创建一个新空链表，遍历给定的链表挨个插入到新的链表
        '''
        # next_node = head
        # new_head = ListNode(0)
        # while next_node:
        #     temp_next = next_node.next
        #     next_node.next = new_head.next
        #     new_head.next = next_node
        #     next_node = temp_next
        # return new_head.next
        '''
        解法2：快慢指针递归翻转
        '''
        if not head or not head.next: return head   # 如果是空或只有1个节点，直接返回
        slow, fast = head, head.next                # slow初始化为节点1，fast为节点2
        while fast.next:                            # 当fast有下一个节点
            slow = slow.next                        # slow前进一步
            fast = fast.next
            if fast.next: fast = fast.next          # fast保证自身不为空的情况下前进2步
        right_head = slow.next                      # 原链表右半边的头节点
        self.reverseList(right_head)                # 翻转右半边链表
        slow.next = None                            # 从中间截断原链表
        self.reverseList(head)                      # 翻转左半边链表
        right_head.next = slow                      # rihgt_head现在为新链表的左边的尾结点
        return fast                                 # 返回新的头节点
    
    def singleNumber(self, nums) -> int:
        '''
        给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
        解法1：使用字典，遍历nums，没有这个key就添加，有就删除，根据数组的性质，最后只有一个key
        '''
        # dic = {}
        # for num in nums:
        #     if num in dic:
        #         dic.pop(num)
        #     else:
        #         dic[num] = 0
        # return dic.popitem()[0]
        '''
        解法2：由于 0^a = a，a^a = 0 ，
        而数组中除了一个数字是只出现一次的，其他数字均出现两次，则可以采用此思路来解答这个问题。 
        异或运算实际上就是不进位的加法，满足交换律
        '''
        res = 0
        for num in nums:
            res ^= num
        return res

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
        百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
        最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
        '''
        # if p == root or q == root: return root
        # self.p = p
        # self.q = q
        # self.p_path = None
        # self.q_path = None
        # self.getNodePath(root, [-1])      # 遍历整棵树取得p和q的路径
        # ancestor = root                     # 祖先节点先初始化为根节点
        # depth = min(len(self.p_path), len(self.q_path))
        # for i in range(1, depth):
        #     if self.p_path[i] == self.q_path[i]:        # 路径为0则往左走，1则往右走
        #         ancestor = ancestor.right if self.p_path[i] else ancestor.left
        #     else:  
        #         break       # 两者路径不相等说明从上一个节点已经分叉了，跳出循环返回上一个节点
        # return ancestor
        '''
        因为是有序的二叉树，根据其性质，左子树的全部点都比根节点小，右子树的全部点都比根节点大。
        所以当遇到两个点比根节点一大一小时必然分布在不同的子树上，所以根节点必然是其最近公共祖先。
        否则根据情况将根节点设为其左节点或右节点
        '''
        # while (root.val - p.val)*(root.val - q.val) > 0:
        #     root = root.left if (root.val - p.val) > 0 else root.right
        # (result_False, result_True)[judge_condition] 更简洁的判断写法
        while (root.val-p.val)*(root.val-q.val) > 0: root = (root.right, root.left)[q.val > root.val]
        return root

    def getNodePath(self, root, path):
        '''
        上一题的辅助函数，遍历整个树，实施更新当前路径，遇到是要找的节点就复制路径
        '''
        if root == self.p:
            self.p_path = path.copy()
        elif root == self.q:
            self.q_path = path.copy()
        if root.left:
            path.append(0)
            self.getNodePath(root.left, path)
        if root.right:
            path.append(1)
            self.getNodePath(root.right, path)
        path.pop()

    def majorityElement(self, nums: list) -> int:
        '''
        给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
        你可以假设数组是非空的，并且给定的数组总是存在众数。
        解法1：遍历
        '''
        # dic = {}
        # for num in nums:
        #     if num in dic:
        #         dic[num] += 1
        #     else:
        #         dic[num] = 1
        # half = len(nums) // 2
        # for k, v in dic.items():
        #     if v > half: return k
        '''
        设置一个current变量和cnt计数变量，current==num时cnt++否则cnt--，当cnt=0时，current改为num，cnt重置1。
        因为众数的数量比其他数的总和还多，所以即使相互抵消，最后剩下的也还是众数。
        '''
        current, cnt = 0, 0
        for num in nums:
            if cnt == 0:
                current = num
                cnt = 1
            elif current == num:
                cnt += 1
            else:
                cnt -= 1
        return current

    def isPalindrome(self, x: int) -> bool:
        '''
        判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
        示例 2:     输入: -121      输出: false
        解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
        示例 3:     输入: 10        输出: false
        解释: 从右向左读, 为 01 。因此它不是一个回文数。
        '''
        # return str(x) == str(x)[::-1]     # 转换字符串方法
        '''
        解法2：翻转后半部分与前半部分比较
        '''
        if x < 0 or (x >= 10 and x % 10 == 0): return False
        if x < 10: return True
        second_half = 0
        while x > second_half:
            second_half = second_half*10+(x%10)
            if second_half == x or second_half == (x//10): return True
            x = x // 10
        return False

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
        示例：
        输入：1->2->4, 1->3->4
        输出：1->1->2->3->4->4
        解法1：创建一个新的头结点，对比两个链表，挨个插入新链表
        '''
        # head = ListNode(0)
        # cur = head
        # while l1 and l2:
        #     if l1.val < l2.val:
        #         cur.next = l1
        #         l1 = l1.next
        #     else:
        #         cur.next = l2
        #         l2 = l2.next
        #     cur = cur.next
        # if l1:
        #     cur.next = l1       # l2为空，直接将l1剩下部分全部接上
        # elif l2:
        #     cur.next = l2       # l1为空，直接将l2剩下部分全部接上
        # return head.next
        '''
        解法2：与解法1类似，比较两个链表的头结点，以小的为主链表，遍历主链表，将副链表依次比较插入
        '''
        # if not l1: return l2
        # if not l2: return l1
        # if l2.val < l1.val: l2, l1 = l1, l2
        # head = l1
        # while l1.next:
        #     if not l2: return head      # 副链表以空，直接返回
        #     if l2.val <= l1.next.val:
        #         temp = l1.next
        #         l1.next, l2 = l2, l2.next
        #         l1.next.next = temp
        #     else:
        #         l1 = l1.next
        # l1.next = l2                    # 把副链表剩余部分接在主链表尾部
        # return head
        '''
        解法3：递归法
        '''
        if not l1: return l2
        if not l2: return l1
        if l1.val > l2.val: l1, l2 = l2, l1         # 交换l1, l2 简化代码
        l1.next = self.mergeTwoLists(l1.next, l2)   # 每次将l1链表的当前节点截断，剩下的部分和l2留给后续递归
        return l1                                   # l1的头结点接上排好序的链表返回

    def maxProfit(self, prices: list) -> int:
        '''
        给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。如果你最多只允许完成一笔交易（即买入和卖出一支股票），
        设计一个算法来计算你所能获取的最大利润。注意你不能在买入股票前卖出股票。
        解法1：暴力搜索
        '''
        # profit = 0
        # for i in range(len(prices) - 1):
        #     if prices[i] >= prices[i+1]: continue   # 如果是递减部分直接跳过，否则TLE
        #     for p in prices[i+1:]:
        #         if p - prices[i] > profit: profit = p - prices[i]
        # return profit
        '''
        解法2：一次遍历，实时更新找到的最小价格，然后将当前价格的差价与最大利润比较，大于就更新
        '''
        max_profit = 0
        min_price = 2**30 -1 + 2**30
        for p in prices:
            if p < min_price: min_price = p
            if p - min_price > max_profit: max_profit = p - min_price
        return max_profit

    def maxProfitII(self, prices: list) -> int:
        '''
        给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
        设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
        注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
        解法1：常规思路，遍历数组，若明天涨就（继续）持有，跌就抛出（如果买了）
        '''
        # if len(prices) < 2: return 0
        # buy, profit = -1, 0
        # for i in range(len(prices)-1):
        #     if prices[i+1] - prices[i] < 0:
        #         if buy != -1:
        #             profit += prices[i] - buy
        #             buy = -1
        #     else:
        #         if buy == -1:
        #             buy = prices[i]
        # if buy != -1:
        #     profit += prices[-1] - buy
        # return profit
        '''
        解法2：应为同一天可以多次交易，所以肯定可以利润最大化，直接遍历数组，如果比前一天高，则进行累加
        '''
        return sum(b - a for a, b in zip(prices, prices[1:]) if a < b)

    def isPowerOfTwo(self, n: int) -> bool:
        '''
        给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
        解法1：按位循环
        '''
        # if n <= 0: return False  # 小于等于0直接False
        # while n > 1:
        #     if n & 1: return False
        #     n = n >> 1
        # return True
        '''
        解法2：在保证n大于0的情况下，n若是2的幂次方，则只有1位为1，与其相差1的数进行按位与运算必为0
        '''
        return n > 0 and n & n - 1 == 0

    def climbStairs(self, n: int) -> int:
        '''
        假设你正在爬楼梯。需要 n 阶你才能到达楼顶，给定 n 是一个正整数。
        每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
        解法1：斐波那契数列，通过归纳可确定结果是一个斐波那契数列数列
        '''
        if n < 3: return n
        a, b = 1, 2
        for i in range(3, n+1):
            a, b = b, a+b
        return b

    def removeDuplicates(self, nums: list) -> int:
        '''
        给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
        不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
        解法：双指针，一个指针遍历数组，另一个记录非重复数字数量
        '''
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                j += 1
                #nums[j] = nums[i]
        return j + 1 if len(nums) else 0

    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
        说明:
        初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
        你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
        解法：对两个列表倒序遍历，谁大就放到nums1队尾中
        """
        a = m - 1
        b = n - 1
        for i in range(m+n-1, -1, -1):
            if a >= 0 and b >= 0:
                if nums1[a] > nums2[b]:
                    nums1[i] = nums1[a]
                    a -= 1
                else:
                    nums1[i] = nums2[b]
                    b -= 1
            elif a < 0:
                nums1[:i+1] = nums2[:b+1]
                break
            
        

if __name__ == "__main__":
    so = Solution()
    res = so.merge([4,5,6,0,0,0], 3, [1,2,3], 3)
    print(res)