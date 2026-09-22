class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxVal = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if maxVal < count:
                    maxVal = count
            else:
                count = 0
        return maxVal