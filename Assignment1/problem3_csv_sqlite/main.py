import pandas as pd
import sqlite3
import os


def import_csv_to_database():

    # Read the CSV file into a DataFrame
    csv_path = os.path.join(os.path.dirname(__file__), "users.csv")

    df = pd.read_csv(csv_path)

    # Store the DataFrame in a SQLite database
    db_path = os.path.join(os.path.dirname(__file__), "users.db")

    conn = sqlite3.connect(db_path)

    df.to_sql("users", conn, if_exists="replace", index=False)

    conn.close()

    return df


def main():

    try:
        
        # Import data from CSV to SQLite database
        users_data = import_csv_to_database()

        print(users_data)

        print("\nData imported successfully!")

    except Exception as e:

        print(e)


if __name__ == "__main__":

    main()