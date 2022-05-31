class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cur = 0
        for val in nums:
            cur ^= val  
        return cur

            

test = Solution()
nums = [2,2,1]
print(test.singleNumber(nums))