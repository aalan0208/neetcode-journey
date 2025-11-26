from typing import List

class Solution:

    """
    when encoded, string would look like ex: 5#hello2#hi
    where the numnber is the length of string and # is the delimeter
    """
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 # i isa pointer, this marks the the beginning of the pointer
        while i < len(s):
            # j is the second pointer, j moves until it finds #
            j = i
            while s[j] != "#":
                j+=1
            #once found this  length is the lenght of the string. Ex in 5#hello. i = 0, j = 1 this means length is 5
            length = int(s[i:j])
            # appends after the delimeter, 
            res.append(s[j+1:j+1+length])
            # next i pointer is a the next number of the word
            i = j + 1 + length
        return res