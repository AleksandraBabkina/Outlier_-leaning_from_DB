# import sys
# import oracledb
# oracledb.version = "8.3.0"
# sys.modules["cx_Oracle"] = oracledb
# import oracledb
# from sqlalchemy.dialects import oracle

from sqlalchemy import create_engine, Column, String, Float, select, or_, and_, Table, MetaData, inspect, text
from sqlalchemy.orm import sessionmaker, declarative_base
import pandas as pd

# Header with connection, DO NOT MODIFY
username = 'username'
password = 'password'
dsn = 'dsn'

conection_string = f'oracle+cx_oracle://{username}:{password}@{dsn}'  # SQL connection
engine = create_engine(conection_string)  # Engine

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Columns with unique data
col_id = ['CONTRACT_ID', 'CONTRACT_NUMBER', 'vin', 'grz', 'OWNER_KLADR', 'CHASSIS', 'BODY', 'contractid']
# Columns with string data
col_bykv = ['tipag', 'brand_region', 'bs_min_max', 'class_dci', 'AUTOSTAT_CATEGORY_VEHICLE', 'model_class', 'subgroup',
            'ins_gender', 'sex_dr', 'brand_calc_dci', 'pass_reg', 'model_new', 'as_engine_type1', 'sale_channel', 'kat_ts',
            'sale_reg', 'model_calc_dci', 'owner', 'vehicle_type', 'subuserag', 'KLADR_REGION', 'CREDIT_LEASING_VEHICLE',
            'brand_level', 'vin_3l', 'BRANCH_CALC', 'brand_dci', 'INSURED_PERSON', 'ADDITIONAL_DRIVER', 'reg_grz', 'astat_codetech',
            'reg_prop_owner_sub_zone', 'model_dci', 'certificate_reg', 'owner_gender']
# Empty columns
col_pyst = ['contract_status_agg', 'ins_age', 'ingos', 'DAY_OF_WEEK', 'OBJECT_ID', 'as_power_weight', 'settlement_type']
# Columns with dates
col_data = ['START_DATE', 'CONCLUSION_DATE', 'LAST_RIGHT_CHANGE_YEAR', 'ch_s', 'astat_last_ny']
# Columns with numeric dates
col_chisl = ['ikp', 'bs', 'owner_age', 'chs_po_vehicle', 'as_dtp_at', 'delta_age', 'sale_reg_is_property_0', 'nsp4', 'days_wr_st',
             'power', 'AUTOSTAT_UTILITY', 'astat_vin', 'delta_exp', 'sale_reg_is_property_1', 'nsp5',
             'HAS_ADDITIONAL_DRIVER', 'vehicle_age', 'AUTOSTAT_TAXI', 'owner_dr', 'bs_begin', 'as_dtp_year', 'sp1', 'kbm_min',
             'ko', 'astat_dtp', 'ins_dr', 'kt_begin', 'as_dtp_sev_year', 'sp2', 'kt_correction', 'ks',
             'vin_is_null', 'multidrive', 'insurance_is_valid', 'kbm_begin', 'sp3', 'kvs_correction',
             'kt', 'grz_is_null', 'astat_kt', 'dopush', 'kvs_begin', 'as_weight', 'sp4', 'ADDITIONAL_TYPE', 'km',
             'ss_trdk', 'new_kt', 'min_experience_dr', 'ko_begin', 'as_count_regaction', 'sp5', 'kbm', 'kp',
             'minprice_audavalue', 'all_fio', 'min_age_dr', 'km_begin', 'as_power', 'nsp1', 'kbm_ins',
             'kvs', 'inn_ins', 'f1_fio', 'num_fam_dr', 'astat_km', 'rider', 'nsp2', 'dr_fio', 'as_dtp_sev_at',
             'taxi', 'rider_other_lb','nsp3']
         
# List of columns for analyzing string data 
columns_to_analyze = col_bykv

# Function to analyze string column 
def analyze_column(column):
    # Form SQL query to select ID and values from the column
    query = text(f"SELECT {column}, COUNT(*) as o_count FROM ml_daup.canvas_osago_contract GROUP BY {column}")

    # Connect to the database and execute query
    with engine.connect() as connection:
        result_proxy = connection.execute(query)

        # Convert result into DataFrame
        df = pd.DataFrame(result_proxy.fetchall(), columns=[column, 'o_count'])

        # Filter values that occur less than 8 times
        filtered_df = df[df['o_count'] < 5]

        # Return Series with rare values
        return filtered_df

