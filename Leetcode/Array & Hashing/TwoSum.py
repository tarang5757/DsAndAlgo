class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[j] + nums[i] == target):
                    return [i, j]


Tester = Solution()
print(Tester.twoSum([1, 2, 6, 4,2, 23, 5], 24))