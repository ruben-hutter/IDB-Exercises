import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="demo",
    user="demo",
    password="demo",
    host="localhost",
    port="54321"
)

with conn.cursor() as cur:

    # Execute SQL query
    cur.execute("""
        SELECT version()
    """)

    print(cur.fetchone())

# Close connection
conn.close()
