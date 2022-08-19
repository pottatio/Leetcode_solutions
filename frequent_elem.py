#Given an integer array nums and an integer k, return the k most frequent 
#elements.You may return the answer in any order.

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count ={}
        freq = [[] for i in range(len(nums)+1)]
        
        for n in nums:
            count[n] = 1+count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1 , 0 ,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

def main():
    nums = [4,4,4,2,2,1,1,1,1,1]
    k=2
    ros = Solution()
    res = ros.topKFrequent(nums,k)
    print(*res, sep = ", ") 
    
if __name__ == "__main__":
    main()
    