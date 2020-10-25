#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   hailstone.py
@Time    :   2020/05/26 00:31:06
@Author  :   Angie Wei 
@WebSite :   https://www.cnblogs.com/AngieWei/
'''
# Start typing your code from here

# 有穷性
def hailstone(n):
    length = 1
    while(1 < n):
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3 + 1
        length += 1
    return length

if __name__ == "__main__":
    print(hailstone(120))
    print(hailstone(7))
    print(hailstone(27))

# 21,17,112