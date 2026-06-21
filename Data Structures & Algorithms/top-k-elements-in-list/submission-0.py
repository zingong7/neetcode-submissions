class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        ans=[]
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        sorted_keys=sorted(count,key=lambda c:count[c],reverse=True)
        return sorted_keys[:k]



