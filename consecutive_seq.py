#In the given list of integers find the numbers of longest sequence

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            if (n-1) not in numSet:
                length = 0
                while(n+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest



def main():
    nums = [100,4,200,1,3,2]
    ros = Solution()
    res = ros.longestConsecutive(nums)
    print(res)
    
if __name__ == "__main__":
    main()
