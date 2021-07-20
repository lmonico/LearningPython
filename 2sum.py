class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i = 0
        #element = nums.pop(0)
        index1 = 0
        index2 = 1
        #for num in nums:
        while i < len(nums):
            while j < len(nums):
                if(nums[i] + nums[j] == target):
                    return [i,j]
                j += 1
            i += 1
            j = i + 1
            # if(num + element == target):
            #     return [index1, index2]
            # else:
            #     i += 1
            #     if(i < len(nums)):
            #         index2 += 1
            #         if(len(nums) == 2 & nums[0] + nums[1] == target):
            #             return [index1+1,index2]
            #     else:
            #         index1 += 1
            #         element = nums.pop(0)
            #         index2 = index1 + 1

newSolution = Solution()
answer = newSolution.twoSum([3,2,4],6)
print(answer)
