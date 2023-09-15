class Solution:
    def isValid(self, s):
        stack = []
        closeToOpen = {"}" : "{", "]" : "[", ")" : "("}
        for c in s:
            if c in closeToOpen:
                #[-1] is the last value
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(c)

        return True if not stack else False

Tester = Solution()
print(Tester.isValid("[]()"))
