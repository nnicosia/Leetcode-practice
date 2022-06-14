from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(lambda: []) 
        for word in strs:
            key = str(sorted(word))
            res[key].append(word)
        return res.values()



def main():

    test = Solution() 

    strs = ["eat","tea","tan","ate","nat","bat"]
    print(test.groupAnagrams(strs))

if __name__ == "__main__":
    main()

