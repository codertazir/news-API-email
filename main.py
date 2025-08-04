
import requests
from send_email import semail

api = "2bb83344f26f4411b6f0c49692b7a9ff"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-07-04&" \
"sortBy=publishedAt&apiKey=2bb83344f26f4411b6f0c49692b7a9ff"

# Make a request
request = requests.get(url)

# Convert to dictionary
content = request.json()

# Access the article titles and descriptions and send email
body = ''
for article in content['articles']:
    if article['title'] is not None and article['description'] is not None:
        body += article['title'] + '\n' + article['description'] + 2*'\n'

body = body.encode('utf-8')
semail(body)
