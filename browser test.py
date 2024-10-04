from openai import OpenAI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

client = OpenAI()

# Define the function to get search query from GPT
def get_search_query(messages, client):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=10,
        temperature=0.5,
    )
    return completion.choices[0].message.content.strip()

# Define the function to perform a Google search using Safari and Selenium
def perform_google_search(query):
    # Set up Safari WebDriver
    driver = webdriver.Safari()

    # Open Google
    driver.get("https://www.google.com")

    # Find the search box and input the query
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)  # Press Enter key

    # Wait for a few seconds to allow results to load
    time.sleep(5)

    # Close the browser after performing the search
    driver.quit()

# Define the prompt to get search query from GPT
messages = [
        {"role": "system", "content": "You are an autonomous AI. You are tasked with performing a Google search."},
            {"role": "user", "content": "What are intellectual subjects are you interested in? Use three words to describe them."},
            ]
# Get the search query using GPT model
search_query = get_search_query(messages, client)

# Perform the Google search with the retrieved query
perform_google_search(search_query)

