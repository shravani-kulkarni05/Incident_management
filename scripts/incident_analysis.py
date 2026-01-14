import pandas as pd
from db_connection import get_connection

conn = get_connection()

df = pd.read_sql("SELECT * FROM incidents", conn)
conn.close()

print("Total Incidents:", len(df))
print("\nIncidents by Type:\n", df['incident_type'].value_counts())
print("\nIncidents by Severity:\n", df['severity'].value_counts())

print("\nRoot Cause Analysis:\n")
rca = df['root_cause'].value_counts()
print(rca)

print("\nSystem-wise Incidents:\n")
system_failures = df['system_name'].value_counts()
print(system_failures)

severity_time = df.groupby('severity')['resolution_time'].mean()
print("\nAverage Resolution Time by Severity:\n", severity_time)

df['incident_date'] = pd.to_datetime(df['incident_date'])
df['month'] = df['incident_date'].dt.to_period('M')

monthly_trend = df.groupby('month').size()
print("\nMonthly Incident Trend:\n", monthly_trend)

rca.to_csv('../data/root_cause_analysis.csv')
monthly_trend.to_csv('../data/monthly_incident_trend.csv')


