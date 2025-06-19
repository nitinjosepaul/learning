class Solution:
    def pivotIndex(self, nums):
        #Return index for lists with single element
        if len(nums) == 1:
            return 0
        left_sum = 0
        right_sum = sum(nums)
        for index in range(len(nums)):
            right_sum -= nums[index]
            if index > 0:
                left_sum += nums[index-1]
            if left_sum == right_sum:
                return index
        return -1

s = Solution()
print(s.pivotIndex([1,7,3,6,5,6]))
print(s.pivotIndex([1,2,3]))
print(s.pivotIndex([]))