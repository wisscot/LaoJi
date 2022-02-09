# 第五章 不是算法的算法 —— 两根指针

本章节的先修内容有：

* 什么是同向双指针，有哪些基本的同向双指针面试题？
* 什么是相向双指针，有哪些基本的相向双指针面试题？
* 最基本的两数之和问题
* 快速排序算法
* 归并排序算法
* 快速选择算法

课后补充内容：

* 三指针算法
* 烙饼排序 Pancake Sort

<br></br>
## 相向双指针
相向双指针，指的是在算法的一开始，两根指针分别位于数组/字符串的两端，并相向行走。如我们在小学的时候经常遇到的问题：

>小明和小红分别在铁轨A站和B站相向而行，小红的速度为 1m/s, 小明的速度为 2m/s，A站和B站相距 1km。
请问 ... 他们什么时候被火车撞死？（逃

一个典型的相向双指针问题就是翻转字符串的问题。在第二节课中我们学到的三步翻转法，就是一个典型的例子。

---
### 判断回文串

另外一个双指针的经典练习题，就是回文串的判断问题。给一个字符串，判断这个字符串是不是回文串。

我们可以用双指针的算法轻易的解决：

Follow up 1: 不区分大小写，忽略非英文字母
完整的题目描述请见：
http://www.lintcode.com/problem/valid-palindrome/

Follow up 2: 允许删掉一个字母（类似的，允许插入一个字母）
完整的题目描述请见：
http://www.lintcode.com/problem/valid-palindrome-ii/

FLAG 的面经中出现过此题。一个简单直观的粗暴想法是，既然要删除一个字母，那么我们就 for 循环枚举（Enumerate）每个字母，试试看删掉这个字母之后，该字符串是否为一个回文串。

上述粗暴算法的时间复杂度是 O(n^2)，因为 for 循环枚举被删除字母的复杂度为 O(n)，判断剩余字符构成的字符串是否为回文串的复杂度为 O(n)，总共花费 O(n^2)。这显然一猜就应该不符合面试官的要求。

正确的算法如下：

1. 依然用相向双指针的方式从两头出发，两根指针设为 L 和 R。
2. 如果 s[L] 和 s[R] 相同的话，L++, R--
3. 如果 s[L] 和 s[R] 不同的话，停下来，此时可以证明，如果能够通过删除一个字符使得整个字符串变成回文串的话，那么一定要么是 s[L]，要么是 s[R]。

简单的来说，这个算法就是依然按照原来的算法走一遍，然后碰到不一样的字符的时候，从总选一个删除，如果删除之后的字符换可以是 Palindrome 那就可以，都不行的话，那就不行。

---
### 双指针的鼻祖：两数之和

题目描述

给一个整数数组，找到两个数使得他们的和等于一个给定的数 target。
返回这两个数。
http://www.lintcode.com/problem/two-sum/

* 使用哈希表来解决
* 使用双指针算法来解决

两个算法的对比

1. Hash方法使用一个Hashmap结构来记录对应的数字是否出现，以及其下标。时间复杂度为O(n)。空间上需要开辟Hashmap来存储, 空间复杂度是O(n)。

2. Two pointers方法，基于有序数组的特性，不断移动左右指针，减少不必要的遍历，时间复杂度为O(nlogn)， 主要是排序的复杂度。但是在空间上，不需要额外空间，因此额外空间复杂度是 O(1)

