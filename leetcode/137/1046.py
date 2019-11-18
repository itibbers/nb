class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while (len(stones) > 1):
            stones.sort()
            c = stones.pop(-2)
            if stones[-1] - c > 0:
                stones[-1] -= c
            else:
                stones.pop(-1)
        stones.append(0)
        return stones[0]

