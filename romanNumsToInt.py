class Solution:
    def romanToInt(self, s: str) -> int:
        # dictionary definition is a must {"I":1} - 
        rlv = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        res = 0
        # loop through all string letters from left to righ - but the last element to avoid array limit errors
        for i in range(len(s)-1):
        #   get letter numeric value = > lnv
        #   if c urrent lnv is lower than succesor lnv  substracr it to the final result else  add it up to the final result 
            if rlv[s[i]] < rlv[s[i+1]]:
                res -= rlv[s[i]] 
            else:     
                res += rlv[s[i]] 
        # add up the last element left (excluded from previous loop)
        res += rlv[s[-1]]
        return res

#test cases
print("IX " + str(Solution().romanToInt("IX")) + " => " + str(Solution().romanToInt("IX") == 9))
print("MCMXCIV " + str(Solution().romanToInt("MCMXCIV")) + " => " + str(Solution().romanToInt("MCMXCIV") == 1994))
print("IV " + str(Solution().romanToInt("IV")) + " => " + str(Solution().romanToInt("IV") == 4))
print("LVIII " + str(Solution().romanToInt("LVIII")) + " => " + str(Solution().romanToInt("LVIII") == 58))
print("DCXXI " + str(Solution().romanToInt("DCXXI")) + " => " + str(Solution().romanToInt("DCXXI") == 621))
print("VIII " + str(Solution().romanToInt("VIII")) + " => " + str(Solution().romanToInt("VIII") == 8))
print("III " + str(Solution().romanToInt("III")) + " => " + str(Solution().romanToInt("III") == 3))
print("X " + str(Solution().romanToInt("X")) + " => " + str(Solution().romanToInt("X") == 10))