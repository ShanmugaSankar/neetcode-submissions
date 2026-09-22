class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores: List = []
        for calc in operations:
            if calc == "+":
                scores.append(scores[-1] + scores[-2])
            elif calc == "D":
                scores.append(2 * scores[-1])
            elif calc == "C":
                scores.pop()
            else:
                scores.append(int(calc))
        return sum(scores)