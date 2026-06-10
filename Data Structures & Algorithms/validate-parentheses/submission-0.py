class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for bracket in s:
            #if opening bracket
            if bracket in lookup.values():
                stack.append(bracket)
            #if closing bracket
            elif not stack or stack[-1] != lookup[bracket]: 
                return False
            #if valid closing bracket
            else:
                stack.pop()
        return not stack