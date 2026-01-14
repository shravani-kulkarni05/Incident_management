import random
from datetime import datetime, timedelta
import mysql.connector

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Plmnk@622001", 
    database="incident_management"
)

cursor = conn.cursor()

incident_types = ['Network', 'Application', 'Hardware', 'Login']
severities = ['Low', 'Medium', 'High', 'Critical']
root_causes = [
    'Misconfiguration',
    'Human Error',
    'Software Bug',
    'Hardware Failure',
    'ISP Issue'
]
systems = [
    'Payment System',
    'Employee Portal',
    'Core Router',
    'Database Server',
    'Office Network'
]

# Generate 500 incidents
for _ in range(500):
    incident_date = datetime.now().date() - timedelta(days=random.randint(1, 180))
    incident_type = random.choice(incident_types)
    severity = random.choice(severities)
    root_cause = random.choice(root_causes)
    system_name = random.choice(systems)
    resolution_time = random.randint(10, 300)
    status = 'Closed'

    cursor.execute("""
        INSERT INTO incidents
        (incident_date, incident_type, severity, root_cause, system_name, resolution_time, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        incident_date,
        incident_type,
        severity,
        root_cause,
        system_name,
        resolution_time,
        status
    ))

conn.commit()
cursor.close()
conn.close()

print("✅ 500 incident records generated successfully.")
