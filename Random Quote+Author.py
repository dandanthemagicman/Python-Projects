import requests

def get_random_quote():
    # URL of the random quote API
    url = "https://api.quotable.io/random"

    # Send an HTTP GET request to the API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        quote_data = response.json()

        # Extract the quote text and author
        quote = quote_data["content"]
        author = quote_data["author"]

        return f'"{quote}" - {author}'
    else:
        return "Failed to retrieve a random quote."

# Generate and print a random quote
random_quote = get_random_quote()
print(random_quote)