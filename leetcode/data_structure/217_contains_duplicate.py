class Solution:
    def containsDuplicate(self, nums):
        for item in nums:
            if nums.count(item) > 1:
                return True
        else:
            return False

    def containsDuplicate2(self, nums):
        item_count = {}
        for item in nums:
            try:
                item_count[item] += 1
                return True
            except KeyError:
                item_count[item] = 1
        else:
            return False


s = Solution()
print(s.containsDuplicate2([1,2,3,1]))
print(s.containsDuplicate2([1,2,3,4]))
print(s.containsDuplicate2([1,1,1,3,3,4,3,2,4,2]))