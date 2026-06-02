class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_dict ={}
        if len(s) != len(t):
            return False
         
        count = [0] * 26
        for i in s:
            count[ord(i) - ord('a')] +=1
        for i in t:
            count[ord(i) - ord('a')] -=1

        return (all(val ==0 for val in count))
