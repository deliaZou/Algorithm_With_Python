#coding=utf8
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        """
        在链表后面增加一个元素
        """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def is_empty(self):
        """
        判断链表是否为空
        """
        return not self.head

    def get_length(self):
        """
        获取链表的长度
        """
        # 临时变量指向队列头部
        temp = self.head
        # 计算链表的长度变量
        length = 0
        while temp != None:
            length = length+1
            temp = temp.next
        # 返回链表的长度
        return length

    def insert_1(self, position, new_element):
        """
        在链表中指定索引处插入元素
        """
        if position < 0 or position > self.get_length():
            raise IndexError('insert 插入时,key 的值超出了范围')
        temp = self.head
        if position == 0:
            # new_element.next = temp
            # self.head = new_element
            new_element.next, self.head = temp, new_element
            return
        i = 0
        # 遍历找到索引值为 position 的结点后, 在其后面插入结点
        while i < position:
            # pre = temp
            # temp = temp.next
            pre, temp = temp, temp.next
            i += 1
        # pre.next = node
        # node.next = temp
        pre.next, new_element.next = new_element, temp

    def print_list(self):
        """
        遍历链表，并将元素依次打印出来
        """
        print("linked_list:")
        temp = self.head
        new_list = []
        while temp is not None:
            new_list.append(temp.data)
            temp = temp.next
        print(new_list)

    def remove(self, position):
        """
        删除指定索引的链表元素
        """
        if position < 0 or position > self.get_length()-1:
            # print("insert error")
            raise IndexError('删除元素的位置超出范围')

        i = 0
        temp = self.head
        # 遍历找到索引值为 position 的结点
        while temp != None:
            if position == 0:
                self.head = temp.next
                temp.next = None
                return True
            # pre = temp
            # temp = temp.next
            pre, temp = temp, temp.next

            i += 1
            if i == position:
                # pre.next = temp.next
                # temp.next = None
                pre.next, temp.next = temp.next, None
                return

    def reverse(self):
        """
        将链表反转
        """
        prev = None
        current = self.head
        while current:
            # next_node = current.next
            # current.next = prev
            # prev = current
            # current = next_node
            next_node, current.next = current.next, prev
            prev, current = current, next_node
        self.head = prev

    def initlist(self, data_list):
        '''
        将列表转换为链表
        '''
        # 创建头结点
        self.head = Node(data_list[0])
        temp = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data_list[1:]:
            node = Node(i)
            temp.next = node
            temp = temp.next

    def swapNodes(self, d1, d2):
        prevD1 = None
        prevD2 = None
        if d1 == d2:
            return
        else:
            D1 = self.head
            while D1 is not None and D1.data != d1:
                prevD1 = D1
                D1 = D1.next
            D2 = self.head
            while D2 is not None and D2.data != d2:
                prevD2 = D2
                D2 = D2.next
            if D1 is None and D2 is None:
                return
            if prevD1 is not None:
                prevD1.next = D2
            else:
                self.head = D2
            if prevD2 is not None:
                prevD2.next = D1
            else:
                self.head = D1
            temp = D1.next
            D1.next = D2.next
            D2.next = temp

if __name__ == '__main__':
    list = Linked_List()
    list.insert(5)
    list.insert(4)
    list.insert(3)
    list.insert(2)
    list.insert(1)
    list.print_list()
    list.swapNodes(1, 4)
    print("After swapping")
    list.print_list()