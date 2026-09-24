class Solution(object):
    def maximumWealth(self, accounts):
        highest = 0
        for customer in accounts:
            total = 0
            for i in customer:
                total = total + i
                if total < highest:
                    False
                elif total > highest:
                    True
                    highest = total
        return highest