# Python Buildins 

## String:
reverse: string[::-1]
String to Bytes:   b = s.encode()   (or b = bytes(s, 'utf-8')   or   b = s.encode('utf-8')  )
Bytes to String:   s = b.decode()   (or s = str(b, 'utf-8')     or   s = b.decode('utf-8')  )
char to ASCII num:     ord('a')  -> 97
ASCII num to char:      chr(97)  -> 'a'
check string is num:       s.isdigit()
check string is letters a-zA-Z:        s.isapha()

## bin:
int to bin: bin(int)   ->  '0b10'
bin to in: int('111', 2) 

## Dictionary:
list frequency dictionary: import collections:     dict = collections.Counter(list)          Counter.most_common(k)  return most common k using heapq
comprehension:      dict = {a:foo(a) for a in list if ...}
init a dict with default value an empty list:     collections.defaultdict(list)
dict.keys()   dict.values()     dict.items()
sorted(count, key=lambda vid: (count[vid], vid))     get keys in count

## List:
Initialize a 2D list:     [[None]*n for _ in range(n)]      Do Not use [[xx]*cols]*rows
Delete an element:     del a[3]     del a[2:4]    queue.pop(0)    stack.pop(-1)   list_a.remove('an item')
Find first occurrence:      a.index(3) 
max(arr[i:j] or [0])   to avoid empty list
pos[5:10] = [1,2]    to replace the list subarray
pos[5:5] = [1,2]     to insert to current list

## Global variable :
can be read in functions, but not changed.  Unless declare global xxx. 

## Sort by key:
sorted(list, key=lambda item: (item[1], item[0]))

## zip:
zip(nums, nums[3:])    -> [(num0, num3), (num1, num4), ...]  two lists do not have to be the same length

## int:
3//2 -> 1      -3//2 -> -2      int(-3/2) -> -1

## ~
| 0  | 1  | 2  | 3  | 4  |
|----|----|----|----|----|
| -5 | -4 | -3 | -2 | -1 |
| ~4 | ~3 | ~2 | ~1 | ~0 |

## &:
int & int: binary and operation
set & set: Intersection of two sets

