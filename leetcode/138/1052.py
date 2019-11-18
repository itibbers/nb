class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        maxx = 0
        rr = 0
        for a in range(len(grumpy)):
            if grumpy[a] == 0:
                rr += customers[a]

        for a in range(len(grumpy)):
            if grumpy[a] == 1:
                rr += customers[a]
            if a >= X and grumpy[a - X] == 1:
                rr -= customers[a - X]
            if rr > maxx:
                maxx = rr

        return maxx
