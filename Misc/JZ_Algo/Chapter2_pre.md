# 第二章 性价比之王的宽度优先搜索

在这一章节中，我们将学习一个一天就能够学会的，面试中又极高频会考到的知识点 —— 宽度优先搜索。英文全称 Breadth First Search，简称 BFS。

BFS是一个你必须掌握的算法，而且也很容易掌握，每个 BFS 的题目，程序写起来都差不多。因此是一个学习起来性价比极高的算法。

本章节的先修内容有
* 什么是队列，如何自己实现一个队列
* 什么是 Interface，LinkedList 和 Queue 之间的关系是什么？
* 什么是拓扑排序
* 如何定义一个图的数据结构

课后补充内容有：
* 宽度优先搜索（BFS）的另外两种实现方式
* 双向宽度优先搜索算法（Bidirectional BFS)

<br></br>
## 什么是队列（Queue）

队列（queue）是一种采用先进先出（FIFO，first in first out）策略的抽象数据结构。比如生活中排队，总是按照先来的先服务，后来的后服务。队列在数据结构中举足轻重，其在算法中应用广泛，最常用的就是在宽度优先搜索(BFS）中，记录待扩展的节点。

队列内部存储元素的方式，一般有两种，数组（array）和链表（linked list）。两者的最主要区别是：

* 数组对随机访问有较好性能。
* 链表对插入和删除元素有较好性能。

在各语言的标准库中：

* Java常用的队列包括如下几种：
  * ArrayDeque：数组存储。实现Deque接口，而Deque是Queue接口的子接口，代表双端队列（double-ended queue）。
  * LinkedList：链表存储。实现List接口和Duque接口，不仅可做队列，还可以作为双端队列，或栈（stack）来使用。
* C++中，使用<queue>中的queue模板类，模板需两个参数，元素类型和容器类型，元素类型必要，而容器类型可选，默认deque，可改用list（链表）类型。
* Python中，使用collections.deque，双端队列。

如何自己用数组实现一个队列？

队列的主要操作有：

* add()队尾追加元素
* poll()弹出队首元素
* size()返回队列长度
* empty()判断队列为空

```python
class MyQueue:
    # 队列初始化
    def __init__(self):
        self.elements = []  # 用list存储队列元素
        self.pointer = 0    # 队头位置

    # 获取队列中元素个数
    def size(self):
        return len(self.elements)-pointer
    
    # 判断队列是否为空
    def empty(self):
        return self.size() == 0

    # 在队尾添加一个元素
    def add(self, e):
        self.elements.append(e)

    # 弹出队首元素，如果为空则返回None
    def poll(self):
        if self.empty():
            return None
        pointer += 1
        return self.elements[pointer-1]
```

队列在工业界的应用
队列可用于实现消息队列（message queue），以完成异步（asynchronous）任务。

“消息”是计算机间传送的数据，可以只包含文本；也可复杂到包含嵌入对象。当消息“生产”和“消费”的速度不一致时，就需要消息队列，临时保存那些已经发送而并未接收的消息。例如集体打包调度，服务器繁忙时的任务处理，事件驱动等等。

常用的消息队列实现包括RabbitMQ，ZeroMQ等等。

更多消息队列的参考资料：

[为什么需要消息队列，及使用消息队列的好处？](https://blog.csdn.net/qq_39470733/article/details/80576013)

[RabbitMQ的应用场景以及基本原理介绍](http://blog.csdn.net/whoamiyang/article/details/54954780)


<br></br>
## 什么时候使用宽搜

如下的一些场景是使用宽度优先搜索的常见场景：

__图的遍历 Traversal in Graph__

图的遍历，比如给出无向连通图(Undirected Connected Graph)中的一个点，找到这个图里的所有点。这就是一个常见的场景。LintCode 上的 [Clone Graph](http://www.lintcode.com/problem/clone-graph) 就是一个典型的练习题。

更细一点的划分的话，这一类的问题还可以分为：

* 层级遍历 Level Order Traversal
* 由点及面 Connected Component
* 拓扑排序 Topological Sorting

层级遍历，也就是说我不仅仅需要知道从一个点出发可以到达哪些点，还需要知道这些点，分别离出发点是第几层遇到的，比如 [Binary Tree Level Order Traversal](http://www.lintcode.com/problem/binary-tree-level-order-traversal/) 就是一个典型的练习题。

由点及面，前面已经提到。

拓扑排序，让我们在后一节中展开描述。

__最短路径 Shortest Path in Simple Graph__

最短路径算法有很多种，BFS 是其中一种，但是他有特殊的使用场景，即必须是在简单图中求最短路径。

大部分简单图中使用 BFS 算法时，都是无向图。当然也有可能是有向图，但是在面试中极少会出现。

__什么是简单图（Simple Graph）？__

即，图中每条边长度都是1（或边长都相同）。



<br></br>
## 图上的宽度优先搜索

BFS 大部分的时候是在图上进行的。

__什么是图（Graph）__

图在离线数据中的表示方法为 <E, V>，E表示 Edge，V 表示 Vertex。也就是说，图是顶点（Vertex）和边（Edge）的集合。

图分为：

* 有向图（Directed Graph）
* 无向图（Undirected Graph）

BFS 在两种图上都适用。另外，树（Tree）也是一种特殊的图。

---
### 二叉树的BFS vs 图的BFS

二叉树中进行 BFS 和图中进行 BFS 最大的区别就是二叉树中无需使用 HashSet（C++: unordered_map, Python: dict) 来存储访问过的节点（丢进过 queue 里的节点）

因为二叉树这种数据结构，上下层关系分明，没有环（circle），所以不可能出现一个节点的儿子的儿子是自己的情况。
但是在图中，一个节点的邻居的邻居就可能是自己了。

---
### 如何定义一个图的数据结构？

有很多种方法可以存储一个图，最常用的莫过于：

1. 邻接矩阵
2. 邻接表

而邻接矩阵因为耗费空间过大，我们通常在工程中都是使用邻接表作为图的存储结构。

#### 邻接矩阵 Adjacency Matrix

```
[
  [1,0,0,1],
  [0,1,1,0],
  [0,1,1,0],
  [1,0,0,1]
]
```

例如上图表示0号点和3号点有连边。1号点和2号店有连边。
当然，每个点和自己也是默认有连边的。
图中的 0 表示不连通，1 表示连通。
我们也可以用一个更具体的整数值来表示连边的长度。

邻接矩阵我们可以直接用一个二维数组表示，如int[][] matrix;。这种数据结构因为耗费 O(n^2) 的空间，所以在稀疏图上浪费很大，因此并不常用。

#### 邻接表 (Adjacency List)

```
[
  [1],
  [0,2,3],
  [1],
  [1]
]
```

这个图表示 0 和 1 之间有连边，1 和 2 之间有连边，1 和 3 之间有连边。即每个点上存储自己有哪些邻居（有哪些连通的点）。
这种方式下，空间耗费和边数成正比，可以记做 O(m)，m代表边数。m最坏情况下虽然也是 O(n^2)，但是邻接表的存储方式大部分情况下会比邻接矩阵更省空间。

自定义邻接表
```python
def DirectedGraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = []  # a list of DirectedGraphNode's
		...
```

__使用 Map 和 Set（面试时）__

也可以使用 HashMap 和 HashSet 搭配的方式来存储邻接表

```python
# 假设nodes为节点标签的列表:

# 使用了Python中的dictionary comprehension语法
adjacency_list = {x:set() for x in nodes}

# 另一种写法
adjacency_list = {}
for x in nodes:
    adjacency_list[x] = set()
```

其中 T 代表节点类型。通常可能是整数(Integer)。

这种方式虽然没有上面的方式更加直观和容易理解，但是在面试中比较节约代码量。
而自定义的方法，更加工程化，所以在面试中如果时间不紧张题目不难的情况下，推荐使用自定义邻接表的方式。


<br></br>
## 拓扑排序

__定义__

在图论中，由一个有向无环图的顶点组成的序列，当且仅当满足下列条件时，称为该图的一个拓扑排序（英语：Topological sorting）。

* 每个顶点出现且只出现一次；
* 若A在序列中排在B的前面，则在图中不存在从B到A的路径。

也可以定义为：拓扑排序是对有向无环图的顶点的一种排序，它使得如果存在一条从顶点A到顶点B的路径，那么在排序中B出现在A的后面。

(来自 Wiki)

__实际运用__

拓扑排序 Topological Sorting 是一个经典的图论问题。他实际的运用中，拓扑排序可以做如下的一些事情：

* 检测编译时的循环依赖
* 制定有依赖关系的任务的执行顺序

__拓扑排序不是一种排序算法__

虽然名字里有 Sorting，但是相比起我们熟知的 Bubble Sort, Quick Sort 等算法，Topological Sorting 并不是一种严格意义上的 Sorting Algorithm。

确切的说，__一张图的拓扑序列可以有很多个，也可能没有。__ 拓扑排序只需要找到其中 __一个__ 序列，无需找到 __所有__ 序列。

---
### 算法描述

__入度与出度__

在介绍算法之前，我们先介绍图论中的一个基本概念，入度和出度，英文为 in-degree & out-degree。

在有向图中，如果存在一条有向边 A-->B，那么我们认为这条边为 A 增加了一个出度，为 B 增加了一个入度。

__算法流程__

拓扑排序的算法是典型的宽度优先搜索算法，其大致流程如下：

1. 统计所有点的入度，并初始化拓扑序列为空。
2. 将所有入度为 0 的点，也就是那些没有任何依赖的点，放到宽度优先搜索的队列中
3. 将队列中的点一个一个的释放出来，放到拓扑序列中，每次释放出某个点 A 的时候，就访问 A 的相邻点（所有A指向的点），并把这些点的入度减去 1。
4. 如果发现某个点的入度被减去 1 之后变成了 0，则放入队列中。
5. 直到队列为空时，算法结束，

__深度优先搜索的拓扑排序__

深度优先搜索也可以做拓扑排序，不过因为不容易理解，也并不推荐作为拓扑排序的主流算法。

参考程序

这是 LintCode 上的题目：[Topological Sorting](http://www.lintcode.com/problem/topological-sorting/)




<br></br>
## 宽度优先搜索的模板

宽度优先搜索有很多种实现方法，这里为了大家记忆方便和教学的方便，我们只介绍最实用的一种方法，即使用一个队列的方法。
这种方法也根据 BFS 时的需求不同，有两个版本，即需要分层遍历的版本和不需要分层遍历的版本。

__什么时候需要分层遍历？__

1. 如果问题需要你区分开不同层级的结果信息，如 二叉树的分层遍历 [Binary Tree Level Order Traversal](http://www.lintcode.com/problem/binary-tree-level-order-traversal/)
2. 简单图最短路径问题，如 单词接龙 [Word Ladder](http://www.lintcode.com/problem/word-ladder/)

---
### 无需分层遍历的宽度优先搜索

```python
from collections import deque

queue = deque()
seen = set()  #等价于Java版本中的set

seen.add(start)
queue.append(start)
while len(queue):
    head = queue.popleft()
    for neighbor in head.neighbors:
        if neighbor not in seen:
            seen.add(neighbor)
            queue.append(neighbor)
```

上述代码中：

* neighbor 表示从某个点 head 出发，可以走到的下一层的节点。
* set/seen 存储已经访问过的节点（已经丢到 queue 里去过的节点）
* queue 存储等待被拓展到下一层的节点
* set/seen 与 queue 是一对好基友，无时无刻都一起出现，往 queue 里新增一个节点，就要同时丢到 set 里。

---
### 需要分层遍历的宽度搜先搜索

```python
from collections import deque

queue = deque()
seen = set()

seen.add(start)
queue.append(start)
while len(queue):
    size = len(queue)
    for _ in range(size):
        head = queue.popleft()
        for neighbor in head.neighbors:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
```

上述代码中：

* size = queue.size() 是一个必须的步骤。如果在 for 循环中使用 for (int i = 0; i < queue.size(); i++) 会出错，因为 queue.size() 是一个动态变化的值。所以必须先把当前层一共有多少个节点存在局部变量 size 中，才不会把下一层的节点也在当前层进行扩展。


<br></br>
## 课后补充内容

除了模板中介绍的这种 BFS 的最佳实践以外，还有两种实现方法也很常见：

1. 两个队列来回迭代，来代表相邻的层级。
2. 使用 dummy node 来间隔不同的层级。

---
### 使用两个队列的BFS实现

我们可以将当前层的所有节点存在第一个队列中，然后拓展（Extend）出的下一层节点存在另外一个队列中。来回迭代，逐层展开。

参考代码如下：

```python
from collections import deque 

queue1, queue2 = deque(), deque()
seen = set()

seen.add(start)
queue1.append(start)
currentLevel = 0
while len(queue1):
    size = len(queue1)
    for _ in range(size):
        head = queue1.popleft()
        for neighbor in head.neighbors:
            if neighbor not in seen:
                seen.add(neighbor)
                queue2.append(neighbor)
    queue1, queue2 = queue2, queue1
    queue2.clear()
    currentLevel += 1
```

---
### 使用 Dummy Node 进行 BFS

__什么是 Dummy Node__

Dummy Node，翻译为哨兵节点。Dummy Node 一般本身不存储任何实际有意义的值，通常用作"占位"，或者链表的“虚拟头”。
如很多的链表问题中，我们会在原来的头head的前面新增一个节点，这个节点没有任何值，但是 next 指向 head。这样就会方便对 head 进行删除或者在前面插入等操作。
```
head->node->node->node ...
=>
dummy->head->node->node->node...
```

__Dummy Node 在 BFS 中如何使用__

在 BFS 中，我们主要用 dummy node 来做占位符。即，在队列中每一层节点的结尾，都放一个 null（or None in Python，nil in Ruby），来表示这一层的遍历结束了。这里 dummy node 就是一个 null。
```python
from collections import deque

queue = deque()
seen = set()

seen.add(start)
queue.append(start)
queue.append(None)
currentLevel = 0
while len(queue) > 1:
    head = queue.popleft()
    if head == None:
        currentLevel += 1
        queue.append(None)
        continue
    for neighbor in head.neighbors:
        if neighbor not in seen:
            seen.add(neighbor)
            queue.append(neighbor)
```

---
### 双向宽度优先搜索算法

双向宽度优先搜索 (Bidirectional BFS) 算法适用于如下的场景：

1. 无向图
2. 所有边的长度都为 1 或者长度都一样
3. 同时给出了起点和终点

以上 3 个条件都满足的时候，可以使用双向宽度优先搜索来求出起点和终点的最短距离。

__算法描述__

双向宽度优先搜索本质上还是BFS，只不过变成了起点向终点和终点向起点同时进行扩展，直至两个方向上出现同一个子节点，搜索结束。我们还是可以利用队列来实现：一个队列保存从起点开始搜索的状态，另一个保存从终点开始的状态，两边如果相交了，那么搜索结束。起点到终点的最短距离即为起点到相交节点的距离与终点到相交节点的距离之和。

Q.双向BFS是否真的能提高效率？

假设单向BFS需要搜索 N 层才能到达终点，每层的判断量为 X，那么总的运算量为 X ^ N. 如果换成是双向BFS，前后各自需要搜索 N / 2 层，总运算量为 2 * X ^ (N/2)。如果 N 比较大且X 不为 1，则运算量相较于单向BFS可以大大减少，差不多可以减少到原来规模的根号的量级。

参考代码
```python
from collections import deque

def doubleBFS(start, end):
    if start == end:
        return 1

    # 分别从起点和终点开始的两个BFS队列
    startQueue, endQueue = deque(), deque()
    startQueue.append(start)
    endQueue.append(end)
    step = 0

    # 从起点开始和从终点开始分别访问过的节点集合
    startVisited, endVisited = set(), set()
    startVisited.add(start)
    endVisited.add(end)
    while len(startQueue) and len(endQueue):
        startSize, endSize = len(startQueue), len(endQueue)
        #　按层遍历
        step += 1
        for _ in range(startSize):
            cur = startQueue.popleft()
            for neighbor in cur.neighbors:
                if neighbor in startVisited: # 重复节点
                    continue
                elif neighbor in endVisited: # 相交
                    return step
                else:
                    startVisited.add(neighbor)
                    startQueue.append(neighbor)
        step += 1
        for _ in range(endSize):
            cur = endQueue.popleft()
            for neighbor in cur.neighbors:
                if neighbor in endVisited:
                    continue
                elif neighbor in startVisited:
                    return step
                else:
                    endVisited.add(neighbor)
                    endQueue.append(neighbor)
    
    return -1
```

学习建议

Bidirectional BFS 掌握起来并不是很难，算法实现上稍微复杂了一点（代码量相对单向 BFS 翻倍），掌握这个算法一方面加深对普通 BFS 的熟练程度，另外一方面，基本上写一次就能记住，如果在面试中被问到了如何优化 BFS 的问题，Bidirectional BFS 几乎就是标准答案了。

参考资料

https://www.geeksforgeeks.org/bidirectional-search

应用例题

[Shortest Path in Undirected Graph](http://www.lintcode.com/zh-cn/problem/shortest-path-in-undirected-graph/)

[Knight Shortest Path](http://www.lintcode.com/zh-cn/problem/knight-shortest-path/)

[Knight Shortest Path II](http://www.lintcode.com/en/problem/knight-shortest-path-ii/)