### 题目描述
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
```
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
```

### 基本思路
由题目可知，此题的核心是解决进位问题，因此，我们可以设置一个字典，分别记录当前位数的状态，1表示进位，0表示不进位。此时，该位的数字sum就变为了$ (a + b + (进位))%10 $，下一位的进位就变成了sum // 10。  

加数和被加数的位数可能不一样，我们可以先处理其公共位数，然后依次处理较长位数的值。

### 实现代码
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 进位标识dict
        from collections import defaultdict
        flag = defaultdict(int)
        # 初始化头
        head_node = ListNode(0)
        # 指针P
        p = head_node
        # 处理序号标记
        deal_id = 0
        while l1 != None and l2 != None:
            sum = l1.val + l2.val + flag[deal_id-1]
            node = ListNode(sum % 10)
            flag.update({deal_id: sum // 10})
            deal_id += 1
            p.next = node
            p = node
            l1 = l1.next
            l2 = l2.next
        print(deal_id)
        # l1位数超出
        while l1 != None:
            sum = l1.val + flag[deal_id-1]
            node = ListNode(sum % 10)
            flag.update({deal_id: sum // 10})
            deal_id += 1
            p.next = node
            p = node
            l1 = l1.next
        # l2位数超出
        while l2 != None:
            sum = l2.val + flag[deal_id-1]
            node = ListNode(sum % 10)
            flag.update({deal_id: sum // 10})
            deal_id += 1
            p.next = node
            p = node
            l2 = l2.next
        # 检测最开头是否有进位
        if flag[deal_id-1] != 0:
            node = ListNode(1)
            p.next = node
        return head_node.next
```