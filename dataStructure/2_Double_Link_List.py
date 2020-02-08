#coding = utf-8

class Node(object):
    '''节点'''
    def __init__(self,elem):
        self.elem = elem
        self.next = None
        self.prev = None

class DoubleLinkList(object):
    '''双链表'''
    def __init__(self,node = None):
        self.__head = node

    def is_empty(self):
        '''链表是否为空'''
        return self.__head == None

    def length(self):
        '''链表长度'''
        #cur为游标，用来遍历整个节点
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历整个链表'''
        cur = self.__head
        while cur != None:
            print(cur.elem,end=" ")
            cur = cur.next
        print("")
    def add(self,item):
        '''链表头部添加元素'''
        node = Node(item)
        node.next = self.__head
        self._head = node
        node.next.prev = node
    def append(self,item):
        '''链表尾部添加元素，尾插法'''
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
        else:
            while cur.next != None:
                cur = cur.next
            cur.next = node


    def insert(self,pos,item):
        '''在指定位置添加元素'''
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            cur = self._head
            count = 0
            while cur != None:
                count += 1
                cur = cur.next
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node
    def search(self,item):
        cur = self._head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

    def delete(self,item):
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                #先判断此节点是否是头节点
                #头结点
                if cur == self._head:
                    if cur.next:#判断是否仅有一个节点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next


if __name__ == '__main__':
    dll = DoubleLinkList()
    print(dll.is_empty())
    print(dll.length())
    dll.append(1)
    print(dll.is_empty())
    print(dll.length())
    dll.append(2)
    dll.add(8)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    dll.travel()



