import praw

reddit = praw.Reddit()
print(reddit.read_only)
keyworda = ['depressed', 'unhappy', 'bullied']
subreddit = reddit.subreddit('python');
hot_python = subreddit.hot(5)
content = {}
for submissions in hot_python:
    
    print(submissions.title)


