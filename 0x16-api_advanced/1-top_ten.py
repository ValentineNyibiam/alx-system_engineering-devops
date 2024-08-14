#!/usr/bin/python3
"""
This is a module that defines a query function
"""

from requests import get


def top_ten(subreddit):
    """
    This is a function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a given subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    params = {'limit': 10}
    cHeader = {'user-agent': 'Chrome/42.0.2311.135', "Accept": "application/json"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    subreddits_abt = get(url, headers=cHeader)

    abt_json =  subreddits_abt.json()
#if abt_json.get('data') and abt_json.get('children'):
    posts = abt_json["data"]["children"]
    for post in posts:
    	print(post["data"]["title"])
   # try:

#top_ten("programming")
