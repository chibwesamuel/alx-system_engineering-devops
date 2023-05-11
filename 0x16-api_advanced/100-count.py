#!/usr/bin/python3
"""
Recursive function that queries the Reddit API
"""
import requests

def count_words(subreddit, word_list, after=None, instances={}):
    """Parses the title of all hot articles, and prints a sorted count of given keywords"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    data = results.get("data")
    after = data.get("after")
    children = data.get("children")

    for child in children:
        title = child.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                if word.lower() not in instances:
                    instances[word.lower()] = 0
                instances[word.lower()] += title.count(word.lower())

    if after is None:
        if len(instances) == 0:
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        for word, count in instances:
            print("{}: {}".format(word, count))
    else:
        count_words(subreddit, word_list, after, instances)


# Example usage
subreddit = "python"
word_list = ["python", "programming", "tutorial"]
count_words(subreddit, word_list)
