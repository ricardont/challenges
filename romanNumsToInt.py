class Solution:
    def romanToInt(self, s: str) -> int:
        romanLttr = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
            "":0
        }
        res = 0     
        for i in range(len(s)-1):  
            if romanLttr[s[i]] < romanLttr[s[i+1]]:
                res -= romanLttr[s[i]] 
            else:
                res += romanLttr[s[i]]            
        return res+romanLttr[s[-1]]
    

print("DCXXI equals 621 => " + str(Solution().romanToInt("DCXXI")))
print("VIII equals 8 => " + str(Solution().romanToInt("VIII")))
print("III equals 3 => " + str(Solution().romanToInt("III")))
print("X equals 10 => " + str(Solution().romanToInt("X")))
print("IX equals 9 => " + str(Solution().romanToInt("IX")))
print("IV equals 4 => " + str(Solution().romanToInt("IV")))
print("LVIII equals 58 => " + str(Solution().romanToInt("LVIII")))
print("MCMXCIV equals 1994 => " + str(Solution().romanToInt("MCMXCIV")))
# s = "IVX"
# print(s[len(s)-1])
# print(len(s)-1)

# dictionary definition is a must {"I":1} - 
# Concerns 
#   validate only permited characters   - 
#   validate within range [1, 3999], else non 
# loop through all string letters from left to righ -
# save letter predecesro, letter, letter succesor, 
# get equivalence single letter number