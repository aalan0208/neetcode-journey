from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for number in nums:
            if number not in hashset:
                hashset.add(number)
            else:
                return True
        return False
    