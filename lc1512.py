class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        count=0
        for i in d:
            a=d[i]
            if(a>1):
                count+=(a*(a-1))//2
        return count