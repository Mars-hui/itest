#coding = utf-8
class Node(object):
    def __init__(self,elem):
        self.elem = elem
        self.next = None

class SingleCycleLinkList(object):

    def __init__(self,node = None):
        self.__head = node
        if node:
            node.next = node   #指向自己

    def is_empty(self):
        return self.__head == None

    def length(self):
        #cur:游标，记录当前移动的位置
        cur = self.__head
        count = 1
        if self.is_empty():
            return 0
        else:
            while cur.next != self.__head:
                count += 1
                cur = cur.next
            return count

    def travel(self):
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=' ')
            cur = cur.next
        print(cur.elem)
        # print("")

    def add(self,item):
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = self.__head

    def append(self,item):
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self,pos,item):
        #pos从0开始
        node = Node(item)
        pre = self.__head
        count = 0
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            while count < pos-1:
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self,item):
        cur = self.__head
        pre = None
        if self.is_empty():
            return
        else:
            while cur.next != self.__head:
                if cur.elem == item:
                    if cur == self.__head:
                        # self.__head = cur.next
                        #删除头节点
                        #遍历找到尾节点，让尾节点指向头节点
                        rear = self.__head
                        while rear.next != self.__head:
                            rear = rear.next
                        self.__head = cur.next
                        rear.next = self.__head
                    else:
                        #删除中间节点
                        pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
        # 删除尾节点
        if cur.next == self.__head:
            if cur == self.__head:
                self.__head = None
            else:
                pre.next = cur.next

    def search(self,item):
        cur = self.__head
        if self.is_empty():
            return False
        else:
            while cur.next != self.__head:
                if cur.elem == item:
                    return True
                else:
                    cur = cur.next
        if cur.elem == item:
            return True
        return False

if __name__ == '__main__':
    ll = SingleCycleLinkList()
    print(ll.is_empty())
    print(ll.length())
    ll.append(1)
    print(ll.is_empty())
    print(ll.length())
    ll.append(2)
    print(ll.length())

    ll.add(8)
    print(ll.length())
    ll.travel()
    ll.insert(-1,9)
    ll.travel()
    ll.insert(3,100)
    ll.travel()
    ll.insert(10,200)
    ll.remove(100)
    ll.travel()
