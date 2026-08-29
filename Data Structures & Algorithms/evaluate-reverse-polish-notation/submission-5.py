import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        pile = []

        for n in tokens :
            if n == "+":
                pile.append(pile.pop()+pile.pop())
            elif n == "-":
                b, a = pile.pop(), pile.pop()
                pile.append(a-b)
            elif n == "*":
                pile.append(pile.pop()*pile.pop())
            elif n == "/":
                b, a = pile.pop(), pile.pop()
                pile.append(int(a/b))
            else :
                pile.append(int(n))
        
        return pile[0]


        