class Solution:
    def alternateDigitSum(self, n: int) -> int:
        result = 0
        st = str(n)
        for i in range(len(st)):
            result = (result + int(st[i])) if i % 2 == 0 else (result - int(st[i]))
        return result