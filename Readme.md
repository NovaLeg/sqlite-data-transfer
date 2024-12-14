# SQLite Data Transfer

This project provides a simple script to transfer data from one SQLite database to another. It connects to both a source and a destination SQLite database, fetches data from a specified table, and inserts that data into the corresponding table in the destination database.

## Features

- Transfer data between two SQLite databases.
- Automatically fetches data from the source database.
- Inserts data into the destination database.
- Handles column names and data insertion dynamically.

## Prerequisites

- Python 3.x
- `sqlite3` library (included with Python by default)

## Setup

1. Clone the repository:

```bash
   git clone https://github.com/NovaLeg/sqlite-data-transfer.git
   cd sqlite-data-transfer
```
2. Modify the source_db, destination_db, and table variables in the script to match your databases and table:
```bash
source_db = 'source.db'
destination_db = 'destination.db'
table = 'put_your_table_name'
```
- Replace `'source.db'` with the path to your source SQLite database.
- Replace `'destination.db'` with the path to your destination SQLite database.
- Replace `'your_table_name'` with the name of the table you want to transfer.
3. Run the transfer script:
  ```bash
  python db.py
  ```

## How It Works

- The script connects to both the source and destination SQLite databases.
- It fetches all rows from the specified table in the source database.
- It inserts the fetched data into the same table in the destination database.
- If no data is found, it will output `No data to transfer.`.
