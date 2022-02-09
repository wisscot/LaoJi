# 第四章 二叉树中的分治法与遍历法

在这一章节的学习中，我们将要学习一个数据结构——二叉树（Binary Tree），和基于二叉树上的搜索算法。

在二叉树的搜索中，我们主要使用了分治法（Divide Conquer）来解决大部分的问题。之所以大部分二叉树的问题可以使用分治法，是因为二叉树这种数据结构，是一个天然就帮你做好了分治法中“分”这个步骤的结构。

本章节的先修内容有：

* 什么是递归（Recursion）—— 请回到第二章节中复习
* 递归（Recursion）、回溯（Backtracking）和搜索（Search）的联系和区别
* 分治法（Divide and Conquer）和遍历法（Traverse）的联系和区别
* 什么是结果类 ResultType，什么时候使用 ResultType
* 什么是二叉查找树（Binary Search Tree）
* 什么是平衡二叉树（Balanced Binary Tree）

本章节的补充内容有：

* Morris 算法：使用 O(1) 的额外空间复杂度对二叉树进行先序遍历（Preorder Traversal）
* 用非递归的方法实现先序遍历，中序遍历和后序遍历
* 二叉查找树（Binary Search Tree）的增删查改
* Java 自带的平衡排序二叉树 TreeMap / TreeSet 的介绍和面试中的应用


<br></br>
## 二叉树上的遍历法

__定义__

遍历（Traversal），顾名思义，就是通过某种顺序，一个一个访问一个数据结构中的元素。比如我们如果需要遍历一个数组，无非就是要么从前往后，要么从后往前遍历。但是对于一棵二叉树来说，他就有很多种方式进行遍历：

* 层序遍历（Level order）
* 先序遍历（Pre order）
* 中序遍历（In order）
* 后序遍历（Post order）

我们在之前的课程中，已经学习过了二叉树的层序遍历，也就是使用 BFS 算法来获得二叉树的分层信息。通过 BFS 获得的顺序我们也可以称之为 BFS Order。而剩下的三种遍历，都需要通过深度优先搜索的方式来获得。而这一小节中，我们将讲一下通过深度优先搜索（DFS）来获得的节点顺序，

__先序遍历 / 中序遍历 / 后序遍历__

先序遍历（又叫先根遍历、前序遍历）
首先访问根结点，然后遍历左子树，最后遍历右子树。遍历左、右子树时，仍按先序遍历。若二叉树为空则返回。

该过程可简记为根左右，注意该过程是递归的。

```python
# 将根作为root，空list作为result传入，即可得到整棵树的遍历结果
def traverse(root, result):
    if not root:
        return
    result.append(root.val)
    traverse(root.left, result)
    traverse(root.right, result)
```

__中序遍历（又叫中根遍历）__

首先遍历左子树，然后访问根结点，最后遍历右子树。遍历左、右子树时，仍按中序遍历。若二叉树为空则返回。简记为左根右。

```python
def traverse(root, result):
    if not root:
        return
    traverse(root.left, result)
    result.append(root.val) # 注意访问根节点放到了遍历左子树的后面
    traverse(root.right, result)
```

__后序遍历（又叫后根遍历）__

首先遍历左子树，然后遍历右子树，最后访问根结点。遍历左、右子树时，仍按后序遍历。若二叉树为空则返回。简记为左右根。

```python
def traverse(root, result):
    if not root:
        return
    traverse(root.left, result)
    traverse(root.right, result)
    result.append(root.val) # 注意访问根节点放到了最后
```

一些有趣的题目：

http://www.lintcode.com/problem/construct-binary-tree-from-inorder-and-postorder-traversal/

http://www.lintcode.com/problem/construct-binary-tree-from-preorder-and-inorder-traversal/

<br></br>
## 二叉树上的分治法

__定义__

分治法（Divide & Conquer Algorithm）是说将一个大问题，拆分为2个或者多个小问题，当小问题得到结果之后，合并他们的结果来得到大问题的结果。

举一个例子，比如中国要进行人口统计。那么如果使用遍历（Traversal）的办法，做法如下：

>人口普查员小张自己一个人带着一个本子，跑遍全中国挨家挨户的敲门查户口

