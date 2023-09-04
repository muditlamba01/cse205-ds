class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        k = 0
        for i in nums:
            if(len(str(i)))%2 == 0:
                k+=1
            else:
                    continue
        return k
