import pandas as pd
from db_connection import get_connection

conn = get_connection()

query = "SELECT * FROM incidents"
df = pd.read_sql(query, conn)

print(df.head())
print("\nTotal Records:", len(df))

conn.close()
