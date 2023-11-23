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

# Step 1: Add the title_id column to the plays_in table
sql_add_column = """
ALTER TABLE plays_in ADD COLUMN title_id INT;
"""
cursor.execute(sql_add_column)
conn.commit()

# Step 2: Update the title_id column in plays_in with the correct values from games
sql_update_titles = """
UPDATE plays_in p
SET title_id = CASE 
    WHEN p.is_white = b'1' THEN g.white_title
    ELSE g.black_title
END
FROM games g
WHERE p.game_id = g.game_id;
"""
cursor.execute(sql_update_titles)
conn.commit()

# Close connection
cursor.close()
conn.close()

print("Updated plays_in table with title_id column.")

