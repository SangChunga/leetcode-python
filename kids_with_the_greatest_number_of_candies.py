class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        ans = []
        highest = max(candies)
        for i in candies:
            total = i + extraCandies
            if total < highest:
                ans.append(False)
            elif total >= highest:
                ans.append(True)
        return ans
        