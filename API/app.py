"""
Use the newsapi to get the latest news about Artificial Intelligence and Machine Learning 
by querying the newsapi. (You try something else
Use JSON normalize pandas method to format the JSON into a dictionary
& chain it with polars to convert to a dataframe and finally store the
file in memory.
"""
import os
import requests
import polars as pl
import pandas as pd
from tenacity import retry, stop_after_attempt, wait_fixed


# Get the API key from the environment variable
API_KEY = os.getenv("NEWS_API_KEY")

# Make a request to the news API
URL = f"https://newsapi.org/v2/everything?q=Artificial Intelligence, Machine Learning&apiKey={API_KEY}"

# retry the request 3 times with a 1 second wait time
# if an error occurs show the error and raise the error
@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def make_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.status_code)
        return response
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        raise err
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
        raise err
    except Exception as err:
        print(f"An unexpected error occurred: {err}")
        raise err

response = make_request(URL)

# Convert the response to a DataFrame
data = response.json()

print("Data before normalization")
print("====================================")
print(data['articles'])

# normalize the JSON data
norm_json = pd.json_normalize(data['articles'])

# Convert the DataFrame to a Polars DataFrame
pl_df = pl.from_pandas(norm_json)

print("====================================")
print("Convert the DataFrame to a Polars DataFrame")


# Display a random sample of 5 articles
top_articles = pl_df.sample(n=5)
print(top_articles)

# store the data in a CSV file
print("====================================")
pl_df.write_csv("news_articles_ml_ai.csv")


# Exercise: Create a function that takes in a keyword and returns the top 5 news articles about that keyword
# Exercise: Use a communication API to send the data to a client
