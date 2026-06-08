class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        
        prod = 1
        for i in range(len(nums)):
            prefix.append(prod)
            prod *= nums[i]
        print(prefix)
        suffix = []
        prod = 1
        for i in range(len(nums) -1,-1,-1):
            suffix.append(prod)
            prod *= nums[i]

        suffix.reverse()
        result = []

        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])

        return result 
        
           
        
            