而如果使用分治法，做法如下：

1. 国家统计局的老板小李想要知道全国人口的总数，于是他找来全国各个省的统计局领导，下派人口普查任务给他们，让他们各自去统计自己省的人口总数。在小李这儿，他只需要最后将各个省汇报的人口总数结果累加起来，就得到了全国人口的数目。
2. 然后每个省的领导，又找来省里各个市的领导，让各个市去做人口统计。
3. 市找县，县找镇，镇找乡。最后乡里的干部小王挨家挨户敲门去查户口。

在这里，把全国的任务拆分为省级的任务的过程，就是分治法中分的这个步骤。把各个小任务派发给别人去完成的过程，就是分治法中治的这个步骤。但是事实上我们还有第三个步骤，就是将小任务的结果合并到一起的过程，合这个步骤。因此如果我来取名字的话，我会叫这个算法：分治合算法。

__为什么二叉树的问题适合使用分治法？__

在一棵二叉树（Binary Tree）中，如果将整棵二叉树看做一个大问题的话，那么根节点（Root）的左子树（Left subtree）就是一个小问题，右子树（Right subtree）是另外一个小问题。这是一个天然就帮你完成了“分”这个步骤的数据结构。

<br></br>
## 遍历法和分治法实战

---
### 二叉树最大深度

https://1256418761.vod2.myqcloud.com/c8e8a510vodtransgzp1256418761/d82304627447398156689899420/v.f30.mp4

---
### 判断平衡二叉树

https://1256418761.vod2.myqcloud.com/c8e8a510vodtransgzp1256418761/325f719b7447398156687377316/v.f30.mp4

---
### 判断二叉搜索树

https://1256418761.vod2.myqcloud.com/c8e8a510vodtransgzp1256418761/d5950abd7447398156774419468/v.f40.mp4

<br></br>
## 递归，分治法，遍历法的联系与区别

__联系__

分治法（Divide & Conquer）与遍历法（Traverse）是两种常见的递归（Recursion）方法。

__分治法解决问题的思路__

先让左右子树去解决同样的问题，然后得到结果之后，再整合为整棵树的结果。

__遍历法解决问题的思路__

通过前序/中序/后序的某种遍历，游走整棵树，通过一个全局变量或者传递的参数来记录这个过程中所遇到的点和需要计算的结果。

__两种方法的区别__

从程序实现角度分治法的递归函数，通常有一个返回值，遍历法通常没有。

<br></br>
## 递归、回溯和搜索

__什么是递归 (Recursion) ？__

很多书上会把递归（Recursion）当作一种算法。事实上，递归是包含两个层面的意思的：

1. 一种由大化小，由小化无的解决问题的算法。类似的算法还有动态规划（Dynamic Programming）。
2. 一种程序的实现方式。这种方式就是一个函数（Function / Method / Procedure）自己调用自己。

与之对应的，是迭代法（Iteration）。

__什么是搜索 (Search)？__

搜索分为深度优先搜索（Depth First Search）和宽度优先搜索（Breadth First Search），通常分别简写为 DFS 和 BFS。搜索是一种类似于枚举（Enumerate）的算法。比如我们需要找到一个数组里的最大值，我们可以采用枚举法，因为我们知道数组的范围和大小，比如经典的打擂台算法：

```python
max_num = nums[0]
for i in range(1, len(nums)):
    max_num = max(max_num, nums[i])
```

枚举法通常是你知道循环的范围，然后可以用几重循环就搞定的算法。比如我需要找到 所有 x^2 + y^2 = K 的整数组合，可以用两重循环的枚举法：

```python
for x in range(1, k+1):
    for y in range(1, k+1):
        if x*x + y*y == k:
            # print x and y
```

而有的问题，比如求 N 个数的全排列，你可能需要用 N 重循环才能解决。这个时候，我们就倾向于采用递归的方式去实现这个变化的 N 重循环。这个时候，我们就把算法称之为搜索。因为你已经不能明确的写出一个不依赖于输入数据的多重循环了。

通常来说 DFS 我们会采用递归的方式实现（当然你强行写一个非递归的版本也是可以的），而 BFS 则无需递归（使用队列 Queue + 哈希表 HashMap就可以）。