参考资料
[lintcode Two pointers 算法题目汇总](http://blog.csdn.net/luoshengkim/article/details/52175440)


<br></br>
## 同向双指针

同向双指针的问题，是指两根指针都从头出发，朝着同一个方向前进。我们通过下面 5 个题目来初步认识同向双指针：

1. 数组去重问题 Remove duplicates in an array
2. 滑动窗口问题 Window Sum
3. 两数之差问题 Two Difference
4. 链表中点问题 Middle of Linked List
5. 带环链表问题 Linked List Cycle

---
### 数组去重问题

问题描述

给你一个数组，要求去除重复的元素后，将不重复的元素挪到数组前段，并返回不重复的元素个数。

LintCode 练习地址：http://www.lintcode.com/problem/remove-duplicate-numbers-in-array/

问题分析
这个问题有两种做法，第一种做法比较容易想到的是，把所有的数扔到 hash 表里，然后就能找到不同的整数有哪些。但是这种做法会耗费额外空间 O(n)O(n)。面试官会追问，如何不耗费额外空间。

此时我们需要用到双指针算法，首先将数组排序，这样那些重复的整数就会被挤在一起。然后用两根指针，一根指针走得快一些遍历整个数组，另外一根指针，一直指向当前不重复部分的最后一个数。快指针发现一个和慢指针指向的数不同的数之后，就可以把这个数丢到慢指针的后面一个位置，并把慢指针++。

---
### 滑动窗口问题

问题描述

求出一个数组每 kk 个连续整数的和的数组。如 nums = [1,2,3,4], k = 2 的话，window sum 数组为 [3,5,7]。
http://www.lintcode.com/problem/window-sum/

问题分析

这个问题并没有什么难度，但是如果你过于暴力的用户 O(n * k) 的算法去做是并不合适的。比如当前的 window 是 |1,2|,3,4。那么当 window 从左往右移动到 1,|2,3|,4 的时候，整个 window 内的整数和是增加了3，减少了1。因此只需要模拟整个窗口在滑动的过程中，整数一进一出的变化即可。这就是滑动窗口问题。

滑动窗口类的其他问题

以下两个高频的滑动窗口类问题我们在《九章算法强化班》中会讲解：

http://www.lintcode.com/problem/sliding-window-median/
http://www.lintcode.com/problem/sliding-window-maximum/

在 LintCode 中直接搜索 sliding window 能找到所有和 sliding window 相关的练习题。

---
### 两数之差问题

问题描述

在一个数组中，求出满足两个数之差等于 target 的那一对数。返回他们的下标。

LintCode 练习地址：
http://www.lintcode.com/problem/two-sum-difference-equals-to-target/

问题分析

作为两数之和的一个 Follow up 问题，在两数之和被问烂了以后，两数之差是经常出现的一个面试问题。
我们可以先尝试一下两数之和的方法，发现并不奏效，因为即便在数组已经排好序的前提下，nums[i] - nums[j] 与 target 之间的关系并不能决定我们淘汰掉 nums[i] 或者 nums[j]。

那么我们尝试一下将两根指针同向前进而不是相向而行，在 i 指针指向 nums[i] 的时候，j 指针指向第一个使得 nums[j] - nums[i] >= |target| 的下标 j：

1. 如果 nums[j] - nums[i] == |target|，那么就找到答案
2. 否则的话，我们就尝试挪动 i，让 i 向右挪动一位 => i++
3. 此时我们也同时将 j 向右挪动，直到 nums[j] - nums[i] >= |target|

可以知道，由于 j 的挪动不会从头开始，而是一直递增的往下挪动，那么这个时候，i 和 j 之间的两个循环的就不是累乘关系而是叠加关系。

相似问题

G家的一个相似问题：找到一个数组中有多少对二元组，他们的平方差 < target（target 为正整数）。

我们可以用类似放的方法来解决，首先将数组的每个数进行平方，那么问题就变成了有多少对两数之差 < target。

---
### 链表中点问题

__问题描述__

求一个链表的中点

LintCode 练习地址：http://www.lintcode.com/problem/middle-of-linked-list/

__问题分析__

这个问题可能大家会觉得，WTF 这么简单有什么好做的？你可能的想法是：

>先遍历一下整个链表，求出长度 L，然后再遍历一下链表找到第 L/2 的那个位置的节点。

但是在你抛出这个想法之后，面试官会追问你：如果只允许遍历链表一次怎么办？

可以看到这种 Follow up 并不是让你优化算法的时间复杂度，而是严格的限制了你遍历整个链表的次数。你可能会认为，这种优化有意义么？事实上是很有意义的。因为遍历一次这种场景，在真实的工程环境中会经常遇到，也就是我们常说的数据流问题（Data Stream Problem）。

__数据流问题 Data Stream Problem__

所谓的数据流问题，就是说，你需要设计一个在线系统，这个系统不断的接受一些数据，并维护这些数据的一些信息。比如这个问题就是在数据流中维护中点在哪儿。（维护中点的意思就是提供一个接口，来获取中点）

类似的一些数据流问题还有：

1. 数据流中位数 http://www.lintcode.com/problem/data-stream-median/
2. 数据流最大 K 项 http://www.lintcode.com/problem/top-k-largest-numbers-ii/
3. 数据流高频 K 项 http://www.lintcode.com/problem/top-k-frequent-words-ii/

这类问题的特点都是，你没有机会第二次遍历所有数据。上述问题部分将在《九章算法强化班》中讲解。

__用双指针算法解决链表中点问题__

我们可以使用双指针算法来解决链表中点的问题，更具体的，我们可以称之为 __快慢指针__ 算法。

在上面的程序中，我们将快指针放在第二个节点上，慢指针放在第一个节点上，while 循环中每一次快指针走两步，慢指针走一步。这样当快指针走到头的时候，慢指针就在中点了。

快慢指针的算法，在下一小节的“带环链表”中，也用到了。

---
### 带环链表问题

https://1256418761.vod2.myqcloud.com/c8e8a510vodtransgzp1256418761/d7e96d277447398156689863389/v.f30.mp4

<br></br>
## 两大经典排序算法

快速排序（Quick Sort）和归并排序（Merge Sort）是算法面试必修的两个基础知识点。很多的算法面试题，要么是直接问这两个算法，要么是这两个算法的变化，要么是用到了这两个算法中同样的思想或者实现方式，要么是挑出这两个算法中的某个步骤来考察。

本小节将从算法原理，实现，以及时间复杂度，空间复杂度、排序稳定性等方面的对比，让大家对这两个经典算法有一个更深入的理解和认识。

---
### 快速排序算法 Quick Sort
https://1256418761.vod2.myqcloud.com/c8e8a510vodtransgzp1256418761/014d9ff97447398156690252976/v.f30.mp4

---
### 归并排序算法 Merge Sort
https://1256418761.vod2.myqcloud.com/c8e8a510vodtransgzp1256418761/8175cc3c7447398156688442287/v.f30.mp4

---
### 快速排序与归并排序的比较
https://1256418761.vod2.myqcloud.com/c8e8a510vodtransgzp1256418761/8427b5807447398156688596731/v.f30.mp4

<br></br>
## 快速选择算法 Quick Select
https://1256418761.vod2.myqcloud.com/c8e8a510vodtransgzp1256418761/19df92137447398156703729534/v.f40.mp4

<br></br>
## 课后补充内容

---
### 三指针算法

题目描述

将包含0，1，2三种颜色代码的数组按照颜色代码的大小排序。如 [1,0,1,0,2] => [0,0,1,1,2]。

LintCode 提交地址：http://www.lintcode.com/problem/sort-colors/

解法分析

在颜色排序（Sort Color）这个问题中，传统的双指针算法可以这么做：

1. 先用 partition 的方式区分开 0 和 1, 2
2. 再在右半部分区分开 1 和 2

这个算法不可避免的要使用两次 Parition，写两个循环。许多面试官会要求你，能否只 partition 一次，也就是只用一个循环。

用一个循环的方法：
http://www.jiuzhang.com/solution/sort-colors

类似的题
G家问过一个类似的题：给出 low, high 和一个数组，将数组分为三个部分，< low, >= low & <= high, > high。解法和本题一模一样

---
### 烙饼排序

烙饼排序是说，如果有一个操作 flip(arr, i)，能够在 O(1) 的时间内将数组 arr 的前 i 个数进行翻转。你能否用这个操作来实现一个排序算法？因为 flip 操作就像是一沓烙饼伸一个铲子进去然后把最上面的 i 个烙饼翻转了一下，因此叫做烙饼排序（Pancake Sorting）。

GeeksforGeeks 上已经有比较好的讲解和代码：

https://www.geeksforgeeks.org/pancake-sorting/

LintCode 练习地址：

http://www.lintcode.com/problem/pancake-sorting/

---
### 如何写 Comparator 来对区间进行排序？

对于数组、链表、堆等结构，标准库中排序方法，往往是对于基本类型的升序排序，有的时候，不一定能满足我们的要求。例如我们有一些特殊的顺序要求，或待排序的对象类型不是基本类型。此时，就需用到自定义排序。自定义排序可以用在很多地方，比如数组排序，堆的排序规则等。

Python实现自定义排序

1. 实现__lt__方法:
以Interval区间为例，在定义该类时，重写其中的__lt__方法，使得Interval类可以进行大小比较，这样也可实现自定义的排序：

    ```python
        class Interval:
            def __init__(self, left, right):
                self.left = left
                self.right = right

            # 以下为重写的__lt__方法
            def __lt__(self, other):
                # 当两个Interval比较大小时，直接比较它们的left属性
                return self.left < other.left
    ```

2. 定义key函数
可以给sort方法传入一个key函数，表示按照什么标准来对元素进行排序，仍以上面的例子为例:
    ```python
    # 要传给sort函数的key方法，表示按照interval.left进行排序
    def IntervalKey(interval):
        return interval.left 

    A = []
    A.append(Interval(1, 7))
    A.append(Interval(5, 6))
    A.append(Interval(3, 4))
    A.sort(key=IntervalKey)
    ```
    
    如果要实现多关键字排序怎么办（比如left小的排前面，如果left相等的话，那么right小的排前面）?
    答案是返回一个tuple作为key。在Python中, 两个tuple比较大小时会先比较第一个元素，返回第一个元素较小的那个，如果第一个元素相等，再比较第二个元素，返回较小的那个，以此类推......
    我们可以利用这一点来实现多关键字排序，具体可以参考下面的例子：

    ```python
    class Interval:
        def __init__(self, left, right):
            self.left, self.right = left, right

        # 打印函数，用于直接print一个Interval对象
        def __repr__(self):
            return "Interval(%d, %d)" % (self.left, self.right)


    data = [(3, 2), (3, 1), (2, 7), (1, 5), (2, 6), (1, 7)]
    intervals = [Interval(left, right) for left, right in data]

    print(sorted(intervals, key=lambda i: (i.left, i.right)))  # 先按x从小到大排，再按y从小到大排
    # 结果: [Interval(1, 5), Interval(1, 7), Interval(2, 6), Interval(2, 7), Interval(3, 1), Interval(3, 2)]

    print(sorted(intervals, key=lambda i: (-i.left, i.right)))  # 先按x从大到小排，再按y从小到大排
    # 结果: [Interval(3, 1), Interval(3, 2), Interval(2, 6), Interval(2, 7), Interval(1, 5), Interval(1, 7)]

    print(sorted(intervals, key=lambda i: (i.right, i.left)))  # 先按y从小到大排，再按x从小到大排
    # 结果: [Interval(3, 1), Interval(3, 2), Interval(1, 5), Interval(2, 6), Interval(1, 7), Interval(2, 7)]

    print(sorted(intervals, key=lambda i: (-i.right, i.left)))  # 先按y从大到小排，再按x从小到大排
    # 结果: [Interval(1, 7), Interval(2, 7), Interval(2, 6), Interval(1, 5), Interval(3, 2), Interval(3, 1)]
    ```
    
---
### 在排好序的区间序列中插入新区间

问题描述

给一个排好序的区间序列，插入一段新区间。求插入之后的区间序列。要求输出的区间序列是没有重叠的。

LintCode 练习地址：http://www.lintcode.com/problem/insert-interval/

算法描述

1. 将该新区间按照左端值插入原区间中，使得原区间左端值是有序的。
2. 遍历原区间列表，并把它复制到一个新的answer区间列表当中，answer是最后要返回的结果。
3. 遍历时，要记录上一次访问的区间last。若当前区间左端值小于等于last区间的右端值，说明这两区间有重叠，此时仅更新last的右端值为这两区间右端值较大者；若当前区间左端值大于last的右端值，则可以直接加入answer。
4. 返回answer。

F.A.Q

Q：第三步有什么意义？

A：插入新区间后的原区间列表，仅能保证左端是有序的。而区间中是否存在重叠，右端是否有序，这些都是未知的。

Q：时空复杂度多少？

A：都是O(N)。

Q：有没有更高效的做法？

A：有！在查找左端新区见待插位置时，可以采用二分查找。原算法的的第三步，实际上是在查找右端的位置，也可以用二分查找，这样两次查找的复杂度都降为了O(logN)。但是，完全没必要，因为这个算法涉及到数组中间位置的移动，所以O(N)的时间复杂度是逃不开的，二分查找的改进对效率提升不明显，而且会增大编码难度。有兴趣的同学可以自己尝试~

相关练习

http://www.lintcode.com/problem/intersection-of-arrays/

http://www.lintcode.com/problem/merge-intervals/