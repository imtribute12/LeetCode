class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ind = 0
        leng = len(nums)
        for i in range (leng):
            if nums[i] != val:
                nums[ind] = nums[i]
                ind += 1
        return ind
