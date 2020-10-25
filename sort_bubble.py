#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2020/04/06 23:19:13
@Author  :   Angie Wei 
@WebSite :   https://www.cnblogs.com/AngieWei/
'''
# Start typing your code from here

# 冒泡排序
# 从大到小排序
# (思路是 不断将相邻两个交换，最小的往后冒泡)


def bubble_sort(our_list):
    for i in range(len(our_list)-1):  # 注意求长度 # 固定进行len-1轮 确定len-1个元素的位置
        for j in range(len(our_list)-i-1):  # 每次循环 不比较已经确认的位置 记最后的i个(i从0开始)
            if(our_list[j] > our_list[j+1]):
                our_list[j], our_list[j+1] = our_list[j +
                                                      1], our_list[j]  # 可以这样交换
    return our_list

# 优化1，如果某一轮已经排序完毕，则不进行下一轮


def bubble_sort_1(our_list):
    is_swap = True
    while(is_swap):
        is_swap = False
        for i in range(len(our_list)-1):
            if(our_list[i] > our_list[i+1]):
                our_list[i], our_list[i+1] = our_list[i+1], our_list[i]
                is_swap = True  # 该论仍有交换
    return our_list

# 优化2，在优化1的基础上，添加上一轮结束位标记。后面不在比较 因为肯定是最小的.


def bubble_sort_2(our_list):
    is_swap, current_pos = True, len(our_list)-1
    while(is_swap):
        is_swap = False
        for i in range(current_pos):
            if(our_list[i] > our_list[i+1]):
                our_list[i], our_list[i+1] = our_list[i+1], our_list[i]
                current_pos = i
                is_swap = True
    return our_list


if __name__ == "__main__":
    # list
    # print(bubble_sort([3, 5, 1, 3, 8, 7, 9, 4, 5]))  # 整体无序
    # print(bubble_sort([1, 2, 3, 5, 4, 6, 7, 8, 9]))  # 局部无序
    # print(bubble_sort([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 完全有序

    # print(bubble_sort_1([3, 5, 1, 3, 8, 7, 9, 4, 5]))  # 整体无序
    # print(bubble_sort_1([1, 2, 3, 5, 4, 6, 7, 8, 9]))  # 局部无序
    # print(bubble_sort_1([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 完全有序

    print(bubble_sort_2([3, 5, 1, 3, 8, 7, 9, 4, 5]))  # 整体无序
    print(bubble_sort_2([1, 2, 3, 5, 4, 6, 7, 8, 9]))  # 局部无序
    print(bubble_sort_2([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 完全有序

    ls = [2, 6, 5, 3, 1]
    print(len(ls))
    # len=5, len-1 =4, range(4) 不包括4，是4个数 从0开始 不包括4[0,1,2,3]
    print(list(range(len(ls)-1)))
