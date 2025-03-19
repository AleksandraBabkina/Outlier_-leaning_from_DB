# Outlier_Cleaning_from_DB

## Description
This program is designed to detect and analyze outliers and rare values in both categorical (string) and numerical columns of an Oracle database table. It retrieves data, identifies infrequent values, and applies statistical methods to detect outliers, providing a clear overview for further data cleansing and quality improvement.

## Functional Description
The program performs the following steps:

1. **Database Connection**: Connects to an Oracle database using SQLAlchemy.
2. **Rare Value Detection in String Columns**: Checks categorical columns for rare values (values appearing fewer than 5 times).
3. **Outlier Detection in Numeric Columns**: Uses statistical methods (Grubbs’ test) to detect outliers in numerical columns.
4. **Results Display**: Displays detected rare values and outliers for inspection.

## How It Works

1. **Connection Setup**:
   - Uses SQLAlchemy to establish a connection to the Oracle database.
   - Credentials (username, password, DSN) need to be configured.

2. **Categorical Columns Analysis**:
   - Executes SQL queries to count occurrences of each unique value.
   - Filters and displays values appearing fewer than 5 times.

3. **Numerical Columns Analysis**:
   - Applies **Grubbs' test** to detect statistical outliers.
   - Outputs whether the dataset contains outliers based on calculated critical values.

4. **Results Display**:
   - Uses `pandas` and `IPython.display` for easy visualization of rare values.
   - Provides clear output messages for each column.

## Input Structure

- **Database Credentials**:
  - `username`: Your database username
  - `password`: Your database password
  - `dsn`: Data Source Name (connection string)

- **Columns Categories**:
  - `col_id`: Columns with unique IDs
  - `col_bykv`: Columns with string/categorical data
  - `col_pyst`: Empty or nullable columns
  - `col_data`: Columns containing date values
  - `col_chisl`: Columns with numeric data

These columns are specified at the beginning of the script and can be modified as needed.

## Technical Requirements

- Python 3.x
- Oracle Database (table: `osago_contract`)
- Installed Python libraries:
  - `sqlalchemy`
  - `pandas`
  - `numpy`
  - `scipy`
  - `IPython`

## Usage
1. Modify the `username`, `password`, and `dsn` values to connect to your Oracle database.
2. Define the columns you wish to analyze (both string and numerical).
3. Run the script. It will display:
   - Rare values for string columns.
   - Outliers in numerical columns.
   - Invalid (non-numeric) entries in numerical columns.

## Example Output

**Rare values:**  
For a string column, the program outputs a list of values that occur fewer than 5 times, along with their occurrence count.

**Outliers:**  
For numerical columns, the program applies Grubbs' test to detect outliers. The output shows the calculated Grubbs statistic, the critical value, and a conclusion on whether an outlier is present.

## Conclusion

This script assists in identifying rare categorical values and statistical outliers in numerical columns directly from the database. By detecting these anomalies, the tool helps improve the accuracy and quality of datasets, making them more suitable for further analysis, reporting, and modeling tasks.
