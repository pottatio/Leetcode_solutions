#Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l=0
        reso = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            reso = max(reso,r-l+1)
        return reso
                  
def main():
    s = "abcabcbb"
    ros = Solution()
    res = ros.lengthOfLongestSubstring(s)
    print(res)
    
if __name__ == "__main__":
    main()