__所以我们在面试中，如果一个问题既可以使用 DFS，又可以使用 BFS 的情况下，一定要优先使用 BFS。因为他是非递归的，而且更容易实现。__

__什么是回溯(Backtracking)？__

有的时候，深度优先搜索算法（DFS），又被称之为回溯法，所以你可以完全认为回溯法，就是深度优先搜索算法。在我的理解中，回溯实际上是深度优先搜索过程中的一个步骤。比如我们在进行全子集问题的搜索时，假如当前的集合是 {1,2} 代表我正在寻找以 {1,2}开头的所有集合。那么他的下一步，会去寻找 {1,2,3}开头的所有集合，然后当我们找完所有以 {1,2,3} 开头的集合时，我们需要把 3 从集合中删掉，回到 {1,2}。然后再把 4 放进去，寻找以 {1,2,4} 开头的所有集合。这个把 3 删掉回到 {1,2} 的过程，就是回溯。

```python
subset.add(nums[i])
subsetsHelper(result, subset, nums, i + 1)
subset.remove(len(list) - 1)
```

详情请参考：
http://www.jiuzhang.com/solutions/subsets/

<br></br>
## 递归三要素

我们以《二叉树的最大深度》和《二叉树的前序遍历》两个题目为例子，来分析一下递归的三要素。

相关题目链接：

http://www.lintcode.com/problem/maximum-depth-of-binary-tree/

http://www.lintcode.com/problem/binary-tree-preorder-traversal/

递归的定义
>每一个递归函数，都需要有明确的定义，有了正确的定义以后，才能够对递归进行拆解。

递归的拆解
>一个大问题如何拆解为若干个小问题去解决。

递归的出口
>什么时候可以直接知道答案，不用再拆解，直接 return

<br></br>
## 什么是二叉搜索树

__定义__

二叉搜索树（Binary Search Tree，又名排序二叉树，二叉查找树，通常简写为BST）定义如下：
空树或是具有下列性质的二叉树：
1. 若左子树不空，则左子树上所有节点值均小于或等于它的根节点值；
2. 若右子树不空，则右子树上所有节点值均大于根节点值；
3. 左、右子树也为二叉搜索树；

__BST 的特性__

* 按照中序遍历（inorder traversal）打印各节点，会得到由小到大的顺序。
* 在BST中搜索某值的平均情况下复杂度为O(logN)，最坏情况下复杂度为O(N)，其中N为节点个数。将待寻值与节点值比较，若不相等，则 __通过是小于还是大于，可断定该值只可能在左子树还是右子树，继续向该子树搜索__ 。
* 在balanced BST中查找某值的时间复杂度为O(logN)。

__BST 的作用__

* 通过中序遍历，可快速得到升序节点列表。
* 在BST中查找元素，平均情况下时间复杂度是O(logN)；插入新节点，保持BST特性平均情况下要耗时O（logN）。（参考链接）。
* 和有序数组的对比：有序数组查找某元素可以用二分法，时间复杂度是O（logN）；但是插入新元素，维护数组有序性要耗时O（N）。

常见的BST面试题
http://www.lintcode.com/en/tag/binary-search-tree/

BST是一种重要且基本的结构，其相关题目也十分经典，并延伸出很多算法。
在BST之上，有许多高级且有趣的变种,以解决各式各样的问题，例如:

* 用于数据库或各语言标准库中索引的红黑树
* 提升二叉树性能底线的伸展树
* 优化红黑树的AA树
* 随机插入的树堆
* 机器学习kNN算法的高维快速搜索k-d树
* …………

<br></br>
## 什么是平衡二叉搜索树

__定义__

平衡二叉搜索树（Balanced Binary Search Tree，又称为AVL树，有别于AVL算法）是二叉树中的一种特殊的形态。二叉树当且仅当满足如下两个条件之一，是平衡二叉树：

* 空树。
* 左右子树高度差绝对值不超过1且左右子树都是平衡二叉树。

__AVL树的高度为 O(logN)__

AVL树有什么用？
最大作用是保证查找的最坏时间复杂度为O(logN)。而且较浅的树对插入和删除等操作也更快。

