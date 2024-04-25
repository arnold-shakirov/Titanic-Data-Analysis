from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

# Initialize SparkContext
conf = SparkConf().setAppName("TitanicDataAnalysis").setMaster("local[*]")
sc = SparkContext(conf=conf)
spark = SparkSession(sc)

# Load the Titanic dataset from your local path
titanic_df = spark.read.csv("titanic.csv", header=True, inferSchema=True)

# Select relevant columns and drop rows with missing values in 'Age' or 'Sex'
titanic_cleaned = titanic_df.select("Survived", "Sex", "Age").na.drop(subset=["Age", "Sex"])

# Calculate survival rates by gender
survival_by_gender = titanic_cleaned.groupBy("Sex").agg(
    (avg("Survived") * 100).alias("Survival Rate (%)")
)

# Calculate the average age of the passengers
average_age = titanic_cleaned.agg(avg("Age").alias("Average Age")).collect()[0]["Average Age"]

# Show survival rates by gender
print("Survival Rates by Gender:")
survival_by_gender.show()

# Print the average age of the passengers
print("\nAverage Age of Passengers:")
print(f"{average_age:.2f}")

# Stop SparkContext
sc.stop()
