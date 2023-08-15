import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.reddit.com/r/programming/'

page = requests.get(url)

html = BeautifulSoup(page.text, "html.parser")

reddit_posts = html.find_all('shreddit-post')[0:3]

titles = []
upvotes = []
links = []

for post in reddit_posts:
  titles.append(post['post-title'])
  upvotes.append(post['score'])
  links.append('https://www.reddit.com' + post['permalink'])

data = {'Title': titles, 'Upvotes': upvotes, 'Links': links}
df = pd.DataFrame(data)

csv_filename = 'reddit_programming_posts.csv'
df.to_csv(csv_filename, index=False)