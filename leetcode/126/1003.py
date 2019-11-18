class Solution:
    def isValid(self, S: str) -> bool:
        while S != '' and 'abc' in S:
            S = S.replace('abc','')
        return S == ''