from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # create dictionary called count

        for n in nums:
            # count.get(n, 0) returns the current count, or 0 if n is not in the dictionary
            count[n] = 1 + count.get(n, 0)
            
        """
        creates lists of empty lists. If nums = [1,1,2], then len(nums) = 3. 
        This creates:
        freq = [ [], [], [], [] ]
                 0   1   2   3   ← indexes
        """
        freq = [[] for i in range(len(nums) + 1)]  
        
        """
        Put the number in the bucket 
        ex: freq[3].append(1) --> this means 1 appears 3 times
        ex: freq[2].append(2) --> this means 2 appears 2 times
        ex: freq[1].append(3) --> this means 3 appears 1 times
        
        """
        for n,c in count.items():
            freq[c].append(n)

        # store the result
        res = []
        # loops backward
        for i in range(len(freq)-1,0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res