class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n) :
            nums[i] += (nums[nums[i]]%n) * n
            print(nums)
        for i in range(n):
            nums[i] //= n
            print(nums)
        return nums