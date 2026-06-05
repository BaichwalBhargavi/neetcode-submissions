class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # for frequency and value mapping
        hashmap={}
        # empty list of lists for buckets
        freq = [ [] for i in range(len(nums)+1) ]

        # get frequency of each element and save in hashmap
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i,0)
        
        # adding the values in the freq list 

        for x,y in hashmap.items():
            freq[y].append(x)
        
        # creating result list which returns k most frequent elements

        res =[]
        for x in range(len(freq)-1,0,-1): # decremnting loop
            for y in freq[x]:
                res.append(y)
                if len(res) == k:
                    return res

    
        

        
                
            
            