AVL树的相关练习题
判断一棵树是否为平衡树
http://www.lintcode.com/problem/balanced-binary-tree/

提示：可以自下而上递归判断每个节点是否平衡。若平衡将当前节点高度返回，供父节点判断;否则该树一定不平衡。


<br></br>
## 第四章课后补充内容

二叉树相关有一些内容，如果学有余力可以掌握一下，可以提升自信心（因为知道了别人不知道的东西），更有底气去面试（虽然考到的概率很低）：

1. 用 Morris 算法实现 O(1) 额外空间对二叉树进行先序遍历
2. 用非递归（Non-recursion / Iteration）的方式实现二叉树的前序遍历，中序遍历和后序遍历
3. BST 的增删查改
4. 平衡排序二叉树（Balanced Binary Search Tree）及 TreeSet / TreeMap 的使用

---
### 非递归的方式实现二叉树遍历

先序遍历

__思路__

遍历顺序为根、左、右

1. 如果根节点非空，将根节点加入到栈中。
2. 如果栈不空，弹出出栈顶节点，将其值加加入到数组中。
    * 如果该节点的右子树不为空，将右子节点加入栈中。
    * 如果左子节点不为空，将左子节点加入栈中。
3. 重复第二步，直到栈空。

__代码实现__

```python
class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        stack = []
        preorder = []

        if not root:
            return preorder

        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return preorder
```
练习
http://www.lintcode.com/problem/binary-tree-preorder-traversal/

中序遍历

__思路__

遍历顺序为左、根、右

1. 如果根节点非空，将根节点加入到栈中。
2. 如果栈不空，取栈顶元素（暂时不弹出），
    * 如果左子树已访问过，或者左子树为空，则弹出栈顶节点，将其值加入数组，如有右子树，将右子节点加入栈中。
    * 如果左子树不为空，则将左子节点加入栈中。
3. 重复第二步，直到栈空。

__代码实现__
```python
class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        stack = []
        result = []

        while root:
            stack.append(root)
            root = root.left

        while len(stack) > 0:
            node = stack[-1]
            result.append(node.val)

            if not node.right:
                node = stack.pop()
                while len(stack) > 0 and stack[-1].right == node:
                    node = stack.pop()
            else:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
        
        return result
```

练习
http://www.lintcode.com/problem/binary-tree-inorder-traversal/

后序遍历

__思路__

遍历顺序为左、右、根

1. 如果根节点非空，将根节点加入到栈中。
2. 如果栈不空，取栈顶元素（暂时不弹出），
    * 如果（左子树已访问过或者左子树为空），且（右子树已访问过或右子树为空），则弹出栈顶节点，将其值加入数组，
    * 如果左子树不为空，切未访问过，则将左子节点加入栈中，并标左子树已访问过。
    * 如果右子树不为空，切未访问过，则将右子节点加入栈中，并标右子树已访问过。
3. 重复第二步，直到栈空。

__代码实现__

```python
class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        result = []
        stack = []
        prev, curr = None, root

        if not root:
            return result

        stack.append(root)
        while len(stack) > 0:
            curr = stack[-1]
            if not prev or prev.left == curr or prev.right == curr:  # traverse down the tree
                if curr.left:
                    stack.append(curr.left)
                elif curr.right:
                    stack.append(curr.right)
            elif curr.left == prev:  # traverse up the tree from the left
                if curr.right:
                    stack.append(curr.right)
            else:  # traverse up the tree from the right
                result.append(curr.val)
                stack.pop()
            prev = curr

        return result
```
练习
http://www.lintcode.com/problem/binary-tree-postorder-traversal/

---
### 用 Morris 算法实现 O(1) 额外空间遍历二叉树

__什么是 Morris 算法__

与递归和使用栈空间遍历的思想不同，Morris 算法使用二叉树中的叶节点的right指针来保存后面将要访问的节点的信息，当这个right指针使用完成之后，再将它置为null，但是在访问过程中有些节点会访问两次，所以与递归的空间换时间的思路不同，Morris则是使用时间换空间的思想。

#### 用 Morris 算法进行中序遍历(Inorder Traversal)

