class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixproduct=[0]*len(nums)
        prefixproduct[0]=1
        suffixproduct=[0]*len(nums)
        suffixproduct[-1]=1
        for i in range(1,len(nums)):
            prefixproduct[i]=prefixproduct[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            suffixproduct[i]=suffixproduct[i+1]*nums[i+1]
        for i in range(len(prefixproduct)):
            prefixproduct[i]=prefixproduct[i]*suffixproduct[i]
        return prefixproduct