class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = set()
        
        for n in nums:
            if n in hashMap:
                return True
            hashMap.add(n)
        return False

test = Solution()
nums = [1,2,3,1]
test.containsDuplicate(nums)