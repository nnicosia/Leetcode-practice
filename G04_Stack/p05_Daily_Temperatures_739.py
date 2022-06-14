from typing import List
class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = []
        for l, temp in enumerate(temperatures):
            r = l + 1
            while r < len(temperatures) and temperatures[r] <= temp:
                r += 1
            
            if r == len(temperatures):
                res.append(0)
            else:
                res.append(r - l)
        return res

            

            





def main():
    test = Solution()
    print(test.dailyTemperatures([30,60,90]))

if __name__ == "__main__":
    main()