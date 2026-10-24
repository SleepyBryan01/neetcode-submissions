class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        aMap = {} 
        for i, n in enumerate(nums): 
            diff = target - n 
            if diff in aMap: 
                return [aMap[diff], i]
            
            else: 
                aMap[n] = i 
        return 

