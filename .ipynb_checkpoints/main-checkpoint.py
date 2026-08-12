import pyodbc
import pandas as pd

server = r"LAPTOP-PUH0OFS5"
database = "pick_n_pay"

connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

try:
    # Connect to SQL Server
    conn = pyodbc.connect(connection_string)
    print("Successfully connected to SQL Server!")

    # SQL query
    query = """
        SELECT
            [transaction_id],
            [timestamp],
            [store_location],
            [sku],
            [product_name],
            [category],
            [quantity],
            [unit_price_zar],
            [total_amount_zar],
            [payment_method]
        FROM [dbo].[combined_beverage_sales]
    """

    # Store SQL results in a Pandas DataFrame
    df = pd.read_sql(query, conn)

    # Close database connection
    conn.close()

    print("Data successfully loaded into DataFrame!")
    #print(f"Rows: {df.shape[0]}")
    #print(f"Columns: {df.shape[1]}")

    df.head()  # Display the first few rows of the DataFrame
    print(df.head())  # Print the first few rows of the DataFrame

except pyodbc.Error as e:
    print("Database connection failed:")
    print(e)