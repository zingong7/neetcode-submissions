class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        ans=[]
        for num in nums:
            count[num]=1+count.get(num,0)
        sorted_keys=sorted(count,key=lambda c:count[c])
        return sorted_keys[-k:]



