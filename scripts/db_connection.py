import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Plmnk@622001",
        database="incident_management"
    )
