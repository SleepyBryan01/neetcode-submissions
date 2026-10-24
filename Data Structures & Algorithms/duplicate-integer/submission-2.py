class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() 
        for num in nums: 
            if num in seen: 
                return True 
            seen.add(num)
    
        return False

        '''
        for i in nums: 
            if i not in process: 
                process.append(i)
            else: 
                return True
        return False 

'''

        