#coding = utf8
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


if __name__ == '__main__':
    sequence = [12, 27, 46, 16, 25, 37, 22, 29, 15, 47, 48, 34]
    print('1.冒泡排序结果',bubble_sort(sequence))
    print('2.选择排序结果',select_sort(sequence))
    print('3.插入排序结果',insert_sort(sequence))