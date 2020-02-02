# Python Buildins 


## string
reverse: string[::-1]   

String to Bytes:  b = s.encode()   or   b = s.encode('utf-8')  \
Bytes to String:   s = b.decode()   or   s = b.decode('utf-8')    
char to ASCII num:   ord('a')  -> 97  \
ASCII num to char:   chr(97)  -> 'a' 

check string is num:   s.isdigit()   Not good for negative number\
check string is letters a-zA-Z:   s.isapha()

string.ascii_uppercase\
string.ascii_lowercase\
string.ascii_letters

s.ljust(maxWidth)    by default filled with spaces \
s.rjust(maxWidth)


## bin
int to bin str :   bin(2)  ->  '0b10'    \
bin str to int :   int('111', 2)      \
divmod(num,2) -> last digit in bin and remain val


## Comprehension     
dict = {a:foo(a) for a in list if ...}  
list = [a for a in list if ...]


## dict
dict.keys()   dict.values()   dict.items()


## list
Initialize a 2D list:     \
   [[None]*n for _ in range(n)]\
   Do Not use [[xx]*cols]*rows 
 
Delete an element:     \
   A.pop(3)   del A[3]   del A[2:4]   A[2:4] = []   A.remove('item')   
          
Find first occurrence: \
   arr.index('item')  \
   arr.index('item', start, end)   find item in arr[start:end] \
   arr.find('item')  \
   arr.find('item', start, end)   similar to index, but return -1 if not found

arr.count('item')   return how many 'item' elements

max(arr[i:j] or [0])   use or to avoid empty list  

pos[5:10] = [1,2]   to replace the list subarray   \
pos[5:5] = [1,2]   to insert to current list  


## Global variable
Can be read in functions, but not changed.  Unless declare global xxx. 


## Sort by key
sorted(list, key=lambda item: (item[1], item[0]))   \
sorted([x for x in dict], key=dict.get)


## zip
zip(nums, nums[3:])    -> [(num0, num3), (num1, num4), ...]  \
     two lists can be with different length


## int
3 // 2 -> 1     -3 // 2 -> -2     int(-3/2) -> -1 \
1 + True -> 2     1 + False -> 0     True * 3 -> 3


## ~
| 0  | 1  | 2  | 3  | 4  |
|----|----|----|----|----|
| -5 | -4 | -3 | -2 | -1 |
| ~4 | ~3 | ~2 | ~1 | ~0 |


## & |
int & int: binary and operation\
int | int: binary or operation

set & set: Intersection of two sets\
set | set: Combination of two sets


## iterator
```python
data = iter(list)
num = next(data, None)
```

## functools
@functools.lru_cache(None): memorize dynamic programming recursive calls


## itertools
itertools.product(A,B) -> ((x,y) for x in A for y in B)
```python
for v1, (r1, c1) in enumerate(itertools.product(range(5), range(6))):  
    ...
```

## collections
count = collections.Counter(items)  \
count -> {item1:count1, item2:count2, ...}  \
count.most_common(k) -> [(item, count), ...]    \
     - return most common k (item, count) using heapq internally 
    
collections.defaultdict(list) \
     - init a dict with default value an empty list
