class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for n in s :

            if (n==')' or n==']' or n=='}') and len(stack)==0:
                return False
            elif n == '(' or n =='[' or n == '{' :
                stack.append(n)
            else :
                if (n == ')' and stack[-1]!='(') or (n == ']' and stack[-1]!='[') or (n == '}' and stack[-1]!='{') :
                    return False
                else :
                    stack.pop()

        if len(stack)==0 :
            return True
        else :
            return False 