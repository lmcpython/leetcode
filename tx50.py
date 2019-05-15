def traverse_tree(node):
    left_depth = 0 if not node.left else traverse_tree(node.left)
    right_depth = 0 if not node.right else traverse_tree(node.right)
    return max(left_depth, right_depth) + 1

def get_expand_length(self, left, right, s):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

def generate_tree(nums):
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
        中心展开方法遍历所有字符串
        '''
        if len(s) < 2: return s
        start = end = 0
        for i in range(len(s)):
            len1 = get_expand_length(i, i, s)
            len2 = get_expand_length(i, i+1, s)
            maxlen = max(len1, len2)
            if maxlen > end - start:
                start = i - (maxlen-1) // 2
                end = i + maxlen // 2 + 1
        return s[start:end]

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
        return traverse_tree(root) if root else 0
        
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
        两次翻转，第一个分割成单词组后逆转单词之间的顺序（单词本身没变）
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
        if p == root or q == root: return root
        self.p = p
        self.q = q
        self.p_path = None
        self.q_path = None
        self.get_node_path(root, [-1])      # 遍历整棵树取得p和q的路径
        ancestor = root                     # 祖先节点先初始化为根节点
        depth = min(len(self.p_path), len(self.q_path))
        for i in range(1, depth):
            if self.p_path[i] == self.q_path[i]:        # 路径为0则往左走，1则往右走
                ancestor = ancestor.right if self.p_path[i] else ancestor.left
            else:  
                break       # 两者路径不相等说明从上一个节点已经分叉了，跳出循环返回上一个节点
        return ancestor

    def get_node_path(self, root, path):
        if root == self.p:
            self.p_path = path.copy()
        elif root == self.q:
            self.q_path = path.copy()
        if root.left:
            path.append(0)
            self.get_node_path(root.left, path)
        if root.right:
            path.append(1)
            self.get_node_path(root.right, path)
        path.pop()

if __name__ == "__main__":
    so = Solution()
    print(so)
    root = generate_tree([6,2,8,0,4,7,9,None,None,3,5])
    node = so.lowestCommonAncestor(root, root.left, root.left.right)
    print(node.val)