class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 采用一遍hash
        index_dict = {}
        nums_len = len(nums)
        for i in range(nums_len):
            end_num = target - nums[i]
            if index_dict.get(end_num) != None:
                return index_dict.get(end_num), i
            index_dict.update({nums[i]: i})