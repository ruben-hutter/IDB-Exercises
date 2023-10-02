import numpy as np
import psycopg2
import matplotlib.pyplot as plt

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="demo",
    user="demo",
    password="demo",
    host="localhost",
    port="54321"
)

# Create a cursor object
cur = conn.cursor()

# Execute SQL query
cur.execute("""
    SELECT game_month,
           SUM(game_white_wins::integer) AS white_wins,
           SUM((NOT game_white_wins)::integer) AS black_wins
    FROM games_simple
    GROUP BY game_month
""")

# Fetch all the rows
rows = cur.fetchall()

# Close the cursor and connection
cur.close()
conn.close()

# Unpack the result into separate lists
months, white_wins, black_wins = zip(*rows)

# Define the width of each bar
bar_width = 0.4

# Generate an array of indices for each month
indices = np.arange(len(months))

# Create a grouped bar chart
plt.figure(figsize=(10, 5))
plt.bar(indices, white_wins, color='b', width=bar_width, label='White Wins')
plt.bar(indices + bar_width, black_wins, color='r', width=bar_width, label='Black Wins')

# Set the positions of the x-axis ticks and labels
plt.xticks(indices + bar_width/2, months)

# Add labels and title
plt.xlabel('Month')
plt.ylabel('Number of Wins in millions')
plt.title('White vs. Black Wins per Month')
plt.legend()

# Show the plot
plt.show()
