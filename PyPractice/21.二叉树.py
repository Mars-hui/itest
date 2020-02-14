#coding = utf - 8
#二叉树：

class Node(object):
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None
class Tree(object):
    def __init__(self):
        self.root = None
    def add_tree(self,item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)
    #递归实现--先序遍历
    def preorder(self,node):
        if node is None:
            return
        print(node.elem, end = ' ')
        self.preorder(node.lchild)
        self.preorder(node.rchild)
    #非递归实现--广度遍历
    def breadth_travel(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=' ')
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

if __name__ == '__main__':
    tree = Tree()
    tree.add_tree(0)
    tree.add_tree(1)
    tree.add_tree(2)
    tree.add_tree(3)
    # tree.preorder(tree.root)
    tree.breadth_travel()