# Process each column one by one 
for column in columns_to_analyze:
    rare_values_df = analyze_column(column)

    # Print results for each column separately
    if not rare_values_df.empty:
        print(f"Rare values for column '{column}':")
        display(rare_values_df)

# List of columns for analyzing string data 
columns_to_analyze = col_chisl

# Function to analyze numeric column 
def analyze_column(column):
    # Form SQL query to select ID and values from the column
    query = text(f"SELECT {column}, COUNT(*) as o_count FROM ml_daup.canvas_osago_contract GROUP BY {column}")

    # Connect to the database and execute query
    with engine.connect() as connection:
        result_proxy = connection.execute(query)

        # Convert result into DataFrame
        df = pd.DataFrame(result_proxy.fetchall(), columns=[column, 'o_count'])

        # Filter values that occur less than 8 times
        filtered_df = df[df['o_count'] < 5]

        # Return Series with rare values
        return filtered_df

# Process each column one by one 
for column in columns_to_analyze:
    rare_values_df = analyze_column(column)

    # Print results for each column separately
    if not rare_values_df.empty:
        print(f"Rare values for column '{column}':")
        display(rare_values_df)
        
numerical_columns = col_chisl

# Process each column one by one
for column in numerical_columns:
    # Form SQL query to select values and their frequencies
    query = text(f"SELECT {column}, COUNT(*) as o_count FROM ml_daup.canvas_osago_contract GROUP BY {column}")
    
    # Connect to the database and execute query
    with engine.connect() as connection:
        result_proxy = connection.execute(query)
        # Convert result into DataFrame
        df = pd.DataFrame(result_proxy.fetchall(), columns=[column, 'o_count'])

    df = df[df[column].notna()]
    string_df = pd.DataFrame()
    non_string_df = pd.DataFrame()

    # Check for string values in the column 'column'
    try:
        # Try to convert the column to float
        df['float_values'] = pd.to_numeric(df[column], errors='coerce')
        # Separate values that cannot be converted to float
        string_df = df[df['float_values'].isna()].drop(columns=['float_values'])
        # Remove string values from the original DataFrame
        non_string_df = df[~df['float_values'].isna()].drop(columns=['float_values'])
        # Convert 'column' in non_string_df to float
        non_string_df[column] = non_string_df[column].astype(float)
    except Exception as e:
        print(f"Error converting column '{column}' to float: {e}")

    # Expand data by frequencies
    expanded_values = non_string_df[column].repeat(non_string_df['o_count']).reset_index(drop=True).dropna().astype(float)

    # Handle outliers for numeric columns
    Q1 = expanded_values.quantile(0.002)
    Q3 = expanded_values.quantile(0.998)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Filter outliers
    outliers = expanded_values[(expanded_values < lower_bound) | (expanded_values > upper_bound)]
    outliers = outliers.to_frame(name=column)

    # Print results for each column separately
    if not outliers.empty:
        print(f"Outliers for column '{column}':")
        display(outliers.drop_duplicates())
    else:
        print(f"No outliers found for column '{column}'.")

    if not string_df.empty:
        print(f"String values found in column '{column}':")
        display(string_df)
        
        
import numpy as np
import scipy.stats as stats
x = np.array([12,13,14,19,21,23])
y = np.array([12,13,14,19,21,23,45])
def grubbs_test(x):
    n = len(x)
    mean_x = np.mean(x)
    sd_x = np.std(x)
    numerator = max(abs(x-mean_x))
    g_calculated = numerator/sd_x
    print("Grubbs Calculated Value:",g_calculated)
    t_value = stats.t.ppf(1 - 0.05 / (2 * n), n - 2)
    g_critical = ((n - 1) * np.sqrt(np.square(t_value))) / (np.sqrt(n) * np.sqrt(n - 2 + np.square(t_value)))
    print("Grubbs Critical Value:",g_critical)
    if g_critical > g_calculated:
        print("From grubbs_test we observe that calculated value is lesser than critical value, Accept null hypothesis and conclude that there is no outliers\n")
    else:
        print("From grubbs_test we observe that calculated value is greater than critical value, Reject null hypothesis and conclude that there is an outlier\n")
grubbs_test(x)
grubbs_test(y)