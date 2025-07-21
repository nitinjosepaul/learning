class Solution:
    def runningSum(self, nums):
        sums = [nums[0]]
        for num in nums[1:]:
            sums.append(sums[-1] + num)
        return sums

s = Solution()
print(s.runningSum([1,2,3,4]))
print(s.runningSum([1]))
print(s.runningSum([1,1,1,1]))