class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n-1):
                for j in range(i+1,n):
                    p=(nums[i]+nums[j])
                    if p==target:
                        return[i,j]
        return[]