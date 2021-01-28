# Scala Spark


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