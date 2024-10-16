import os
import psycopg2

# Get password from environment variable
password = os.environ.get("DB_PASSWORD")

# Separator
separator = "-" * 30

# Connect to PostgreSQL
con = psycopg2.connect(
    dbname="introdb",
    user="introdb416",
    password=password,
    host="dmi-dbis-introdb4.dmi.unibas.ch",
    port="5432"
)

with con.cursor() as cur:
    # Print how many games were won by white
    cur.execute("""\
        SELECT COUNT(*)
        FROM games
        WHERE result = '1-0'
    """)
    white_wins = cur.fetchone()
    if white_wins:
        print("White wins:", white_wins[0])

    print(separator)
    # Print the number of games per month. Print the name of the month, not the number
    cur.execute("""\
        SELECT EXTRACT(MONTH FROM game_start) AS month, COUNT(*)
        FROM games
        GROUP BY month
    """)
    for month, count in cur.fetchall():
        print("Month:", month, "Count:", count)

    print(separator)
    # Print the total number of games
    cur.execute("""\
        SELECT COUNT(*)
        FROM games
    """)
    total_games = cur.fetchone()
    if total_games:
        print("Total games:", total_games[0])

# Close connection
con.close()

