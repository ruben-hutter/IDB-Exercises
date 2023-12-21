db_size=$(du -h example.db | cut -f1)

csv_size=$(du -h 100127.csv | cut -f1)

echo "SQLite DB: $db_size"
echo "CSV file: $csv_size"

if [ "$db_size" -eq "$csv_size" ]; then
    echo "Same size"
elif [ "$db_size" -lt "$csv_size" ]; then
    echo "DB < CSV"
else
    echo "CSV < DB"
fi
