"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = 0
        for digit in digits:
          number = number *10 + digit
        newnumber = number +1
        # print(len(str(newnumber)))
        dLength = len(str(newnumber))
        newList = []
        for x in range(dLength):
          newList.insert(-x,int(newnumber%10))
          newnumber = newnumber/10
        return newList