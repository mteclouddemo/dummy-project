import psycopg2
from psycopg2 import sql

# Hardcoded credentials
db_name = 'users_db'
db_user = 'db_admin'
db_password = 'P@ssw0rd!'
db_host = '192.168.123.123'
db_port = 'your_database_port'

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)

# Create a cursor object
cur = conn.cursor()

# Define the SQL query
query = sql.SQL("SELECT * FROM user_profiles")

# Execute the query
cur.execute(query)

# Fetch all the results
results = cur.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()
