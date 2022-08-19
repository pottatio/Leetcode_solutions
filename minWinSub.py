#Given two strings s and t of lengths m and n respectively, 
#return the minimum window substring of s such that every character
# in t (including duplicates) is included in the window. If there is
# no such substring, return the empty string "".

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
def main():
    s = "ADOBECODEBANC"
    t = "ABC"
    ros = Solution()
    res = ros.minWindow(s,t)
    print(*res, sep = ", ") 
    
if __name__=="__main__":
    main()