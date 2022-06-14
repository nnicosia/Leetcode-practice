from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
        paren = {"}" : "{", "]" : "[", ")" : "(" }
        stack = []
        for char in s:
            if stack and paren.get(char, 0) == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0

        
def main():

    test = Solution() 
    print(test.isValid("(]"))



if __name__ == "__main__":
    main()