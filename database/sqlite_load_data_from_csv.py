import sqlite3
import csv
import glob
import os


def sqlite_load_data_from_csv(path_input_files, path_database):
    os.chdir(path_input_files)
    conn = sqlite3.connect(path_database)
    cursor = conn.cursor()
    csv_files = glob.glob('*.csv')
    for file in csv_files:
        with open(file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            print(file)
            create_table = f"CREATE TABLE IF NOT EXISTS {file.replace('.csv', '')} ({', '.join(header)})"
            cursor.execute(create_table)
            insert_query = f"INSERT INTO table_name VALUES ({', '.join(['?'] * len(header))})"
            cursor.executemany(insert_query, reader)
    conn.commit()
    conn.close()
