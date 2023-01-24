from collections import deque


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class CreateBitree:
    def __init__(self, str_tree):
        self.str_tree = str_tree

    def create_tree(self):
        l1 = list(self.str_tree)
        l1 = [None if i == "#" else i for i in l1]  # 将 # 转换为 None
        nodes = [BiTreeNode(l1[i]) for i in range(len(l1))]  # 初始化各个节点
        root = nodes[0]
        for i in range(len(l1)):
            if 2 * i + 2 > len(l1):  # 循环到最后的右孩子结束
                break

            cur_node = nodes[i]
            if nodes[2 * i + 1].data:
                cur_node.lchild = nodes[2 * i + 1]  # 当前结点的左孩子

            if nodes[2 * i + 2].data:
                cur_node.rchild = nodes[2 * i + 2]  # 当前结点的右孩子

        return root

    def __call__(self):
        return self.create_tree()


class BiTreeSorted:
    def __init__(self, root):
        self.root = root

    def pre_order(self, root):
        # 前序遍历
        if root:
            print(root.data, end=",")

            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self, root):
        # 中序遍历
        if root:
            self.in_order(root.lchild)
            print(root.data, end=",")
            self.in_order(root.rchild)

    def post_order(self, root):
        # 后序遍历
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=",")

    def level_order(self, root):
        # 层序遍历
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            node = queue.popleft()
            print(node.data, end=",")
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)

    def __call__(self):
        print("前序排列")
        self.pre_order(self.root)
        print()

        print("中序排列")
        self.in_order(self.root)
        print()

        print("后序排列")
        self.post_order(self.root)
        print()

        print("层序排列")
        self.level_order(self.root)
        print()


# 创建二叉树
a = CreateBitree("ABCDE#F##G#####")
root = a()  # 调用__call__方法
print("根节点为：", root.data)

tree_sorted = BiTreeSorted(root)
tree_sorted()  # 调用__call__方法
