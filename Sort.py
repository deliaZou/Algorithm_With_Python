#coding = utf8
import math
'''1.冒泡排序'''
def bubble_sort(sequence):
    for i in range(1, len(sequence)):
        for j in range(0,len(sequence)-i):
            if sequence[j] > sequence[j+1]:
                sequence[j],sequence[j+1] = sequence[j+1],sequence[j]
    return  sequence

'''2.选择排序'''
def select_sort(sequence):
    for  i in range(len(sequence)):
        min_index = i
        for j in range(i+1,len(sequence)-1):
            if sequence[j] < sequence[min_index]:
                min_index = j
        sequence[min_index],sequence[i] = sequence[i],sequence[min_index]
    return sequence

'''3.插入排序'''
def insert_sort(sequence):
    for index in range(1,len(sequence)-1):
        while(index > 0 and sequence[index-1] > sequence[index]):
            sequence[index],sequence[index-1] = sequence[index-1],sequence[index]
            index -= 1
    return sequence

'''4.希尔排序'''
def shell_sort(sequence):
    gap = len(sequence)
    while gap > 1:
        gap = gap // 2
        for i in range(gap,len(sequence)):
            for j in range(i%gap, i, gap):
                if sequence[j] > sequence[i]:
                    sequence[i],sequence[j] = sequence[j], sequence[i]
    return sequence

'''5.归并排序'''
def merge_sort(sequence):
    if len(sequence) < 2:
        return  sequence
    mid = math.floor(len(sequence)/2)
    left, right = sequence[0:mid], sequence[mid:]
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

'''6.快速排序'''
def quick_select(sequence):
    def recursive(begin, end):
        if begin > end:
            return
        left, right = begin, end
        pivot = sequence[left]
        while left < right:
            while left < right and sequence[right] > pivot:
                right -= 1
            while left < right and sequence[right] <= pivot:
                left += 1
            sequence[left], sequence[right] = sequence[right], sequence[left]
            recursive(begin, left -1)
            recursive(right+ 1, end)

    recursive(0, len(sequence) - 1)
    return  sequence


if __name__ == '__main__':
    sequence = [12, 27, 46, 16, 25, 37, 22, 29, 15, 47, 48, 34]
    print('1.冒泡排序结果',bubble_sort(sequence))
    print('2.选择排序结果',select_sort(sequence))
    print('3.插入排序结果',insert_sort(sequence))
    print('4.希尔排序结果', shell_sort(sequence))
    print('5.合并排序结果', merge_sort(sequence))
    print('6.快速排序结果',quick_select(sequence))