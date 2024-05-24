class Solution2:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        nums.extend(nums)
        return nums
        