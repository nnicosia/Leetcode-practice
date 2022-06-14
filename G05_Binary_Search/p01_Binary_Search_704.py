from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target: return 0
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return -1
            


 
def main():
    test = Solution()
    print(test.search([-1,0,3,5,9,12], 9))

if __name__ == "__main__":
    main()