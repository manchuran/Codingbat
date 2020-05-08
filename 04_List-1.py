# -*- coding: utf-8 -*-
"""
Created on Wed May  6 19:38:20 2020

@author: manchuran
@source: codingbat (python)
@module: List-1
"""
def first_last6(nums):
    '''
    Given an array of ints, return True if 6 appears as 
    either the first or last element in the array. 
    The array will be length 1 or more.
    '''
    if nums[-1:][0] == 6 or nums[:1][0] == 6:
        return True
    return False


def same_first_last(nums):
    '''
    Given an array of ints, return True if the array is length 1 or more, 
    and the first element and the last element are equal.
    '''
    if (len(nums) >= 1) and (nums[-1:] == nums[:1]):
        return True
    return False


def make_pi():
    '''
    Return an int array length 3 containing the first 3 digits of pi, 
    {3, 1, 4}.
    '''
    return [3, 1, 4]


def common_end(a, b):
    '''
    Given 2 arrays of ints, a and b, return True if they have the same 
    first element or they have the same last element. 
    Both arrays will be length 1 or more.
    '''
    if a[:1] == b[:1] or a[-1:] == b[-1:]:
        return True
    return False


def sum3(nums):
    '''
    Given an array of ints length 3, return the sum of all the elements.
    '''
    return sum(nums)


def rotate_left3(nums):
    '''
    Given an array of ints length 3, return an array with the elements 
    "rotated left" so {1, 2, 3} yields {2, 3, 1}.
    '''
    return nums[1:] + nums[:1]


def reverse3(nums):
    '''
    Given an array of ints length 3, return a new array with the 
    elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
    '''
    return nums[::-1]


def max_end3(nums):
    '''
    Given an array of ints length 3, figure out which is larger, 
    the first or last element in the array, and set all the other 
    elements to be that value. Return the changed array.
    '''
    if nums[:1] > nums[-1:]:
        return nums[:1] + map(lambda x: nums[:1][0], nums[1:])
    return nums[-1:] + map(lambda x: nums[-1:][0], nums[:-1])


def sum2(nums):
    '''
    Given an array of ints, return the sum of the first 2 elements 
    in the array. If the array length is less than 2, 
    just sum up the elements that exist, returning 0 if the array is 
    length 0.
    '''
    if len(nums) == 0:
        return 0
    return sum(nums[:2])


def middle_way(a, b):
    '''
    Given 2 int arrays, a and b, each length 3, 
    return a new array length 2 containing their middle elements.
    '''
    return a[len(a) // 2:len(a) // 2 + 1] \
      + b[len(b) // 2:len(b) // 2 + 1]
      

def make_ends(nums):
    '''
    Given an array of ints, return a new array length 2 containing 
    the first and last elements from the original array. 
    The original array will be length 1 or more.
    '''
    return nums[:1] + nums[-1:]


def has23(nums):
    '''
    Given an int array length 2, return True if it contains a 2 or a 3.
    '''
    if 2 in nums or 3 in nums:
        return True
    return False


