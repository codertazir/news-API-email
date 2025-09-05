
import requests
from send_email import semail
import os


# Pakistani Newssss:

# Topic
topic = 'Politics and Pakistan'

# Get API key and URL
api = os.getenv("API")
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2025-09-01&" \
      "sortBy=publishedAt&" \
      f"apiKey={api}&" \
      "language=en"

# Make a request
request = requests.get(url)

# Convert to dictionary
content = request.json()

# Add subject
body = "Subject: Today's Pakistani News" + '\n'

# Access the article titles and descriptions and send email
for article in content['articles'][:20]:
    if article['title'] is not None and article['description'] is not None:
        body += article['title'] + '\n' \
        + article['description'] + '\n' \
        + article['url'] +2*'\n'

body = body.encode('utf-8')
semail(body)


# World Newssss:

# New topic and URL
topic = 'News'
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2025-09-01&" \
      "sortBy=publishedAt&" \
      f"apiKey={api}&" \
      "language=en"

# Make a request
request = requests.get(url)

# Convert to dictionary
content = request.json()

# Add subject
body = "Subject: Today's World News" + '\n'

# Access the article titles and descriptions and send email
for article in content['articles'][:20]:
    if article['title'] is not None and article['description'] is not None:
        body += article['title'] + '\n' \
        + article['description'] + '\n' \
        + article['url'] +2*'\n'

body = body.encode('utf-8')
semail(body)
