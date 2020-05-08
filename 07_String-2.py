# -*- coding: utf-8 -*-
"""
Created on Wed May  6 19:38:20 2020

@author: manchuran
@source: codingbat (python)
@module: String-2
"""

def double_char(str):
    '''
    Given a string, return a string where for every char in the original, 
    there are two chars.
    '''
    temp = [''] * len(list(str)) * 2
    temp[::2], temp[1::2] = list(str), list(str)
    return ''.join(temp)


def count_hi(str):
    '''
    Return the number of times that the string "hi" 
    appears anywhere in the given string.
    '''
    return str.count('hi')


def cat_dog(str):
    '''
    Return True if the string "cat" and "dog" 
    appear the same number of times in the given string.
    '''
    return str.count('cat') == str.count('dog')


def count_code(str):
    '''
    Return the number of times that the string "code" appears 
    anywhere in the given string, except we'll accept any letter 
    for the 'd', so "cope" and "cooe" count.
    '''
    count = 0
    for item in filter(lambda x: len(x) >=2, str.split('co')):
        if 'e' == item[1]:
            count += 1
    return count


def end_other(a, b):
    '''
    Given two strings, return True if either of the strings appears at 
    the very end of the other string, ignoring upper/lower case differences 
    (in other words, the computation should not be "case sensitive")
    '''
    if a[-len(b):].lower() == b.lower() \
    or b[-len(a):].lower() == a.lower():
        return True
    else:
        return False
    

def xyz_there(str):
    '''
    Return True if the given string contains an appearance of "xyz" 
    where the xyz is not directly preceeded by a period (.). 
    So "xxyz" counts but "x.xyz" does not.
    '''
    if 'xyz' in ''.join(str.split('.xyz')):
        return True
    return False    