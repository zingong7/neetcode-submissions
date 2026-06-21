class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_track={}
        for i in range(len(nums)):
            second=target-nums[i]
            if second in nums_track:
                return sorted([nums_track[second],i])
            else:
                nums_track[nums[i]]=i
