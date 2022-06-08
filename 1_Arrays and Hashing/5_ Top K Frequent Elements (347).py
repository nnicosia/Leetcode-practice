from typing import List
class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        outer_array = [[] for _ in range(len(nums) + 1)]
        counter = {}

        for num in nums:
            counter[num] = 1 if num not in counter else counter[num] + 1
        for value, count in counter.items():
            outer_array[count].append(value)
        result = []
        for inner_array in reversed(outer_array):
            while inner_array and k > 0:
                result.append(inner_array.pop())
                k -= 1
            if k == 0:
                break
        return result

def main():
    test = Solution() 
    print(test.groupAnagrams([1,1,1,2,2,3], 2))

if __name__ == "__main__":
    main()

