import csv
import matplotlib.pyplot as plt

# Read data from the CSV file
with open('task_2.3.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    data = list(csv_reader)

# Extract counts and count_appearances from the data
counts = [int(row['count']) for row in data]
appearances = [int(row['count_appearances']) for row in data]

# Plot the results
plt.bar(counts, appearances)
plt.xlabel('Count')
plt.ylabel('Number of Appearances')
plt.title('Counts Appearing More Than 5 Times')
plt.show()

