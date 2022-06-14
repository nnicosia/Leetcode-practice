
from re import L
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1 
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row - 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        if not (top <= bot):
            return False
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False

        # l_row, r_row = 0, len(matrix) - 1 
        # while l_row <= r_row:
        #     mid_row = (l_row + r_row) // 2
        #     if target < matrix[mid_row][0]:
        #         r_row = mid_row - 1
        #     elif target > matrix[mid_row][-1]:
        #         l_row = mid_row + 1
        #     else:
        #         break
        # l, r = 0, len(matrix[mid_row]) - 1
        # while l <= r:
        #     m = (l + r) // 2
        #     if target < matrix[mid_row][m]:
        #         r = m - 1
        #     elif target > matrix[mid_row][m]:
        #         l = m + 1
        #     else:
        #         return True
        # return False
        
         
def main():

    test = Solution()
    print(test.searchMatrix([[1,3]], 3))

if __name__ == "__main__":
    main()