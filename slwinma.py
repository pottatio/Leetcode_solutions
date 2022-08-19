#You are given an array of integers nums, 
# there is a sliding window of size k which is moving
# from the very left of the array to the very right. 
# You can only see the k numbers in the window.
# Each time the sliding window moves right by one position.

import collections


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []
        q = collections.deque()
        l = r = 0
        
        while r < len(nums):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            
            if l>q[0]:
                q.popleft()
                
            if (r+1) >= k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output
        
        
def main():
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    ros = Solution()
    res = ros.maxSlidingWindow(nums,k)
    print(*res, sep = ", ")
if __name__=="__main__":
    main()