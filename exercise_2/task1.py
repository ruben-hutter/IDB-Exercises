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

    # First part
    cur.execute("""
        SELECT version()
    """)

    print(cur.fetchone())

    # Second part

    cur.execute("""
        SELECT SUM(game_white_wins::integer) AS white_wins
        FROM games_simple
    """)

    rows = cur.fetchall()

    print("Number of white wins:", rows[0][0])

# Close connection
conn.close()
