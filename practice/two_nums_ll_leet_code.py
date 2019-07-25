# from leet codes

#Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

#The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

#You may assume that each input would have exactly one solution and you may not use the same element twice.

#Input: numbers={2, 7, 11, 15}, target=9
#Output: index1=1, index2=2

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
       
        # see if there is a number >= target, thats the mid point
        
        for num in numbers:
            tar=target-num
            if tar in numbers:
                index1=numbers.index(num)
                index2=numbers.index(tar)
                return [index1 +1,index2 +1]

a =Solution()

n=[2,3,4]
t=6

print (a.twoSum(n,t))
