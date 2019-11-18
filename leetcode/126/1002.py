class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        result = [];
        # 队列为空，或者队列长度小于2，返回空
        if not A or len(A) < 2:
            return result;

        # 获取队列中第一位的所有的字符
        setKey = set(A[0])

        # 遍历字符，并获取所有字符串中出现的次数的最小值
        for x in setKey:
            num = min(a.count(x) for a in A)
            for i in range(num):
                result.append(x)
        return result
