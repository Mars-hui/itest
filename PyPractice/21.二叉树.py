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
            self.root = node.elem
        elif node.lchild is None:
            node.lchild = node.elem
        elif node.rchild is None:
            node.rchild = node.elem
        self.add_tree(node.lchild)
        self.add_tree(node.rchild)

if __name__ == '__main__':
    tree = Tree()
    tree.add_tree(0)


