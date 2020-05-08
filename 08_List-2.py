# -*- coding: utf-8 -*-
"""
Created on Wed May  6 19:38:20 2020

@author: manchuran
@source: codingbat (python)
@module: List-2
"""
def count_evens(nums):
    '''
    Return the number of even ints in the given array. 
    Note: the % "mod" operator computes the remainder, 
    e.g. 5 % 2 is 1.
    '''
    return len(list(filter(lambda y: (y - 1) % 2, nums)))


def big_diff(nums):
    '''
    Given an array length 1 or more of ints, 
    return the difference between the largest and smallest 
    values in the array.
    '''
    return max(nums) - min(nums)


def centered_average(nums):
    '''
    Return the "centered" average of an array of ints, which we'll say is the 
    mean average of the values, except ignoring the largest and smallest values 
    in the array. If there are multiple copies of the smallest value, 
    ignore just one copy, and likewise for the largest value. 
    Use int division to produce the final average. 
    You may assume that the array is length 3 or more.
    '''
    nums = sorted(nums)
    return sum(nums[1:-1]) // len(nums[1:-1])


def sum13(nums):
    '''
    Return the sum of the numbers in the array, returning 0 for an empty 
    array. Except the number 13 is very unlucky, so it does not count and 
    numbers that come immediately after a 13 also do not count.
    '''
    if nums == []:
        return 0
    while (13 in nums):
        ind = nums.index(13)
        nums = nums[:ind] + nums[ind + 2:]
        return sum(nums)


def sum67(nums):
    '''
    Return the sum of the numbers in the array, except ignore sections of 
    numbers starting with a 6 and extending to the next 7 
    (every 6 will be followed by at least one 7). 
    Return 0 for no numbers.
    '''
    if nums == []:
        return 0
    
    total = 0
    
    flag = False
    for num in nums:
        if num == 6:
            flag = True
            
        if flag == False:
            total += num
            
        if num == 7:
            flag = False
            
    return total

  

def has22(nums):
    '''
    Given an array of ints, return True if the array contains 
    a 2 next to a 2 somewhere.
    '''
    for ind in range(len(nums) - 1):
        if nums[ind] == nums[ind + 1] == 2:
            return True
    return False