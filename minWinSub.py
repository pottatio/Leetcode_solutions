#Given two strings s and t of lengths m and n respectively, 
#return the minimum window substring of s such that every character
# in t (including duplicates) is included in the window. If there is
# no such substring, return the empty string "".

from itertools import count
from json.encoder import INFINITY


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        countT , window = {} , {}
        
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have , need = 0,len(countT)
        res , resLen = [-1,-1] , float("infinity")
        l=0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            
            if c in countT and window[c] == countT[c]:
                have += 1
            while have==need:
                #update the result
                if(r-l+1)<resLen:
                    res = [l,r]
                    resLen = (r-l+1)
                    
                #pop from the left of the window    
                window[s[l]] -= 1
                
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l+=1
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""
                        
def main():
    s = "ADOBECODEBANC"
    t = "ABC"
    ros = Solution()
    res = ros.minWindow(s,t)
    print(*res, sep = ", ") 
    
if __name__=="__main__":
    main()