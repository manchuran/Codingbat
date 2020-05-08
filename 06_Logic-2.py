# -*- coding: utf-8 -*-
"""
Created on Wed May  6 19:38:20 2020

@author: manchuran
@source: codingbat (python)
@module: Logic-2
"""

def make_bricks(small, big, goal):
    '''
    We want to make a row of bricks that is goal inches long. 
    We have a number of small bricks (1 inch each) and big bricks 
    (5 inches each). Return True if it is possible to make the goal 
    by choosing from the given bricks.
    '''
    goal = goal - big*5
    if goal < 0:
        goal = goal - goal // 5 * 5
    if goal <= small:
        return True
    return False


def lone_sum(a, b, c):
    '''
    Given 3 int values, a b c, return their sum. 
    However, if one of the values is the same as another of the values, 
    it does not count towards the sum.
    '''
    temp = [a, b, c]
    temp_dict =  {i:temp.count(i) for i in temp if temp.count(i) <= 1}
    return sum(temp_dict.keys())


def lucky_sum(a, b, c):
    '''
    Given 3 int values, a b c, return their sum. 
    However, if one of the values is 13 then it does not count 
    towards the sum and values to its right do not count. 
    So for example, if b is 13, then both b and c do not count.
    '''
    if 13 not in [a, b, c]:
        return sum([a, b, c])
    else:
        return sum([a, b, c][:[a, b, c].index(13)])
    

def no_teen_sum(a, b, c):
    '''
    Given 3 int values, a b c, return their sum. 
    However, if any of the values is a teen -- in the range 13..19 
    inclusive -- then that value counts as 0, except 15 and 16 do not 
    count as a teens.
    '''
    def fix_teen(n):
        if n >= 13 and n <= 19:
            if n == 15 or n == 16:
                return n
            else:
                return 0
        else:
            return n
    
    return sum([fix_teen(i) for i in [a, b, c]])



def round_sum(a, b, c):
    '''
    For this problem, we'll round an int value up to the next multiple of 
    10 if its rightmost digit is 5 or more, so 15 rounds up to 20. 
    Alternately, round down to the previous multiple of 10 if its 
    rightmost digit is less than 5, so 12 rounds down to 10. 
    Given 3 ints, a b c, return the sum of their rounded values.
    '''
    def round10(num):
        if num % 10 >= 5:
            return num + (10 - num % 10)
        else:
            return num  - num % 10
    return sum([round10(i) for i in [a, b, c]])


def close_far(a, b, c):
    '''
    Given three ints, a b c, return True if one of b or c is "close" 
    (differing from a by at most 1), while the other is "far", 
    differing from both other values by 2 or more. Note: abs(num) 
    computes the absolute value of a number.
    '''
    if abs(a-b)<=1 and (abs(a-c)>=2 and abs(b-c)>=2):
        return True
    elif abs(a-c)<=1 and (abs(a-b)>=2 and abs(b-c)>=2):
        return True
    else:
        return False


def make_chocolate(small, big, goal):
    '''
    We want make a package of goal kilos of chocolate. 
    We have small bars (1 kilo each) and big bars (5 kilos each). 
    Return the number of small bars to use, assuming we always use big bars 
    before small bars. Return -1 if it can't be done
    '''
    goal = goal - big * 5
    if goal < 0:
        goal = goal - goal // 5 * 5
    if goal > small:
        return -1
    return goal