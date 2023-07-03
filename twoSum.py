class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        elements = []
        found = False

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target and found == False:
                    found = True
                    elements.append(i)
                    elements.append(j)                  
        
        return elements
