class Solution:

    def encode(self, strs: List[str]) -> str:
        returnStr = ""

        for s in strs:
            returnStr += str(len(s)) + "#" + s

        return returnStr

    def decode(self, s: str) -> List[str]:
        result: list[str] = []

        n = 0
        tempWord = ""
        numberStr = ""
        while n < len(s):
            ch = s[n]
            if ch != '#':
                numberStr += ch
            elif ch == '#':
                num = int(numberStr)
                numberStr = ""
                tempWord = s[n+1:n+1+num]
                n = n + num
                result.append(tempWord)

            n = n + 1

        return result