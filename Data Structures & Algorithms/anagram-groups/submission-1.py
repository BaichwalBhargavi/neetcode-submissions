class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        
        for word in strs:
            count = [0]*26
            for i in word:
                count[ord(i) - ord('a')] +=1

            hashmap[tuple(count)].append(word)
        return [value for value in hashmap.values()]

        
            
        


      
            

    
    
        
     
