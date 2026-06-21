class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans=[]
        nums=sorted(nums)
        maxcount=1
        count=1
        if not nums:
            return 0
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                if nums[i]+1==nums[i+1]:
                    count+=1
                else:
                    count=1
            maxcount=max(maxcount,count)
        return maxcount