class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char={}
        for i in s:
            if i in char:
                char[i] +=1
            else:
                char[i] =1
        for i in t:
            if i in char:
                char[i] -=1
            else:
                char[i] =1
        print(char)
        for i in char.values():
            if i!=0:
                return False
        return True

        
