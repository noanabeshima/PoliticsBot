from post_to_market import create_market_from_post
import feedparser
import json

rss_url = 'https://sfstandard.com/politics-policy/feed'

feed = feedparser.parse(rss_url)

with open('title_to_post.json', 'r') as f:
    title_to_post = json.load(f)

for post in feed.entries:
    title = post['title']
    if title not in title_to_post:
        create_market_from_post(post)
        title_to_post[title] = post

with open('title_to_post.json', 'w') as f:
    json.dump(title_to_post, f, indent=2)