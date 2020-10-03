"""
Given two arrays of numbers, where the first array is a subset of the
second array, return an array containing all the next greater elements
for each element in the first array, in the second array. If there is no
greater element for any element, output -1 for that number.

Ex: Given the following arrays…

nums1 = [4,1,2]
nums2 = [1,3,4,2],
-> return [-1, 3, -1]
because no element in nums2 is greater than 4, 3 is the first number in
nums2 greater than 1, and no element in nums2 is greater than 2.

nums1 = [2,4]
nums2 = [1,2,3,4]
-> return [3, -1]
because 3 is the first greater element that occurs in nums2 after 2 and
no element is greater than 4.
"""

# I personally found the wording for this horrible, so I'll try my best
# to rephrase:
# For every element N in nums1, return the first number that is bigger
# than N in and occurs after N in nums2. If no such number exists,
# return -1.
#
# PS. I can't seem to come up with a solution for this that isn't O(N^2)
