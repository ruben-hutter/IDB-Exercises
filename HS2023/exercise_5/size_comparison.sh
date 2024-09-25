db_size=$(du -h example.db | cut -f1)

csv_size=$(du -h 100127.csv | cut -f1)

echo "SQLite DB: $db_size"
echo "CSV file: $csv_size"

