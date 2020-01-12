# Python Buildins 

## String
reverse: string[::-1]   

String to Bytes: &emsp; b = s.encode() &emsp; or &emsp; b = s.encode('utf-8')  \
Bytes to String: &emsp; s = b.decode() &emsp; or &emsp; s = b.decode('utf-8')    

char to ASCII num: &emsp; ord('a')  -> 97  \
ASCII num to char: &emsp; chr(97)  -> 'a' 

check string is num: &emsp; s.isdigit()  \
check string is letters a-zA-Z: &emsp; s.isapha()

string.ascii_uppercase\
string.ascii_lowercase\
string.ascii_letters
     
## Bin
int to bin str : bin(2)  ->  '0b10'    \
bin str to int : int('111', 2)      \
divmod(num,2) -> last digit in bin and remain val

## Comprehension     
dict = {a:foo(a) for a in list if ...}  
list = [a for a in list if ...]

## Dictionary
list frequency dictionary: \
count = collections.Counter(list)          \
count.most_common(k) :  return most common k using heapq    \
init a dict with default value an empty list:    collections.defaultdict(list)
dict.keys()   dict.values()     dict.items()
sorted(count, key=lambda vid: (count[vid], vid))     get keys in count

## List
Initialize a 2D list:     [[None]*n for _ in range(n)]      Do Not use [[xx]*cols]*rows
Delete an element:     del a[3]     del a[2:4]    queue.pop(0)    stack.pop(-1)   list_a.remove('an item')
Find first occurrence:      a.index(3) 
max(arr[i:j] or [0])   to avoid empty list
pos[5:10] = [1,2]    to replace the list subarray
pos[5:5] = [1,2]     to insert to current list

## Global variable
can be read in functions, but not changed.  Unless declare global xxx. 

## Sort by key
sorted(list, key=lambda item: (item[1], item[0]))

## zip
zip(nums, nums[3:])    -> [(num0, num3), (num1, num4), ...]  two lists do not have to be the same length

## int
3//2 -> 1      -3//2 -> -2      int(-3/2) -> -1
1 + True -> 2       1 + False -> 0    True*3 -> 3

## ~
| 0  | 1  | 2  | 3  | 4  |
|----|----|----|----|----|
| -5 | -4 | -3 | -2 | -1 |
| ~4 | ~3 | ~2 | ~1 | ~0 |

## & and |
int & int: binary and operation\
int | int: binary or operation

set & set: Intersection of two sets\
set | set: Combination of two sets

## functools
@functools.lru_cache(None): memorize dynamic programming recursive calls

## itertools
itertools.product(A,B) -> ((x,y) for x in A for y in B)
> for v1, (r1, c1) in enumerate(itertools.product(range(5), range(6))):  ...

## collections.Counter()
count = collections.Counter(items)
count -> {item1:count1, item2:count2, ...}
count.most_common(k) -> [(item, count), ...]
    - return most common k (item, count) using heapq internally