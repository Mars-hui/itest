#coding = utf-8
class Node(object):
    def __init__(self,elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):

    def __init__(self,node = None):
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        #cur:游标，记录当前移动的位置
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.elem,end=' ')
            cur = cur.next
        print("")
    def add(self,item):
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self,item):
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
        else:
            while cur.next != None:
                cur = cur.next
            cur.next = node

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
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self,item):
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

if __name__ == '__main__':
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())
    ll.append(1)
    print(ll.is_empty())
    print(ll.length())
    ll.append(2)

    ll.add(8)
    ll.insert(-1,9)
    ll.travel()
    ll.insert(3,100)
    ll.travel()
    ll.insert(10,200)
    ll.remove(100)
    ll.travel()
