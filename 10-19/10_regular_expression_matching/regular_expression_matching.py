# -*- coding: utf-8 -*-

"""
正则匹配
https://leetcode-cn.com/problems/regular-expression-matching/
"""


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 处理边界值
        if p == '':
            return s == ''

        if s == '':
            return self.isEndOfStar(p)

        if (len(p) > 1 and p[1] != '*') or len(p) == 1:
            if not self.match(s[0], p[0]):
                return False
            else:
                return self.isMatch(s[1:], p[1:])
        else:
            # 尝试将模式后移两位，相当于假设 x* 不存在
            if self.isMatch(s, p[2:]):
                return True

            # x* 可以 代表 x 一到多次
            while self.match(s[0], p[0]):
                # 后移1位字符串
                s = s[1:]

                # 同上
                if self.isMatch(s, p[2:]):
                    return True

                if s == '':
                    return self.isEndOfStar(p)
            return False

    def match(self, sc, pc):
        return sc == pc or pc == '.'

    def isEndOfStar(self, ps):
        while ps != '':
            if len(ps) == 1 or len(ps) > 1 and ps[1] != '*':
                return False
            ps = ps[2:]
        return True