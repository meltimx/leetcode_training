"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

import pytest

class Solution:
    def romanToInt(self, roman: str) -> int:
        summ = 0
        roman = roman[::-1]
        for i in range(len(roman)):
            if roman[i] == 'I':
                if roman[i-1] in ['M', 'D', 'C', 'L', 'X', 'V'] and i != 0:
                    summ -= 1
                else:
                    summ += 1
            elif roman[i] == 'V':
                if roman[i-1] in ['M', 'D', 'C', 'L', 'X'] and i != 0:
                    summ -= 5
                else:
                    summ += 5
            elif roman[i] == 'X':
                if roman[i-1] in ['M', 'D', 'C', 'L'] and i != 0:
                    summ -= 10
                else:
                    summ += 10
            elif roman[i] == 'L':
                if roman[i-1] in ['M', 'D', 'C'] and i != 0:
                    summ -= 50
                else:
                    summ += 50
            elif roman[i] == 'C':
                if roman[i-1] in ['M', 'D'] and i != 0:
                    summ -= 100
                else:
                    summ += 100
            elif roman[i] == 'D':
                if roman[i-1] == 'M' and i != 0:
                    summ -= 500 
                else:
                    summ += 500
            elif roman[i] == 'M':
                summ += 1000
        return summ
    
class BetterSolution:
    def roman_to_int(self, roman: str) -> int:
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(roman)):
            if i + 1 < len(roman) and values[roman[i]] < values[roman[i+1]]:
                result -= values[roman[i]]
            else:
                result += values[roman[i]]
        return result


@pytest.mark.parametrize('roman, expected',[
    ('III', 3),
    ('IV', 4),
    ('IX', 9),
    ('XL', 40),
    ('XC', 90),
    ('LVIII', 58),
    ('CD', 400),
    ('CM', 900),
    ('MCMXCIV', 1994),
    ('M', 1000),
])
def test_solution(roman, expected):
    sol = BetterSolution()
    assert sol.roman_to_int(roman) == expected
    