import sqlite3

source_db = 'source.db'
destination_db = 'destination.db'

def transfer_data():
    try:
        source_conn = sqlite3.connect(source_db)
        dest_conn = sqlite3.connect(destination_db)

        source_cursor = source_conn.cursor()
        dest_cursor = dest_conn.cursor()

        table = 'put_your_table_name'

        source_cursor.execute(f'SELECT * FROM {table}')
        rows = source_cursor.fetchall()

        if not rows:
            print('No data to transfer.')
            return

        print(f'Fetched {len(rows)} rows from the source database.')

        columns = [desc[0] for desc in source_cursor.description]
        
        insert_query = f'INSERT INTO {table} ({", ".join(columns)}) VALUES ({", ".join(["?"] * len(columns))})'

        dest_cursor.executemany(insert_query, rows)

        dest_conn.commit()

        print('Data transferred successfully.')

        source_conn.close()
        dest_conn.close()

    except sqlite3.Error as e:
        print(f'Error transferring data: {e}')

transfer_data()
