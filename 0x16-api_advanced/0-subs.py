#!/usr/bin/python3
"""
This is a module that defines a query function
"""
from requests import get


def number_of_subscribers(subreddit):
    """
    This is a function that queries the Reddit API and returns
    the number of subscribers for a given subreddit
    """
    if subreddit is None or subreddit is str:
        return 0
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    cHeaders = {'user-agent': 'Chrome/42.0.2311.135'}

    subreddits = get(url, headers=cHeaders)
    results = subreddits.json()

    try:
        return results.get('data').get('subscribers')
    except Exception:
        return 0
