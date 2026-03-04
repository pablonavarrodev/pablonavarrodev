class Solution:
    def romanToInt(self, s: str) -> int:

        total = 0
        i = len(s) - 1

        while i >= 0:

            if s[i] == "I":
                total += 1
                i -= 1

            elif s[i] == "V":
                if i > 0 and s[i-1] == "I":
                    total += 4
                    i -= 2
                else:
                    total += 5
                    i -= 1

            elif s[i] == "X":
                if i > 0 and s[i-1] == "I":
                    total += 9
                    i -= 2
                else:
                    total += 10
                    i -= 1

            elif s[i] == "L":
                if i > 0 and s[i-1] == "X":
                    total += 40
                    i -= 2
                else:
                    total += 50
                    i -= 1

            elif s[i] == "C":
                if i > 0 and s[i-1] == "X":
                    total += 90
                    i -= 2
                else:
                    total += 100
                    i -= 1

            elif s[i] == "D":
                if i > 0 and s[i-1] == "C":
                    total += 400
                    i -= 2
                else:
                    total += 500
                    i -= 1

            else: 
                if i > 0 and s[i-1] == "C":
                    total += 900
                    i -= 2
                else:
                    total += 1000
                    i -= 1

        return total