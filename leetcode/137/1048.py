from collections import defaultdict


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        res = defaultdict(int)
        for word in words:
            res[word] = max(res[word[:i] + word[i + 1:]] for i in range(len(word))) + 1
        return max(res.values())
