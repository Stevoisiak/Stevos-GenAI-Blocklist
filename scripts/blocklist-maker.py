"""Creates filters for AI subreddits on Reddit."""

with open('reddit.txt', 'r') as file:
    reddit_list = file.read().splitlines()


# -- https://www.reddit.com/
# Posts from AI Subreddit
test = 'www.reddit.com##shreddit-post:is([subreddit-name="' + '"],[subreddit-name="'.join(reddit_list) + '"])'
print(test + '\n')

# Right sidebar - Recent posts from AI subreddits
test = 'www.reddit.com##[slot="posts"] > div:has(faceplate-hovercard:is([label="r/' + '"],[label="r/'.join(reddit_list) + '"]))'
print(test + '\n')

# https://www.reddit.com/search/?q=ai (Search results)
# Media & Posts from AI subreddits
test = 'www.reddit.com##search-telemetry-tracker[view-events="search/view/post"]:has([aria-haspopup="dialog"]:is([href="/r/' + '/"],[href="/r/'.join(reddit_list) + '/"]))'
print(test + '\n')

# Search communities
test = 'www.reddit.com##[data-testid="search-community"]:has(a:is([href="/r/' + '/"],[href="/r/'.join(reddit_list) + '/"]))'
print(test + '\n')

# ============================

# -- https://old.reddit.com/
# Top navbar > My Subreddits - AI Subreddits
test = 'old.reddit.com##.sr-bar > li:has(> :is([href$="/r/' + '/"],[href$="/r/'.join(reddit_list) + '/"]))'
print(test + '\n')

# Post from AI subreddit
test = 'old.reddit.com##.link:is([data-subreddit="' + '"],[data-subreddit="'.join(reddit_list) + '"])'
print(test + '\n')

# -- https://old.reddit.com/search?q=ai+art
# Search result from AI Subreddit
test = 'old.reddit.com##.search-result:has( .search-subreddit-link:is([href$="/r/' + '/"],[href$="/r/'.join(reddit_list) + '/"]))'
print(test + '\n')

# -- https://old.reddit.com/subreddits/search?q=ai
test = 'old.reddit.com##.subreddit:has([data-sr_name="' + '"],[data-sr_name="'.join(reddit_list) + '"])'
print(test)
