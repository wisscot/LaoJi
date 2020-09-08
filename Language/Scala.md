# Scala 

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
// return 3, similar to pythono collections.defaultdict

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

## Spark RDD:
val numRange = scala.util.Random.shuffle(1 to 10000)
val rdd = sc.parallelize(numRange)
val rdd2 = data.map(_ * 2)

val sample = rdd.takeSample(true, 1000, 123)
// args: can take second time, how many to take, seed (optional)

val nums1 = Array.fill(100000)(scala.util.Random.nextDouble)
val nums2 = Array.fill(100000)(scala.util.Random.nextDouble)
val rdd = sc.parallelize(nums1)
val rdd2 = sc.parallelize(nums2)
val corr = org.apache.spark.mllib.stat.Statistics.corr(rdd, rdd2, "pearson")
//get correlation between two number datasets

val rdd = sc.textFile("someFiction.txt")
rdd.take(25).foreach(println)
//top 25 lines print out
filtedLines = rdd.filter(line => line.contains("someword"))

## Spark DataFrame
import org.apache.spark.sql.SparkSession
val spark = SparkSession.builder().appName("DFExercise").getOrCreate()
val df = spark.read.option("header", "true").csv("filename")

df.take(10)
df.show()

df.schema
df.columns

// To use SQL:
df.createOrReplaceTempView("viewname")
val x = spark.sql("""SELECT ...  FROM viewname""")

// Join two df
val df_joined = df1.join(df2, "col1")