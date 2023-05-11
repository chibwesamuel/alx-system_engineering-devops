#!/usr/bin/python3
"""
Returns a list containing the titles of all hot articles for a given subreddit
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """Queries the Reddit API recursively and returns a list of titles"""
    if len(hot_list) == 0 and after is None:
        url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot/.json?after={}".format(subreddit, after)

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return (None)

    data = response.json().get("data")
    after = data.get("after")
    children = data.get("children")

    for child in children:
        title = child.get("data").get("title")
        hot_list.append(title)

    if after is not None:
        return (recurse(subreddit, hot_list, after))
    else:
        return (hot_list)
