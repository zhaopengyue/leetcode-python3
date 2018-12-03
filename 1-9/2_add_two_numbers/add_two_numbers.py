# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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