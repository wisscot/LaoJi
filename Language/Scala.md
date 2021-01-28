# Scala 

## Philosophy
1. Operate with IMMUTABLE value.  Any modification to an object must return ANOTHER object. 
   - Miracle in multithread and distributed env
   - helps making sense of the code 
2. Everything is Object, even the operator 


## Resources
[Python to Scala](https://wrobstory.gitbooks.io/python-to-scala/content/index.html)

## Data Type
val a = 32654867125132L  (add L to the end of the large integer)

## Common Operations
item in list/dict  (python)  ->  list/array contains item (scala)
For number: + - * / % += -= .. (same as python)


## Comprehension
Note that in many cases, it may be more concise to use map vs a for-comprehension:
val array2 = for (x <- array if x > 3) yield x + 2     equivalent to 
val array2 = array.filter(_ > 3).map(_ + 2)

array.map(func(_))
array.filter(func(_))
array.filterNot(func(_))

// map, filter can be applied to Array, Vector, ArrayBuffer
Vector("foo", "bar", "baz").filter(_ != "foo").map(_ + "qux")


// List (python) -> ArrayBuffer (scala):
import scala.collection.mutable.ArrayBuffer
var nums = ArrayBuffer[Int]()
for (n <- 0 until 5) {
    nums += n
}
// res: ArrayBuffer(0, 1, 2, 3, 4)
// <- is "in" in python, -> is : in python dict


## Sequences

List -> Linked List
Vectors -> Immutable Array (best default immutable sequence in Scala)
Array -> Mutable Array of Fix Length
ArrayBuffer -> Mutable Array of Varying Length (the go-to mutable sequence)

enumerate() in python is nums.zipWithIndex in Scala
nums.zipWithIndex.toMap -> convert to a map, use the last one if duplicat key

parray = array.par -> Convert array to parallel array object for parallel operations

## Map (class not funciton)

val count = Map(1 -> 4, 2 -> 5, 3 -> 6)
// immutable Map

val mut_fruit_count = scala.collection.mutable.Map[String, Int]()
// mutable Map, similar to dict in python

val defaultMap = Map("foo" -> 1, "bar" -> 2).withDefaultValue(3)
defaultMap("other")
count.getOrElse("other", 3)
// return 3, similar to python collections.defaultdict

for ((k, v) <- count) ...
// similar to python

Class SortedMap in scala, tree map.  No equivalent in Python. 
// SortedMap is immutable

count.keys
count.values
// get keys and values

count.get(key)   
count get key
// both work

map2 = map1 + (key, value)
map2 = map1 - key


## Tuple
val foo = (1, 2.3, "hello")
// foo._1 is 1

val (a, b, c) = foo
// unpack

val pairs = Array(1,2,3).zip(Array("four", "five", "six"))
// pairs: Array[(Int, String)] = Array((1,four), (2,five), (3,six))


## Exceptions

```scala
throw new RunTimeException("user define message")

try{
    ...
} catch {
  case e: OneException => print(e)
  case _: OtherException => print("other")
} finally {
  println("print this for any catch")
}
```

## Object Oriented

```scala

class A {
    ...
}
class B(val b:Int) extends A //inheritance

//Abstract Class
abstract class C(...) {
    ...  // fields and methods are by default public, can restrict by adding protect or private
}
class D(..) extends C {
    //implementation or override
}

//"interface"
//ultimate abstract class, mutiple inheritance, can leave anything unimplemented
trait H {
    ...
}
class G(...) extends A with H {
    ...
}

a.call(b)    equals to    a call b      //this only available for method with one argument
1 + 2        equals to    1.+(2)        //everything is a object/method

// anonymous class
val h = new H()

// object singlton
object MySingleton{
    val a = 1
    def apply(x:Int): Int = x + 1
}
MySingleton.apply(2)   equals to    MySingleton(2)

// companion object
object A {
    // can access class A's private fields/methods
    val field: boolean = true
}
val v = A.field // "static" field/method

// case class
// come with companion with apply(), so no need to new
// sensible equal and hash code
// serialization
// pattern matching
case class Person(...)
bob = Person(name, age)    equals to    bob = Person.apply(name, age)

// generics
abstract class MyList[T] { // can be any type
    def head: T
    def tail: MyList[T]
}
val aList = MyList[Int]
val bList = MyList[String]

```
