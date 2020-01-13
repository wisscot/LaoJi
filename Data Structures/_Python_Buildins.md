# Python Buildins 

## String
reverse: string[::-1]   

String to Bytes: &emsp; b = s.encode() &emsp; or &emsp; b = s.encode('utf-8')  \
Bytes to String: &emsp; s = b.decode() &emsp; or &emsp; s = b.decode('utf-8')    

char to ASCII num: &emsp; ord('a')  -> 97  \
ASCII num to char: &emsp; chr(97)  -> 'a' 

check string is num: &emsp; s.isdigit()  \
check string is letters a-zA-Z: &emsp; s.isapha()

string.ascii_uppercase\
string.ascii_lowercase\
string.ascii_letters
     
## Bin
int to bin str : &emsp; bin(2)  ->  '0b10'    \
bin str to int : &emsp; int('111', 2)      \
divmod(num,2) -> last digit in bin and remain val

## Comprehension     
dict = {a:foo(a) for a in list if ...}  
list = [a for a in list if ...]

## Dictionary
dict.keys() &emsp; dict.values() &emsp; dict.items()

## List
Initialize a 2D list:     \
 &emsp; [[None]*n for _ in range(n)]\
 &emsp; Do Not use [[xx]*cols]*rows 
 
Delete an element:     \
 &emsp; A.pop(3) &emsp; del A[3] &emsp; del A[2:4] &emsp; A[2:4] = [] &emsp; A.remove('item')   
          
Find first occurrence: \
 &emsp; a.index('item')  
 
max(arr[i:j] or [0]) &emsp; use or to avoid empty list  

pos[5:10] = [1,2] &emsp; to replace the list subarray   \
pos[5:5] = [1,2] &emsp; to insert to current list  

## Global variable
Can be read in functions, but not changed.  Unless declare global xxx. 

## Sort by key
sorted(list, key=lambda item: (item[1], item[0]))   \
sorted([x for x in dict], key=dict.get)

## zip
zip(nums, nums[3:])    -> [(num0, num3), (num1, num4), ...]  \
&emsp; two lists can be with different length

## int
3 // 2 -> 1  &emsp;  -3 // 2 -> -2  &emsp;  int(-3/2) -> -1 \
1 + True -> 2  &emsp;  1 + False -> 0  &emsp;  True * 3 -> 3

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
&emsp; - return most common k (item, count) using heapq internally 
    
collections.defaultdict(list) \
&emsp; - init a dict with default value an empty list
