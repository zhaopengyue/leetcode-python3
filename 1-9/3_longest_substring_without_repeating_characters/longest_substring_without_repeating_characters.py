# -*- coding: utf-8 -*-


"""
无重复字符的最长子串
"""


def lengthOfLongestSubstring1(self, s):
    """
    无重复子串 -- 暴力解法
    :type s: str
    :rtype: int
    """
    # 记录临时子串字典，用于查询
    temp_dict = {}
    max_sub_len = 0
    # 逐个字母开始遍历
    for i in range(len(s)):
        sub_len = 1
        temp_dict.update({s[i]: 1})
        for j in range(i + 1, len(s)):
            if temp_dict.get(s[j]) != None:
                temp_dict.clear()
                break
            else:
                temp_dict.update({s[j]: 1})
                sub_len += 1
        if sub_len > max_sub_len:
            max_sub_len = sub_len
    return max_sub_len


def lengthOfLongestSubstring2(self, s):
    """
    滑动窗口解法
    :type s: str
    :rtype: int
    """
    # 滑动窗口
    window_dict = {}
    # 滑动窗口左右索引
    i = j = 0
    # 子串长度
    ans = 0
    # 字符串长度
    length = len(s)
    for j in range(len(s)):
        if s[j] in window_dict and i <= window_dict.get(s[j]):
            i = window_dict[s[j]] + 1
        # 如果没有处于滑动窗口中
        else:
            ans = max(ans, j - i + 1)
        window_dict[s[j]] = j
    return ans