"""An application that gets the latest news from https://en.wikipedia.org/wiki/List_of_public_corporations_by_market_capitalization and displays the top 5 news articles

Using requests and BeautifulSoup to scrape the table of trillion dollar companies from Wikipedia and display the top 5 companies by market capitalization.
"""

import requests
import pandas as pd
from io import StringIO
import seaborn as sns
import matplotlib.pyplot as plt

# Get the website and if the request was successful
try:
    website = requests.get(
        "https://en.wikipedia.org/wiki/List_of_public_corporations_by_market_capitalization"
    )
    website.raise_for_status()  # Raise an exception if the request was not successful
    print("Request successful wuth status code:", website.status_code)
except requests.exceptions.HTTPError as err:
    print(f"Request failed: {err}")

# grab the second table from the website
table = pd.read_html(StringIO(website.text))[1].head()  # Display the first 5 rows of the table

# dataset before cleaning
print("====================================")
print("Dataset before cleaning")
print(table.transpose())

# Define a regex pattern to match the company name and the numbers
pattern = r'(?P<Company>\D+)(?P<Numbers>\d+,\d+)'

# Apply the pattern to each quarter column separately
table['company'], table['performance_Q1'] = table['First quarter.1'].str.extract(pattern).values.T
_, table['performance_Q2'] = table['Second quarter.1'].str.extract(pattern).values.T
_, table['performance_Q3'] = table['Third quarter.1'].str.extract(pattern).values.T
_, table['performance_Q4'] = table['Fourth quarter.1'].str.extract(pattern).values.T

# Remove commas from performance columns and convert to float
for col in ['performance_Q1', 'performance_Q2', 'performance_Q3', 'performance_Q4']:
    table[col] = table[col].str.replace(',', '').astype(float)

# Since the numbers are in millions, multiply by a million
for col in ['performance_Q1', 'performance_Q2', 'performance_Q3', 'performance_Q4']:
    table[col] = table[col] * 1e6

table = table[['company', 'performance_Q1', 'performance_Q2', 'performance_Q3', 'performance_Q4']]
print("====================================")
print("Dataset after cleaning")
print(table)

# Get the unique company names
companies = table['company'].unique()

# Melt the entire table to a long format suitable for line plot
table_melted = table.melt(id_vars='company', var_name='Quarter', value_name='Performance')

# rename row entries in the column 'performance_Q1', 'performance_Q2', 'performance_Q3', 'performance_Q4' 
# to 'Q1', 'Q2', 'Q3', 'Q4'
table_melted['Quarter'] = table_melted['Quarter'].str.replace('performance_', '')

print("====================================")
print("Dataset after melting")

print(table_melted)

# Get the unique company names
companies = table_melted['company'].unique()

# Determine the layout of the subplots
n = len(companies)
ncols = 3  # Number of columns
nrows = n // ncols + (n % ncols > 0)  # Number of rows

# Create a figure with multiple subplots
fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(15, nrows*5))

# Flatten the axes array
axes = axes.flatten()

# Create a separate line plot for each company
for i, company in enumerate(companies):
    # Subset the table for the current company
    table_subset = table_melted[table_melted['company'] == company]
    
    # Create a line plot on the current subplot
    sns.lineplot(data=table_subset, x='Quarter', y='Performance', ax=axes[i])
    
    # Set the title for the current subplot
    axes[i].set_title(company)

# Remove the unused subplots
for i in range(n, len(axes)):
    fig.delaxes(axes[i])

# Show the plot
plt.tight_layout()
print("====================================")
print("Plotting the data")
plt.savefig('plot.png')
plt.show()

# Exercise: Try to plot more 10 companies and try to plot the data in a different way
# Exercise: Use a communication API to send the plot to a user using Africa's Talking APIs