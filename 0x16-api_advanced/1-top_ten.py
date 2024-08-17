#!/usr/bin/python3
"""
prints the titles of the first 10 hot
posts listed for a given subreddit
"""

from requests import get


def top_ten(subreddit):
    """
    function that queries the Reddit API
    and prints the titles of the first
    10 hot posts listed for a given subreddit
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = \
        {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    response = get(url, headers=user_agent, params=params, timeout=10)
    results = response.json()

    try:
        my_data = results.get('data').get('children')
        for i in my_data:
            print(i.get('data').get('title'))
    except (AttributeError, KeyError, TypeError) as e:
        print(f"An unexpected error occured: {e}")
