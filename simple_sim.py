import numpy 
from sklearn.metrics import jaccard_score
from collections import defaultdict
import json
import random

def jaccard(s1, s2):
    numer = len(s1.intersection(s2))
    denom = len(s1.union(s2))
    if denom == 0:
        return 0
    return numer/denom

with open('data/cleaned/RC_2023-01_2.json', 'r') as fh:
    comments = json.load(fh)

# item definition - subreddits
# users definition - reddit users
usersperitem = defaultdict(set)
itemsperuser = defaultdict(set)
item_name = defaultdict()
for comment in comments:
    user = comment['author']
    item = comment['subreddit_id']
    item_name[item] = comment['subreddit']
    usersperitem[item].add(user)
    itemsperuser[user].add(item)


def most_similar_jaccard(i, N = 10):
    similarity  = []
    users = usersperitem[i]
    for i2 in usersperitem:
        if i == i2: continue
        sim = jaccard(users, usersperitem[i2])
        i2 = item_name[i2]
        similarity.append((sim, i2))
    similarity.sort(reverse=True)
    return similarity[:N]

sample_item = list(usersperitem.keys())[random.randint(0, len(usersperitem.keys()))]
sample_item_name = item_name[sample_item]

similar_item = most_similar_jaccard(sample_item)

print(similar_item)
print(sample_item_name)
for sim_item in similar_item:
    item = sim_item[1]
    print(item)

