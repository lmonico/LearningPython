class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        results = list()
        i = 0
        for num in nums:
            sum = sum + num
            results.append(sum)
        return results
