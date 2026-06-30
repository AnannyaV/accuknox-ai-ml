# AccuKnox AI-ML Assignment
Python-based solutions for API integration, SQLite databases, data processing, visualization, and machine learning concepts.

### Problem 1: API Data Retrieval and Storage

**Objective**:
In this problem, I used the FreeAPI Books API to fetch book details and store the retrieved data in a local SQLite database.

**Approach**
- Sent a GET request to the FreeAPI Books endpoint using the `requests` library.
- The API response contained multiple (2) pages, so I fetched data from both pages.
- Extracted only the required information such as title, author and publication year from the JSON response.
- Converted the extracted data into a Pandas DataFrame.
- Saved the DataFrame into a SQLite database (`books.db`) using `to_sql()`.
- Stored the database in the same folder as the Python script using `os.path.join()`.

**Output**
- `books.db`
- Console output showing the retrieved records.

### Problem 2: Data Processing and Visualization

**Objective**:
In this problem, I used the FreeAPI random users API to fetch user details, assigned sample scores to each user, calculated the average score and visualized the data.

**Approach**
- Retrieved user details from the FreeAPI Random Users API.
- Since the API does not contain student scores, I assigned sample scores for demonstration.
- Created a Pandas DataFrame containing student names and scores.
- Calculated the average score using Pandas.
- Generated a bar chart using Matplotlib.
- Saved the chart as `result.png` in the same directory.

**Output**
- `result.png`
- Average score displayed in the terminal.

### Problem 3: CSV Data Import to SQLite

**Objective**:
In this problem, I read user information from a CSV file and stored it in a SQLite database.

**Approach**
- Read the CSV file (`users.csv`) using Pandas.
- Loaded the data into a DataFrame.
- Created a SQLite database (`users.db`).
- Inserted all records into the `users` table using `to_sql()`.
- Stored the database in the same folder as the script.

**Output**
- `users.db`
- Console output confirming successful import.

## How to Run

1. Clone the repository.
```bash
git clone https://github.com/AnannyaV/accuknox-ai-ml.git
```

2. Navigate to the project directory.
```bash
cd accuknox-ai-ml
```

3. Install the required dependencies.
```bash
pip install -r requirements.txt
```

4. Run the required problem.
Example:
```bash
python Assignment1/problem1_api_sqlite/main.py
```

Similarly,
```bash
python Assignment1/problem2_data_visualization/main.py
```

```bash
python Assignment1/problem3_csv_sqlite/main.py
```
