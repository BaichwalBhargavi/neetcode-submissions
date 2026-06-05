class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap ={}
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
        print(hashmap)
        sorted_lst = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        result = [sorted_lst[i][0] for i in range(0,k)]
        return result

    
        

        
                
            
            
