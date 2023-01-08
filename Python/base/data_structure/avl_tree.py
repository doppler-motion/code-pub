# AVL树（二叉平衡树）
# 节点类。AVL树相对一般二叉搜索树，节点增加树高属性，便于判断是否平衡，从而决定是否进行调整等。
class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 0


# AVL树类
class AVLTree(object):
    # 初始化函数和一般二叉树、二叉搜索树相同，只需创建空的根节点
    def __init__(self):
        self.root = None

    # find为公有方法（可以对外暴露），判断key是否在avl树中。
    # 与私有的_find相比，增加【树根是否为空】的判断；
    # 一般二叉搜索树查找也常用这种公有私有机制。
    def find(self, key):
        # 树根为空则返回空，没找到
        if not self.root:
            return None
        # 否则传入树的根节点寻找
        else:
            return self._find(key, self.root)

    # 私有化方法，寻找以node为根的树或者子树中是否存在键值为key的元素
    def _find(self, key, node):
        # 如果node为空，则无法找到相应key值，返回空
        if not node:
            return None
        # 如果要找key小于当前节点数据，到左子树中找
        elif key < node.data:

            return self._find(key, node.left)
        # 如果要找的key大于当前节点存储数据，到当前节点的右子树找
        elif key > node.data:
            return self._find(key, node.right)
        # 以上(不包括return None)用于递归向下延申，缩小问题规模的过程
        # 以上条件都不满足，说明这个节点存储的数据与key值相等，也就是找到了相应的元素，将这个节点返回即可
        else:
            # 用于递归向上返回结果过程
            # 这里的return，是将最后返回的node值一层层原样返回到上一层递归函数，最终返回的就是那个找到的node
            return node

    # 寻找avl树中的最小元素。
    # 类似地，公有方法增加树根空与否的判断
    def findMin(self):
        if self.root is None:
            return None
        # 树根不空，返回树的最小值
        else:
            return self._findMin(self.root)

    # 私有方法，增加传入参数node便于递归
    def _findMin(self, node):
        # avl树最小值出现在最左侧的叶子节点。
        # 只要当前节点还有左孩子节点，左孩子节点就比当前节点小，转到左孩子节点继续向下寻找
        if node.left:
            # 用于递归向下扩展并缩小问题规模
            return self._findMin(node.left)
        # 执行else时，说明左孩子已到尽头。返回当前的节点值，就是最小的
        else:
            # 类似_find最后一句，用于递归向上返回
            return node

    # 寻找avl树的最大值，使用完全相同的方法进行寻找。不再赘述。
    def findMax(self):
        if self.root is None:
            return None
        else:
            return self._findMax(self.root)

    # 看_findMin，完全对偶，不再赘述。
    def _findMax(self, node):
        # 最大值出现在最右侧，应该逐层向右延申
        if node.right:
            return self._findMax(node.right)
        else:
            return node

    # 确认一棵AVL树或其中某子树的高度，传入参数为node
    def height(self, node):
        # 空树不存在高度，返回-1
        if node is None:
            return -1
        # 否则直接返回node的height即可
        else:
            return node.height

    # 右旋(函数命名与之相反)，对应左侧过长
    # 在node节点的左孩子k1的左子树添加了新节点，左旋转
    # 输入参数应该为左左节点的紧接着的往上的那个节点

    def left_left_rotate(self, node):
        # k1首先指向node左孩子节点
        k1 = node.left
        # 开始旋转。插入后节点形状构成左左左三连(见上方代码块外的图,这里的左左左指存储2、3、4的节点(不包括1))。
        # 旋转就是使三连的中间节点上提的过程，所以关键是构造好中间节点的形状。
        # 塑造新形状分两步。
        # 第一步，释放即将上提(中间，图中是3)节点的右孩子
        # 将它赋给原来三连中最上端节点(图中是5)的左孩子，腾出右孩子。
        node.left = k1.right
        # 第二步，将中间节点的右孩子定为原来三连中最上方的节点，就完成了新形状的塑造
        k1.right = node
        # 更改node所在节点的高度
        # node(原三连最上方节点,图中对应5)被向下翻。
        # 以node为根的子树高度是它的新左子树和原右子树中较大值加1
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        # 以k1(原三连中间节点，图中对应3)被向上翻。
        # 以k1为根的子树高度是它的原左子树和新右子树(就是以node为根的树)中较大值加1
        k1.height = max(self.height(k1.left), node.height) + 1
        # 返回更改后的子树根节点，即原来三连节点的中心节点
        return k1

    # 在node节点的右孩子k1的右子树添加了新节点，左旋，对应右右的情况
    def right_right_rotate(self, node):
        # k1相当于代码块外的上图节点4
        k1 = node.right
        # 开始旋转。插入后节点形状构成右右右三连(见代码块外的图,右右右指存储2、4、5的节点(不包括6))。
        # 旋转就是使三连的中间节点上提的过程，所以关键是构造好中间节点的形状。
        # 塑造新形状分两步。
        # 第一步，释放即将上提(中间，图中是4)节点的左孩子
        # 将它赋给原来三连中最上端节点(图中是2)的右孩子，腾出左孩子。
        node.right = k1.left
        # 第二步，将中间节点的左孩子定为原来三连中最上方的节点，就完成了新形状的塑造
        k1.left = node
        # 更改node所在节点的高度
        # node(原三连最上方节点,图中对应2)被向下翻。
        # 以node为根的子树高度是它的新右子树和原左子树中较大值加1
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        # 以k1(原三连中间节点，图中对应4)被向上翻。
        # 以k1为根的子树高度是它的原右子树和新左子树(就是以node为根的树)中较大值加1
        k1.height = max(self.height(k1.right), node.height) + 1
        # 返回现子树的根节点，也就是k1
        return k1

    # 对应代码块外的上图。
    def right_left_rotate(self, node):
        # 先以子树根节点的右孩子节点（即上图中5）为中心进行右旋转，将3翻上去。
        node.right = self.left_left_rotate(node.right)
        # 以上操作过后就可以使用右右旋转(也即左旋转)达到解决冲突目的。
        # 旋转轴应为右右右三连的最上方，也就是2节点
        return self.right_right_rotate(node)

        ##再看超出两节点先向左延申，然后向右延申的情况

    def left_right_rotate(self, node):
        # 先以子树根节点的左孩子节点（即上图中2）为中心进行左旋转，将3翻上去。
        node.left = self.right_right_rotate(node.left)
        # 以上操作过后就可以使用左左旋转(也即右旋)达到解决冲突目的。
        # 旋转轴应为左左左三连的最上方，也就是5节点
        return self.left_left_rotate(node)

    # 以上面的旋转为基础，实现AVL树元素插入。插入元素是key。
    # 与刚开始的查找相似，公有私有方法分开。
    def insert(self, key):
        # 如果root根本不存在，说明没有这棵树。直接把待插元素作为树根
        if not self.root:
            self.root = TreeNode(key)
        # 否则，调用私有方法以树根为起点判断插入位置、插入、解决冲突即可。
        else:
            self.root = self._insert(key, self.root)

    # 插入的私有方法，多了一个node参数
    def _insert(self, key, node):
        # 递归的最终插入步骤。
        # 如果node是none，表明到了要插的位置，直接将key转变成node填在那里
        # 若执行了此if语句，key的node就已加入树中
        if node is None:
            node = TreeNode(key)
        # 如果key值比当前指向节点小，向左缩小范围，冲突解决时用左左或左右。
        elif key < node.data:
            # 递归沿树向下推进，转化为更小规模问题。
            node.left = self._insert(key, node.left)
            # 这样递归调用之后，最后得到了正确的应该插入的位置。
            # 插入后应针对不符合平衡树规则的冲突情况进行判断和调整。
            # 判断是否调整的标准是当前最邻近子树node.left,node.right是否满足高度差小于2的条件。
            # 递归每次返回上一层，都会调用这个判断函数层一层地判断，直到回到根节点。
            # 只要某处刚刚不满足规则(刚刚到2)，就及时整改。保证最大高度差始终不超过2
            # 经过下面代码块，任何子树都已经过判断和改造，满足平衡二叉树条件
            if (self.height(node.left) - self.height(node.right)) == 2:
                # 此if语句成立，一定存在冲突，且应从node处解决。
                # 递归返回结果时并不知道key相对于node子节点具体位置
                # 故要将key与node的子节点比较以得出key到底插入了当前冲突节点的子节点的左还是右。
                # 如果比当前冲突节点的左孩子还小，就显然通过left_left_rotate解决。
                if key < node.left.data:
                    node = self.left_left_rotate(node)
                # 否则，由于起始的if语句中确定了插入key值是要比当前节点小的，所以只可能三连节点符合——左——右——的形式，通过先左后右即可实现相应调整(三连节点始终可能不包括含key节点)
                else:
                    node = self.left_right_rotate(node)
        # 完全对偶。当key大于当前节点存储数据时
        elif key > node.data:
            # 递归向下时，还未插入。缩小成子问题
            # 如果比目标节点大，说明应该插入右侧
            node.right = self._insert(key, node.right)
            # 以下与上完全同理。递归子问题已解决，递归向上检查结果时执行下列语句，不再赘述。
            if (self.height(node.right) - self.height(node.left)) == 2:
                if key > node.right.data:
                    node = self.right_right_rotate(node)
                else:
                    node = self.left_right_rotate(node)
        # 递归更新树高
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        # 返回插入后树的根节点。很可能与输入的node不一样。
        return node

    # 完全平衡树的先序遍历与一般二叉树完全相同,不再赘述。
    def preOrderTraverse(self, node):
        if node is not None:
            print(node.data)
            self.preOrderTraverse(node.left)
            self.preOrderTraverse(node.right)


# avl树实现完成。如下检验
# 输入一个数组作为要建立树的每一个节点应该存储的元素
n = list(map(int, input().split()))
# 建avl树实例
avl = AVLTree()
# 逐一向建立的平衡二叉树中插入列表元素
for i in range(len(n)):
    avl.insert(n[i])
# 先序遍历二叉平衡树
avl.preOrderTraverse(avl.root)
