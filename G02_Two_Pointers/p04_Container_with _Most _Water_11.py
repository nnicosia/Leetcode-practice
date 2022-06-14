
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0

        while l < r:
            area = (r - l) * min(height[l], height[r])
            maxArea = max(area, maxArea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea
        
def main():

    test = Solution() 
    print(test.maxArea([1,8,6,2,5,4,8,3,7]))



if __name__ == "__main__":
    main()