#!/usr/bin/python3
"""Reddit API and returns the number total subscribers"""
import requests


def number_of_subscribers(subreddit):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' +
            'AppleWebKit/537.36 (KHTML, like Gecko)' +
            'Chrome/121.0.0.0 Safari/537.36'
            }
    response = requests.get('https://www.reddit.com/r/{:}/about.json'.format(
        subreddit), headers=headers, allow_redirects=False)
    if response.status_code >= 300:
        return 0
    else:
        json = response.json()
        data_dict = json.get('data')
        return(data_dict.get('subscribers'))
