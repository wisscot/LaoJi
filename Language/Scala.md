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
```

List -> ArrayBuffer:
```scala
import scala.collection.mutable.ArrayBuffer
var nlist = ArrayBuffer[Int]()
while (n < 5) {
    nlist += n
    n += 1
}
res115: scala.collection.mutable.ArrayBuffer[Int] = ArrayBuffer(0, 1, 2, 3, 4)
```

<- equals "in" in python, -> is : in python dictionary