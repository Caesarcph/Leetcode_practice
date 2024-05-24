class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:

        return 0+operations.count('X++')+operations.count('++X')-operations.count('X--')-operations.count('--X')
        