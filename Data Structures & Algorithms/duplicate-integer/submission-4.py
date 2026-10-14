class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() #hash table
        for val in nums:
            if val in seen:
                return True
            seen.add(val)
        return False
