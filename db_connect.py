import mysql.connector

# 🔹 Connect to MySQL
def get_connection(database=None):
    return mysql.connector.connect(
        host="localhost",
        user="root",      # change if your user is different
        password="",      # put your MySQL password
        database=database
    )
# cursor = db.cursor()
print("✅ Connected to MySQL")    