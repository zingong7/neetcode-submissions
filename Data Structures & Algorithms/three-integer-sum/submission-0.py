class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        ans=[]
        for i in range(len(nums)):
            l=i+1
            e=len(nums)-1
            while(l<e):
                currsum=nums[i]+nums[l]+nums[e]
                if currsum==0:
                    if [nums[i],nums[l],nums[e]] not in ans:
                        ans.append([nums[i],nums[l],nums[e]])
                if currsum<0:
                    l+=1
                else:
                    e-=1
        return ans
