import psycopg2

# Replace these variables with your actual database connection information
db_name = "demo"
db_user = "demo"
db_pass = "demo"
db_host = "localhost"
db_port = "54321"

# Establish a connection to the database
conn = psycopg2.connect(
    dbname=db_name, user=db_user, password=db_pass, host=db_host, port=db_port
)
cursor = conn.cursor()

# SQL to find players with more than 100 games
sql_games_played = """
SELECT player_id, COUNT(*) AS games_played
FROM plays_in
GROUP BY player_id
HAVING COUNT(*) > 100;
"""

# Execute the query
cursor.execute(sql_games_played)

# Fetch all players with more than 100 games played
players = cursor.fetchall()

# Prepare SQL to find the number of wins for each player
sql_wins = """
SELECT COUNT(*) FROM games
WHERE (result = '1-0' AND white = %s) OR (result = '0-1' AND black = %s);
"""

# Calculate win percentages for players
win_percentages = []
for player in players:
    player_id, games_played = player
    # Execute the query to find the number of wins
    cursor.execute(sql_wins, (player_id, player_id))
    wins = cursor.fetchone()[0]
    win_percentage = (wins / games_played) * 100
    win_percentages.append((player_id, win_percentage, games_played))

# Sort the players by win percentage in descending order
win_percentages.sort(key=lambda x: x[1], reverse=True)

# Get the top ten players by win percentage
top_ten_players = win_percentages[:10]

# Close the cursor and the connection
cursor.close()
conn.close()

# Print out the top ten players
for player in top_ten_players:
    print(f"Player ID: {player[0]}, Win Percentage: {player[1]:.2f}%, Games Played: {player[2]}")
