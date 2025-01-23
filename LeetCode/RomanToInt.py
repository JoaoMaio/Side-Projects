class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {
         'I': 1,
         'V': 5,
         'X': 10,
         'L': 50,
         'C': 100,
         'D': 500,
         'M': 1000
        }

        total = 0

        for i in range(len(s)-1):
            if numerals[s[i]] < numerals[s[i+1]]:
                total = total - numerals[s[i]]
            else:
                total = total + numerals[s[i]]

        return total + numerals[s[-1]]

    def r(self, s: str) -> int:
        resultado = 0
        dicta = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        especial = {4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}

        s = list(s)
        k = 0

        for i in range(0, len(s)):
            if i == k:
                if i != len(s) - 1:
                    teste = f'{s[i]}{s[i + 1]}'
                    if teste in especial.values():
                        resultado += list(especial.keys())[list(especial.values()).index(teste)]
                        k += 2
                    else:
                        resultado += list(dicta.keys())[list(dicta.values()).index(s[i])]
                        k += 1
                else:
                    resultado += list(dicta.keys())[list(dicta.values()).index(s[i])]
                    k += 1

        return resultado

solution = Solution()
print(solution.romanToInt('MCMXCIV'))
print(solution.r('MCMXCIV'))