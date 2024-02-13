#!/usr/bin/python3
"""
This for parses the title of all hot articles,
and prints a sorted count of given keywords
"""
import json
import requests


def count_words(subreddit, word_list, after="", count=[]):
    """parses the title of all hot articles,
    and prints a sorted count of given keywords"""

    if after == "":
        count = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url, params={'after': after},
                           allow_redirects=False,
                           headers={'user-agent': 'bhalut'})

    if request.status_code == 200:
        data = request.json()
        for ina in (data['data']['children']):
            for word in ina['data']['title'].split():
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        count[i] += 1
        after = data['data']['after']
        if after is None:
            yaze = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        yaze.append(j)
                        count[i] += count[j]
            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (count[j] > count[i] or
                            (word_list[i] > word_list[j] and
                             count[j] == count[i])):
                        iom = count[i]
                        count[i] = count[j]
                        count[j] = iom
                        iom = word_list[i]
                        word_list[i] = word_list[j]
                        word_list[j] = iom
            for i in range(len(word_list)):
                if (count[i] > 0) and i not in yaze:
                    print("{}: {}".format(word_list[i].lower(), count[i]))
        else:
            count_words(subreddit, word_list, after, count)
