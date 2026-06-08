class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += str(len(i)) + '#' + i 
        print(encoded)
        return(encoded)
    


    def decode(self, s: str) -> list[str]:
        decoded = []
        i=0
        while i < len(s):
            ss = ""
            j = i 

            while s[j] != '#':
                j+=1

            value = int(s[i:j]) 

            for k in range(j+1, j+1+value):
                ss+=s[k]
            
            decoded.append(ss)

            i= j+1+value
        return decoded

                

        
            
