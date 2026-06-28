import requests
import pandas as pd
import matplotlib.pyplot as plt
import os


def fetch_users_data_freeapi():

    base_url = "https://api.freeapi.app/api/v1/public/randomusers"

    users = []

    # Predefined scores for the 20 users
    scores = [85, 78, 92, 88, 76, 81, 95, 89, 84, 90,
              37, 51, 80, 26, 93, 79, 82, 94, 83, 88]

    score_index = 0

    # Fetch data from the API for 2 pages (10 users per page)
    for page in range(1, 3):

        url = f"{base_url}?page={page}&limit=10"

        response = requests.get(url)

        data = response.json()

        if data["success"] and "data" in data:

            users_data = data["data"]["data"]

            # Extract relevant information from each user and append to the list
            for user in users_data:

                name = user.get("name", {})

                users.append({
                    "name": f"{name.get('title', '')} {name.get('first', '')} {name.get('last', '')}".strip(),
                    "score": scores[score_index]
                })

                score_index += 1

        else:
            raise Exception("API request failed or returned no data.")

    return users


def main():

    try:
        
        users_data = fetch_users_data_freeapi()

        # Create a DataFrame from the fetched data
        df = pd.DataFrame(users_data)

        print(df)

        average = df["score"].mean()

        print("\nAverage Score:", round(average, 2))

        # Create a bar chart to visualize the scores of the students
        plt.figure(figsize=(10, 5))
        plt.bar(df["name"], df["score"])
        plt.title("Students Test Scores")
        plt.xlabel("Students")
        plt.ylabel("Score")
        plt.xticks(rotation=45)
        plt.tight_layout()

        image_path = os.path.join(os.path.dirname(__file__), "result.png")

        plt.savefig(image_path)
        plt.show()

        print("\nBar chart saved successfully!")

    except Exception as e:

        print(e)


if __name__ == "__main__":
    main()