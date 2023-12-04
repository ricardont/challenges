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
        # if  not (1 <= len(s) <= 15)  or not all( c in romanLttr for c in s) or res not in range(0,10000):
        #     return None
        skip=False
        for i in range(0, len(s)):  
            if skip:
                skip=False
                continue            
            currentLetter = s[i]
            if  i < len(s)-1 and (
                                  (currentLetter == "I" and (s[i+1] in ["X","V"])) or
                                  (currentLetter == "X" and (s[i+1] in ["L","C"])) or 
                                  (currentLetter == "C" and (s[i+1] in ["D","M"]))
                                 ):
                succesLetter = s[i+1]                    
                res += romanLttr[succesLetter] - romanLttr[currentLetter] 
                skip=True
            else:
                res += romanLttr[s[i]]            
        return res
    

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