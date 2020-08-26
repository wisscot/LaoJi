# Scala 

## Resources
[Python to Scala](https://wrobstory.gitbooks.io/python-to-scala/content/index.html)

## Comprehension
Note that in many cases, it may be more concise to use map vs a for-comprehension:

```scala
scala> for (c <- Array(1, 2, 3)) yield c + 2
res56: Array[Int] = Array(3, 4, 5)

scala> Array(1, 2, 3).map(_ + 2)
res57: Array[Int] = Array(3, 4, 5)
```

Condition:
```scala
scala> for (x <- (1 to 5).toArray if x != 2 if x != 3) yield x
res44: Array[Int] = Array(1, 4, 5)

scala> Vector("foo", "bar", "baz").filter(_ != "foo").map(_ + "qux")
```

List (python) -> ArrayBuffer (scala):
```scala
import scala.collection.mutable.ArrayBuffer
var nlist = ArrayBuffer[Int]()
while (n < 5) {
    nlist += n
    n += 1
}
res115: scala.collection.mutable.ArrayBuffer[Int] = ArrayBuffer(0, 1, 2, 3, 4)
```

<- is "in" in python, -> is : in python dictionary


## Sequences

List -> Linked List
Vectors -> Immutable Array (best default immutable sequence in Scala)
Array -> Mutable Array of Fix Length
ArrayBuffer -> Mutable Array of Varying Length (the go-to mutable sequence)

enumerate() in python is nums.zipWithIndex in Scala
nums.zipWithIndex.toMap -> convert to a map, use the last one if duplicat key

## Map

val count = Map(1 -> 4, 2 -> 5, 3 -> 6)
// immutable Map

val mut_fruit_count = scala.collection.mutable.Map[String, Int]()
// mutable Map, similar to dict in python

val defaultMap = Map("foo" -> 1, "bar" -> 2).withDefaultValue(3)
defaultMap("other")
// return 3, similar to pythono collections.defaultdict

for ((k, v) <- count) ...
// similar to python

Class SortedMap in scala, tree map.  No equivalent in Python. 
// SortedMap is immutable

## Tuple
val foo = (1, 2.3, "hello")
// foo._1 is 1

val (a, b, c) = foo
// unpack

val pairs = Array(1,2,3).zip(Array("four", "five", "six"))
// pairs: Array[(Int, String)] = Array((1,four), (2,five), (3,six))


## Exceptions
throw new RunTimeException("user define message")

try{..
} catch {
  case ex: OneException => print(ex)
  case _: OtherException => print("other")
} finally {
  print("print this for any catch")
}


## Class
class Automobile(val a:Int = 1, var b:Int = 2){
    ...
}
car = new Automobile(a=3, b=6)
car.a = 4 // error
car.b = 4 // ok

class Automobile(private val a:Int = 4){
    ...
}
car.wheels // error
car.wheels = 5 // error

//Static mehtod in Scala is named "companion objects"
class Automobile(...){
    ...
}
object Automobile {
    var wheels = 4
    var lights = 2
    def print_uninst_str() = "No 'self' passed to this method, and no instantiation. It's static!"
}
Automobile.print_uninst_str()

//Abstract Class -> single inheritance
abstract class Automobile(val color:String, val make:String) {
    val door:Int = 6
    def top_speed():Int
}
class Car(color:String, make:String) extends Automobile(color, make) {
    override val doors = 4 // immutable need override
    def top_speed() = {...}
}
val mycar = new Car(...)
mycar.top_speed()

//Traits -> preferred over abstract class, mutiple inheritance
trait Engine {
    ...
}
trait Transmission {
    ...
}
class Car(...) extends Automobile(...) with Engine with Transmission {
    ...
}