__思路__

1. 如果当前节点的左孩子为空，则输出当前节点并将其右孩子作为当前节点。
2. 如果当前节点的左孩子不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点。
    * 如果前驱节点的右孩子为空，将它的右孩子设置为当前节点。当前节点更新为当前节点的左孩子。
    * 如果前驱节点的右孩子为当前节点，将它的右孩子重新设为空（恢复树的形状）。输出当前节点。当前节点更新为当前节点的右孩子。
3. 重复1、2两步直到当前节点为空。

LintCode 练习
http://www.lintcode.com/problem/binary-tree-inorder-traversal/


#### 用 Morris 算法实现先序遍历(Preorder Traversal)

__思路__

1. 如果当前节点的左孩子为空，则输出当前节点并将其右孩子作为当前节点。
2. 如果当前节点的左孩子不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点。
    * 如果前驱节点的右孩子为空，将它的右孩子设置为当前节点。**输出当前节点**（与中序遍历唯一一点不同）。当前节点更新为当前节点的左孩子。
    * 如果前驱节点的右孩子为当前节点，将它的右孩子重新设为空。当前节点更新为当前节点的右孩子。
3. 重复1、2两步直到当前节点为空。

LintCode 练习
http://www.lintcode.com/problem/binary-tree-preorder-traversal/

#### 用 Morris 算法实现后序遍历(Postorder Traversal)

__思路__

* 后序遍历其实可以看作是和前序遍历左右对称的，此处，我们同样可以利用这个性质，基于前序遍历的算法，可以很快得到后序遍历的结果。我们只需要将前序遍历中所有的左孩子和右孩子进行交换就可以了。

LintCode 练习
http://www.lintcode.com/problem/binary-tree-postorder-traversal/

---
### BST 的增删查改

什么是二叉搜索树(Binary Search Tree)

二叉搜索树可以是一棵空树或者是一棵满足下列条件的二叉树:

* 如果它的左子树不空，则左子树上所有节点值均小于它的根节点值。
* 如果它的右子树不空，则右子树上所有节点值均大于它的根节点值。
* 它的左右子树均为二叉搜索树(BST)。
* 严格定义下BST中是没有值相等的节点的(No duplicate nodes)。
根据上述特性，我们可以得到一个结论：BST中序遍历得到的序列是升序的。如下述BST的中序序列为：[1,3,4,6,7,8,10,13,14]

BST基本操作——增删改查(CRUD)

__基本操作之查找(Retrieve)__

思路

* 查找值为val的节点，如果val小于根节点则在左子树中查找，反之在右子树中查找

实战

http://www.lintcode.com/en/problem/search-range-in-binary-search-tree/

http://www.lintcode.com/en/problem/two-sum-bst-edtion/

http://www.lintcode.com/en/problem/closest-binary-search-tree-value/

http://www.lintcode.com/en/problem/closest-binary-search-tree-value-ii/

http://www.lintcode.com/en/problem/trim-binary-search-tree/

http://www.lintcode.com/en/problem/bst-swapped-nodes/


__基本操作之修改(Update)__

思路

修改仅仅需要在查找到需要修改的节点之后，更新这个节点的值就可以了

实战

http://www.lintcode.com/en/problem/bst-swapped-nodes/

__基本操作之增加(Create)__

思路

* 根节点为空，则待添加的节点为根节点
* 如果待添加的节点值小于根节点，则在左子树中添加
* 如果待添加的节点值大于根节点，则在右子树中添加
* 我们统一在树的叶子节点(Leaf Node)后添加

实战

http://www.lintcode.com/en/problem/insert-node-in-a-binary-search-tree/

__基本操作之删除(Delete)__

思路(最为复杂)

* 考虑待删除的节点为叶子节点，可以直接删除并修改父亲节点(Parent Node)的指针，需要区分待删节点是否为根节点
* 考虑待删除的节点为单支节点(只有一棵子树——左子树 or 右子树)，与删除链表节点操作类似，同样的需要区分待删节点是否为根节点
* 考虑待删节点有两棵子树，可以将待删节点与左子树中的最大节点进行交换，由于左子树中的最大节点一定为叶子节点，所以这时再删除待删的节点可以参考第一条
* 详细的解释可以看 http://www.algolist.net/Data_structures/Binary_search_tree/Removal

