# from leet codes

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

import copy

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pair=[]
        
        #pseudocode
        #start with full list
            #loop through elements from nums
                #subtract first element from target
                    #if not negative, or 0 continue
                        #new = copy of nums 
                        #new.pop(element)
                        # search through the remaining elements in new and find an element that maches target - original element
                        # get the index of that element from new
                        # return both index in pair
                    #else continue with next element because the element wont be in the list  

        
        for num in nums:
            newtar=target-num
            if newtar >= 0:
                new =copy.copy(nums)
                index=nums.index(num)
                new.pop(index)
                for n in new:
                    if newtar == n:
                        print ("first index", index)
                        pair.append(index)
                        print ("second index", nums.index(n))
                        pair.append(nums.index(n))
                        return pair


new=[3,2,4]
tar=6
a=Solution()

print (a.twoSum(new,tar))
