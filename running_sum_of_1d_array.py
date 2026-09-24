class Solution(object):
    def runningSum(self, nums):
        total = 0
        ans = []
        for i in nums:
            total = total + i
            ans.append(total)
        return ans