实战

http://www.lintcode.com/en/problem/remove-node-in-binary-search-tree/
http://www.lintcode.com/en/problem/trim-binary-search-tree/

---
### 平衡排序二叉树(Self-balancing Binary Search Tree)

__定义__

平衡二叉搜索树又被称为AVL树（有别于AVL算法），且具有以下性质：

* 它是一棵空树或它的左右两个子树的高度差的绝对值不超过1
* 左右两棵子树都是一棵平衡二叉搜索树
* 平衡二叉搜索树必定是二叉搜索树，反之则不一定。

平衡排序二叉树 与 二叉搜索树 对比:

也许因为输入值不够随机，也许因为输入顺序的原因，还或许一些插入、删除操作，会使得二叉搜索树失去平衡，造成搜索效率低落的情况。

常用的实现办法
* AVL树 --> https://en.wikipedia.org/wiki/AVL_tree
* 红黑树(Red Black Tree) --> http://blog.csdn.net/v_july_v/article/details/6105630

__练习：链表转平衡排序二叉树__

LintCode 练习地址：
http://www.lintcode.com/en/problem/convert-sorted-list-to-balanced-bst/


* 粗暴的算法

    可以十分容易想到一个一个 O(nlogn) 的分治算法，以链表作为参数，二叉树作为返回值：

    算法的大致思路就是，找到链表中点和他前后的点，然后左边的部分递归生成一棵左子树，右边的部分递归生成一棵右子树，再和中间的点拼接起来就好了。

    这个算法我们不难发现他的时间复杂度是 O(nlogn) 的，因为找到中点的时间复杂度是 O(n)，因此可以用 T 函数推算法来进行推算：

    T(n) = 2 * T(n/2) + O(n) = O(nlogn)


* 优化的算法

    为了优化这个算法，我们给分治函数带上了一个参数 n 代表目前打算去转换 head 开始，长度为 n 那么多个节点，让其变为 Balanced Binary Tree。递归函数接口如下：
    ```python
    def convert(head, n):
    ```
    这样，我们不用真正把链表从 prev 和 mid 之间断开。可以利用对第二个参数的大小控制来让处理规模缩小。

    但是虽然我们可以很快的调用 convert(head, n / 2)，让链表的一半变成二叉树。但是如何很快知道链表的中点呢？这里的办法是，如果我们把 head 放在参数里，那么就无法利用 convert 函数对 head 进行挪动了，所以我们把 head 挪出来，放到全局，作为一个全局变量。

    这里我们在全局放了一个 current 指针，这个指针会指向当前还没有被变成 Tree 的下一个 List 上的节点。因此如果我们把左子树变成 Tree 以后，current 就要让他指向 List 上的下一个点，也就是中间的这个点了。

    算法有一些绕，建议使用几个小数据模拟整个算法的执行过程。
    完整参考程序见：
    http://www.jiuzhang.com/solution/convert-sorted-list-to-balanced-bst/

    完整算法描述如下：

    1. 首先求得整个list的长度 O(n)
    2. 利用 helper 函数进行递归，helper(head, len) 表示把从 head 开始的，长度为len的链表，转换为一个bst并且return。与此同时，把global variable的指针挪到head开始的第 len + 1个listnode上。

    那么 convert(head, len) 就可以分为，三个步骤：

    1. 把head开头的长度为 len/2的先变成bst，也就是我们的左子树，convert(head, len / 2)。这个时候他顺便会把global variable 挪到第len / 2 + 1的那个node，这个就是我们的root。
    2. 然后得到了root之后，把global variable 往下挪一个挪到 第 len/2 + 2个点，也就是右子树开头的那个点，然后调用 convert(global variable, len - len/2 -1)，构造出右子树。
    3. 然后把root，左子树，右子树，拼接在一起，return

    这个题算法框架就是这样，如果不是很明白的话，建议模拟一个小数据，比如 5个节点的情况。模拟几个数据结合算法的思路来分析，就应该可以明白。这个题的这种解法背下来就好了。