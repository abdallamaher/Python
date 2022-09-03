#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = dict()
        for idx, item in enumerate(nums):
            diff = target - item
            
            if  diff in mp:
                return [mp[diff], idx]
            mp[item] = idx        
# @lc code=end

