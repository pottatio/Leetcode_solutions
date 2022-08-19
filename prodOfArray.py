#Find the product of array except the number itself.

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1 , -1 , -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


def main():
    nums = [1,2,3,4]
    ros = Solution()
    res = ros.productExceptSelf(nums)
    print(*res, sep = ", ") 

if __name__ == "__main__":
    main()