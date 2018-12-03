# -*- coding: utf-8 -*-


"""
最长回文子串动态
"""

import numpy as np


def longest_palindrome_1(string):
    """
    暴力破解
    :param string:
    :return:
    """
    ans = 1
    max_i = 0
    max_j = 1
    l = len(string)
    for i in range(l):
        # 列表切片不包含最右部分
        # 故对于bb 来说, a[0:2]才为bb
        for j in range(i + 1, l + 1):
            child_s = string[i:j]
            # 验证是否为回文子串
            if child_s[::-1] == child_s:
                if len(child_s) > ans:
                    max_i = i
                    max_j = j
                    ans = len(child_s)
    return string[max_i: max_j]


def longest_palindrome_2(string):
    """
    动态规划法
    :param string:
    :return:
    """
    length = len(string)
    # 最长回文子串
    ans = 1
    start = 0
    # 状态转移方程数组
    dp = np.zeros((length, length))
    # 计算边界值状态方程
    for i in range(length):
        dp[i][i] = 1
        if i + 1 < length and string[i] == string[i+1]:
            dp[i][i+1] = 1
            ans = 2
            start = i
    # 计算长度大于3的状态方程
    for l in range(3, length+1):
        i = 0
        # i 为左端点, j为右端点
        while i + l - 1 < length:
            j = i + l - 1
            if string[i] == string[j] and dp[i+1][j-1] == 1:
                dp[i][j] = 1
                start = i
                ans = l
            i += 1
    return string[start: start + ans]


def longest_palindrome_3(string):
    """
    动态规划法 -- 减小空间复杂度
    :param string:
    :return:
    """
    """
        动态规划法
        :param string:
        :return:
        """
    length = len(string)
    # 最长回文子串
    ans = 1
    start = 0
    # 状态转移方程数组 -- 使用以为数组表示
    dp = [0] * (length * (length + 1) // 2)
    # 计算边界值状态方程
    for i in range(length):
        dp[_turn(i, i, length)] = 1
        if i + 1 < length and string[i] == string[i + 1]:
            dp[_turn(i, i+1, length)] = 1
            ans = 2
            start = i
    # 计算长度大于3的状态方程
    for l in range(3, length + 1):
        i = 0
        # i 为左端点, j为右端点
        while i + l - 1 < length:
            j = i + l - 1
            if string[i] == string[j] and dp[_turn(i+1, j-1, length)] == 1:
                dp[_turn(i, j, length)] = 1
                start = i
                ans = l
            i += 1
    return string[start: start + ans]


def _turn(i, j, l):
    """
    三角矩阵的压缩
    :param i:
    :param j:
    :return:
    """
    return i * (2 * l - i + 1) // 2 + j - i

if __name__ == '__main__':
    s = 'ccc'
    # print(longest_palindrome_1(s))
    print(longest_palindrome_3(s))