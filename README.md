# Titanic Data Analysis with PySpark

## Overview
This project performs a simple analysis of the Titanic dataset using PySpark. The analysis focuses on calculating survival rates by gender and the average age of the passengers. PySpark is used to process and analyze the dataset efficiently.

## Features
- **Survival Rate by Gender**: Calculates the survival rates for male and female passengers.
- **Average Age Calculation**: Computes the average age of the passengers from the dataset.
- **PySpark**: Leverages PySpark's distributed computing capabilities to handle the dataset.

## Project Structure
- **`titanic.csv`**: The dataset file containing information about Titanic passengers.
- **`titanic_analysis.py`**: The Python script that uses PySpark to process the Titanic dataset and compute the desired metrics.

## How to Run the Project

### Prerequisites
- **Apache Spark**: Ensure Spark is installed on your system. You can follow the installation guide on the [Apache Spark website](https://spark.apache.org/downloads.html).
- **PySpark**: Install PySpark via pip if not already installed:
    ```bash
    pip install pyspark
    ```

### Running the Script

1. Clone the repository:
    ```bash
    git clone https://github.com/arnold-shakirov/titanic-data-analysis.git
    ```

2. Navigate to the project directory:
    ```bash
    cd titanic-data-analysis
    ```

3. Ensure the Titanic dataset (`titanic.csv`) is in the project directory or adjust the path in the script accordingly.

4. Run the PySpark script:
    ```bash
    python titanic_analysis.py
    ```

### Output
The script calculates:
1. **Survival Rates by Gender**: The survival rate for male and female passengers.
2. **Average Age of Passengers**: The average age of the Titanic passengers.

Sample output:
```text
Survival Rates by Gender:
+------+-----------------+
|   Sex|Survival Rate (%)|
+------+-----------------+
|female|         74.20382|
|  male|         18.89081|
+------+-----------------+

Average Age of Passengers:
29.70
```
### Dataset
You can download the Titanic dataset from Kaggle or use any local CSV file with similar data structure.

The dataset should have the following columns for this script to work:

Survived: 1 for survived, 0 for not.
Sex: Gender of the passengers.
Age: Age of the passengers.

### Requirements
Python 3.x or higher
PySpark (install with pip install pyspark)

### Contact
For any questions or suggestions, feel free to reach out to me at [ashakirov@stetson.edu].
