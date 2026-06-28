import requests
import pandas as pd
import sqlite3
import os

def fetch_books_data_freeapi():
    base_url = "https://api.freeapi.app/api/v1/public/books"
    books_list = []

    # Fetch data from the API for 2 pages
    for page in range(1, 3):
        url = f"{base_url}?page={page}&limit=10&inc=kind%2Cid%2Cetag%2CvolumeInfo&query=tech"
        response = requests.get(url)
        data = response.json()
        if data["success"] and "data" in data:
            books = data["data"]["data"]

            # Extract relevant information from each book and append to the list
            for book in books:
                volume_info = book.get("volumeInfo", {})
                books_list.append({
                    "title": volume_info.get("title"),
                    "author": ", ".join(volume_info.get("authors", [])),
                    "publish_year": volume_info.get("publishedDate", "").split("-")[0]
                })
        else:
            raise Exception("API request failed or returned no data.")

    return books_list

def main():
    try:
        books_data = fetch_books_data_freeapi()
        
        # Create a DataFrame from the fetched data
        df = pd.DataFrame(books_data)
        print(df.head())

        # Store the DataFrame in a SQLite database
        db_path = os.path.join(os.path.dirname(__file__), "books.db")
        conn = sqlite3.connect(db_path)

        df.to_sql("books", conn, if_exists="replace", index=False)

        conn.close()

        print("Data stored successfully!")

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()