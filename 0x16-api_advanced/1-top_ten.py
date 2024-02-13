#!/usr/bin/python3
"""Thsi for Reddit API and returns the top 10"""
import requests


def top_ten(subreddit):
    try:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        reques = requests.get(
            url, allow_redirects=False, headers={
                'User-Agent': 'FanComprehensive8698'},
            params={'limit': 10})

        leje = reques.json().get('data').get('children')
        for le in leje:
            print(le.get('data').get('title'))
    except ConnectionError:
        print(None)
