import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b),
        }

        pile = []

        for n in tokens:

            if n in operations :
                calcul = operations[n]

                b = pile.pop()
                a = pile.pop()

                out = calcul(a, b)
                pile.append(out)

            else :
                pile.append(int(n))

        return pile[0]


        