import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password=" "
)

cur = conn.cursor()

def upload_data_from_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=";")
        for row in reader:
            cur.execute(
                "INSERT INTO PhoneBook (first_name, last_name, phone, email) VALUES (%s, %s, %s, %s)",
                (row[0], row[1], row[2], row[3])
            )
        conn.commit()
        print("Data uploaded successfully from", filename)

def update_data(id, column, value):
    cur.execute(
        f"UPDATE PhoneBook SET {column} = %s WHERE id = %s",
        (value, id)
    )
    conn.commit()
    print("Data updated successfully")

def insert_data_from_console():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    cur.execute(
        "INSERT INTO PhoneBook (first_name, last_name, phone, email) VALUES (%s, %s, %s, %s)",
        (first_name, last_name, phone, email)
    )
    conn.commit()
    print("Data inserted successfully")

def query_data(column, value, limit, offset):
    cur.execute(
        f"SELECT * FROM PhoneBook WHERE {column} = %s LIMIT %s OFFSET %s",
        (value, limit, offset)
    )
    rows = cur.fetchall()
    if len(rows) == 0:
        print("No records found")
    else:
        for row in rows:
            print(row)

def search_data(pattern):
    cur.execute(
        f"SELECT * FROM PhoneBook WHERE first_name LIKE '%{pattern}%' OR last_name LIKE '%{pattern}%' OR phone LIKE '%{pattern}%'"
    )
    rows = cur.fetchall()
    if len(rows) == 0:
        print("No records found")
    else:
        for row in rows:
            print(row)

def delete_data(column, value):
    cur.execute(
        f"DELETE FROM PhoneBook WHERE {column} = %s",
        (value,)
    )
    conn.commit()
    print("Data deleted successfully")

upload_data_from_csv('PhoneBook_data.csv')
insert_data_from_console()
print("-----------------------------------------------------------------------------------")
update_data(1, 'first_name', 'Jane')
print("-----------------------------------------------------------------------------------")
delete_data('last_name', 'Harris')
print("-----------------------------------------------------------------------------------")
search_data('7919')
print("-----------------------------------------------------------------------------------")
query_data('last_name', 'Jones', 10, 0) # Querying the first 10 records with last name = 'Jones'

cur.close()
conn.close()