
import requests

api = "2bb83344f26f4411b6f0c49692b7a9ff"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-07-04&" \
"sortBy=publishedAt&apiKey=2bb83344f26f4411b6f0c49692b7a9ff"

# Make a request
request = requests.get(url)

# Convert to dictionary
content = request.json()

# Access the article titles and descriptions
for article in content['articles']:
    print(article['title'])
    print(article['description'])
