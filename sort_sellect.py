#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   sort_sellect.py
@Time    :   2020/05/24 09:53:47
@Author  :   Angie Wei 
@WebSite :   https://www.cnblogs.com/AngieWei/
'''
# Start typing your code from here

# 选择排序

# 最差 的情况 每一次都会交换，增大内存
def selection_sort(our_list):
    for i in range(len(our_list)-1):
        for j in range(i+1, len(our_list)):  # 每次找到一个都移动一下
            if(our_list[i] > our_list[j]):
                our_list[i], our_list[j] = our_list[j], our_list[i]
    return our_list

# 先记录位置，循环后交换
def selection_sort_1(our_list):
    min_index = 0
    for i in range(len(our_list)-1):
        min_index = i
        for j in range(i+1, len(our_list)):
            if(our_list[min_index] > our_list[j]):# 和当前最小位置的最小值比较
                min_index = j# 先找到最i小的值的位置 
        if min_index != i: # 如果最i小的值的位置不是 当前的i位置，则替换
            our_list[i], our_list[min_index] = our_list[min_index], our_list[i]
    return our_list

# 网友做法，两边向中间逼近，总循环数是n//2，分别找到最大和最小放在两端，然后范围去掉最大和最小的中间的部分。
def selection_sort_2(our_list):
    n=len(our_list)
    # print(n//2) 4
    for i in range(n//2):
        min_index = i
        max_index = n-i-1
        # print(list(range(i+1,n-i)))
        for j in range(i+1,n-i):
            if(our_list[min_index]>our_list[j]):
                min_index = j
        if min_index != i:
            our_list[i],our_list[min_index] = our_list[min_index],our_list[i]
        # print(list(range(n-i-2, i,-1)))
        for j in range(n-i-2, i,-1):
            if(our_list[max_index]<our_list[j]):
                max_index = j
        if max_index !=n-i-1:
            our_list[max_index],our_list[n-i-1] = our_list[n-i-1],our_list[max_index]
    return our_list

def selection_sort_3(our_list):
    n = len(our_list)
    for i in range(n//2):
        min_index = i
        max_index = n-i-1
        for j in range(i,n-i):# 每次的 最边上的值也比
            if(our_list[min_index]>our_list[j]):
                min_index = j
            if(our_list[max_index]<our_list[j]):
                max_index = j
        if(max_index!=n-i-1):
            our_list[max_index],our_list[n-i-1] = our_list[n-i-1],our_list[max_index]
        if(min_index!=i):
            our_list[min_index],our_list[i] = our_list[i],our_list[min_index]
        # print(our_list) # for debug
    return our_list

if __name__ == "__main__":
    print(selection_sort_3([3, 5, 1, 3, 8, 7, 9, 4, 5]))  # 整体无序
    print(selection_sort_3([1, 2, 3, 5, 4, 6, 7, 8, 9]))  # 局部无序
    print(selection_sort_3([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 完全有序

    # print(selection_sort_2([3, 5, 1, 3, 8, 7, 9, 4, 5]))  # 整体无序
    # print(selection_sort_2([1, 2, 3, 5, 4, 6, 7, 8, 9]))  # 局部无序
    # print(selection_sort_2([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 完全有序

    # print(selection_sort_1([3, 5, 1, 3, 8, 7, 9, 4, 5]))  # 整体无序
    # print(selection_sort_1([1, 2, 3, 5, 4, 6, 7, 8, 9]))  # 局部无序
    # print(selection_sort_1([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 完全有序

    # print(selection_sort([3, 5, 1, 3, 8, 7, 9, 4, 5]))  # 整体无序
    # print(selection_sort([1, 2, 3, 5, 4, 6, 7, 8, 9]))  # 局部无序
    # print(selection_sort([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 完全有序