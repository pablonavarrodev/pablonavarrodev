from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        rg = len(nums)
        
        for i in range(rg):
            for j in range(i+1, rg):
                if nums[i] + nums[j] == target:
                    n1 = i
                    n2 = j

        sol = [n1,n2]

        return sol