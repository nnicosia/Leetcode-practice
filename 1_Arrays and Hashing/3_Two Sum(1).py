class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # index : value
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        
test = Solution()
nums = [2,7,11,15]
target = 9
test.twoSum(nums, target)