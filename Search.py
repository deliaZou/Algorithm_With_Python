#coding = utf8
import math
import random
'''1.顺序搜索'''
def sequencesearch(sequence, target):
    for i in range(len(sequence)):
        if target == sequence[i]:
            return i
    return  None

'''2.二分搜索'''
def binarysearch(sequence, target):
    left = 0
    right = len(sequence) - 1
    while (left <= right):
        middle = (left + right) // 2
        m = sequence[middle]
        if m == target:
            return middle
        elif m < target:
            left = middle + 1
        else:
            right = middle - 1
    return None

'''3.差值搜索'''
def insertsearch(sorted_sequence, target):
    left = 0
    right = len(sorted_sequence) - 1
    while(left <= right):
        midpoint = left + (target - sorted_sequence[left])* (right - left)//(sorted_sequence[right]-sorted_sequence[left])
        if midpoint < 0 or midpoint >= len(sorted_sequence) - 1:
            return None
        elif sorted_sequence[midpoint] == target:
            return midpoint
        elif sorted_sequence[midpoint] > target:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return None

'''4.跳跃搜索'''
def jumpsearch(sorted_sequence, target):
    n = len(sorted_sequence)
    step = int(math.floor(math.sqrt(n)))
    prev = 0
    while sorted_sequence[min(step, n) - 1] < target:
        prev = step
        step = step + int(math.floor(math.sqrt(n)))
        if prev > n:
            return None
    while sorted_sequence[prev] < target:
        prev = prev + 1
        if prev == min(step, n):
            return None
    if sorted_sequence[prev] == target:
        return prev
    else:
        return None

'''5.快速搜索'''
def partition(sequence, left, right, pivot_index):
    pivot_value = sequence[pivot_index]
    # 交换两个元素，使pivot_index与最右边元素置换位置，即先将pivot移动到最右边
    sequence[pivot_index], sequence[right] = sequence[right], sequence[pivot_index]
    store_index = left
    for i in range(left, right):
        if sequence[i] < pivot_value:
            # 交换两个元素，使当前遍历元素(小于pivot_value的元素)与store_index元素置换位置
            sequence[store_index], sequence[i] = sequence[i], sequence[store_index]
            store_index = store_index+1  # store_index索引增加1
    # 交换两个元素，使store_index与最右边元素置换位置，即交换回来pivot最终应该在的位置
    sequence[store_index], sequence[right] = sequence[right], sequence[store_index]
    return store_index

def quick_search(sequence, left, right, k):
    if left == right:  # 如果只有一个元素
        return sequence[left]  # 返回该元素
    # 初始 pivot_index，使 pivot_index 在无序表随机
    pivot_index = left+random.randint(0, right-left+1)
    # pivot 在已经排好序的位置
    pivot_index = partition(sequence, left, right, pivot_index)
    if k == pivot_index:
        return sequence[k]  # 返回该位置元素
    elif k < pivot_index:
        # 需要在[left,pivot_index-1]里面继续快速检索
        return quick_search(sequence, left, pivot_index-1, k)
    else:
        # 需要在[pivot_index+1,right]里面继续快速检索
        return quick_search(sequence, pivot_index+1, right, k)

'''6.哈希搜索'''
class HashTable:
    def __init__(self, size):
        # 使用list数据结构作为哈希表元素保存方法
        self.elem = [None for i in range(size)]
        self.count = size  # 最大表长

    def hash(self, key):
        # 散列函数采用除留余数法
        return key % self.count

    def insert_hash(self, key):
        # 插入关键字到哈希表内
        address = self.hash(key)  # 求散列地址
        # 当前位置已经有数据了，发生冲突。
        while self.elem[address]:
            # 线性探测下一地址是否可用
            address = (address+1) % self.count
        # 没有冲突则直接保存。
        self.elem[address] = key

    def search_hash(self, key):
        # 查找关键字，返回布尔值
        star = address = self.hash(key)
        while self.elem[address] != key:
            address = (address + 1) % self.count
            # 说明没找到或者循环到了开始的位置
            if not self.elem[address] or address == star:
                return False
        return True, address  # 返回索引值


if __name__ == '__main__':
    sorted_sequence = [i for i in range(1, 10001, 2)]
    target = 521
    print('1.顺序搜索测试结果:', sequencesearch(sorted_sequence,target))
    print('2.二分搜索测试结果:', binarysearch(sorted_sequence,target))
    print('3.差值搜索测试结果:', insertsearch(sorted_sequence, target))
    print('4.跳跃搜索测试结果:', jumpsearch(sorted_sequence, target))
    sequence = [12]
    left = 0
    right = len(sequence) - 1
    k = int(input("Find the k'th smallest number in sequence,k=")) - 1
    value = quick_search(sequence, left, right, k)
    print('5.快速搜索测试结果:', quick_search(sequence, left, right, k))
    list_a = [12, 67, 56, 16, 25, 37, 22, 29, 15, 47, 48, 34]
    hash_table = HashTable(12)
    for i in list_a:
        hash_table.insert_hash(i)
    for i in hash_table.elem:
        if i:
            print((i, hash_table.elem.index(i)), end=" ")
    print("\n")
    print('6.快速搜索测试结果:',hash_table.search_hash(15))
    print('6.快速搜索测试结果:',hash_table.search_hash(33))