# Outlier_cleaning_from_DB
## Description
This program performs outlier detection and cleaning on database columns containing both categorical and numerical data. It retrieves data from a specified Oracle database, analyzes it for rare or infrequent values, as well as outliers, and returns the results for further inspection or data cleansing. The program uses SQL queries to extract the relevant data from the database and then applies statistical methods to detect and handle outliers. Additionally, it checks for the presence of invalid (non-numeric) values in numerical columns.

## Functional Description
The program performs the following steps:
1. Retrieves data from the database.
2. Analyzes string columns for rare values (less than a specified frequency).
3. Detects outliers in numerical columns using IQR (Interquartile Range) and Grubbs’ test.
4. Separates invalid (non-numeric) values in numerical columns for further inspection.
5. Outputs the results in a format that shows rare values and outliers for further analysis.

## How It Works
1. The program connects to an Oracle database using SQLAlchemy and executes queries to retrieve the necessary data.
2. For string columns, it checks for rare values (values that appear fewer than 5 times) and displays them.
3. For numerical columns, it identifies and handles outliers using statistical methods like the IQR method and Grubbs’ test.
4. The results are then displayed in a readable format for further processing.

## Input Structure
To run the program, the following parameters need to be provided:
1. Database credentials: Username, Password, Database DSN (Data Source Name)
2. Column categories: String columns to check for rare values, Numerical columns to check for outliers.
The program is designed to work with a specific table in the Oracle database: ml_daup.canvas_osago_contract.

## Technical Requirements
To run the program, the following are required:
1. Python 3.x
2. Installed libraries: sqlalchemy, pandas, numpy, scipy, IPython
3. Oracle Database with the following table: ml_daup.canvas_osago_contract, which contains relevant columns to be analyzed.

## Usage
1. Modify the username, password, and dsn values to connect to your Oracle database.
2. Define the columns you wish to analyze (both string and numerical).
3. Run the script. It will display:
     Rare values for string columns.
     Outliers in numerical columns.
     Invalid (non-numeric) entries in numerical columns.

## Example Output
Rare values: 
  For a string column: A list of values that occur less than 5 times.
Outliers:
  For numerical columns: Detected values that fall outside the defined statistical bounds.

## Conclusion
This tool helps in identifying and cleaning outliers and invalid values in the database, improving the quality of the data for further analysis and modeling.
