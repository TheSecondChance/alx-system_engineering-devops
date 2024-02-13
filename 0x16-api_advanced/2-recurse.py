#!/usr/bin/python3
"""Thsi for Reddit API and returns a list
containing the titles of all
hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' +
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }
    re = requests.get('https://www.reddit.com/r/{:}/hot.json?after={:}'.format(
        subreddit, after), headers=headers, allow_redirects=False)
    if re.status_code == 200:
        json = re.json()
        dataDict = json.get('data')
        listPost = dataDict.get('children')
        for post in listPost:
            dataDictPost = post.get('data')
            hot_list.append(dataDictPost.get('title'))
        after = dataDict.get('after')
        if dataDict.get('after') is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    else:
        return None
