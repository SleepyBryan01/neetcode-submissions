class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        process = [] 
        for i in nums: 
            if i not in process: 
                process.append(i)

            else: 
                return True
        return False 



        