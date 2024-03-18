from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchrange(nums, target):
            pos = []
            for i in range(len(nums)):
                if nums[i] == target:
                    pos.append(i)

            if len(pos) == 0:
                return [-1, -1]
            
            pos1 = [min(pos), max(pos)]
            return pos1

        return searchrange(nums, target)