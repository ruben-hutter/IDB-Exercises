import redis
import csv

conn = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)

def main():
    
    process_csv_with_pipeline('100127.csv')

    name = input("Please input a last name: ")
    for year in range(2011, 2023):
        print(year, name, get_count(name, year))
    conn.close()


def set_name(name, id):
    key = f"name:{name}"
    conn.set(key, id)

def set_count(id, date, count):
    key = f"count:{id}:{date}"
    conn.set(key, count)

def get_name_id(name):
    key = f"name:{name}"
    return conn.get(key)

def get_count(id, date):
    key = f"count:{id}:{date}"
    return conn.get(key)

def process_csv_with_pipeline(file_path):
    with open(file_path, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        next(csvreader)  # skip header row

        pipeline = conn.pipeline()
        i = 0
        for row in csvreader:
            if i % 10000 == 0:
                print("Inserted rows: ", i)
            i+=1
            try:
                name = row[1]
                count = row[2]
                date = row[3]

                pipeline.set(f"name:{name}", name)  # Using name as ID
                pipeline.set(f"count:{name}:{date}", count)

            except Exception as e:
                print(f"Error processing row: {row}")
                print(f"Error message: {e}")

        pipeline.execute()


if __name__ == "__main__":
    main()
