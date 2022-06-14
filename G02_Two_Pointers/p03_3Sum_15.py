from re import L
from turtle import update
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = {}
        
        updatedNums = sorted(nums)
        
        for i in range(len(updatedNums) - 1):
            l, r = i + 1, len(nums) - 1 

            
            while l < r:
                cur = updatedNums[i] + updatedNums[l] + updatedNums[r]
                if cur == 0:
                    result[str([updatedNums[i], updatedNums[l], updatedNums[r]])] = [updatedNums[i], updatedNums[l], updatedNums[r]]

                    l += 1
                    r -= 1
                elif cur < 0:
                    l += 1
                else :
                    r -= 1
                
        return result.values()

    def neetCodeThreeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return result

# Neetcode solution

def main():
    test = Solution() 
    print(test.neetCodeThreeSum([-1,0,1,2,-1,-4]))


if __name__ == "__main__":
    main()