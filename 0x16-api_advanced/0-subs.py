#!/usr/bin/python3
"""Reddit API and returns the number total subscribers"""
import requests


def number_of_subscribers(subreddit):
    headers = {
        'User-Agent': 'Chrome/76.0.3809.132 (mesakmegerem@gmail.com)'
    }
    response = requests.get('https://www.reddit.com/r/{:}/about.json'.format(
        subreddit), headers=headers, allow_redirects=False)
    if response.status_code >= 300:
        return 0
    json = response.json()
    data_dict = json.get('data')
    return(data_dict.get('subscribers'))
