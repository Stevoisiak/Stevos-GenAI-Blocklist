deviantart_user_list = []
# Image previews
deviantart_filter = 'www.deviantart.com##div.V_S0t_[data-testid="content_row"] > div:not(.m_4A2n):has(a[href^="{username}"])'

youtube_user_list = []
youtube_filter_list =[
    # Search - Video Result
    'www.youtube.com##ytd-video-renderer:has(a#channel-thumbnail[href="/@{username}"])',
    # Search - Channel Result
    'www.youtube.com##div.ytd-channel-renderer[id="content-section"]:has(div#avatar-section > a.channel-link[href="/@{username}"])',
    # Video - Right sidebar - Recommended video
    'www.youtube.com##ytd-item-section-renderer > div#contents > yt-lockup-view-model:has(span.yt-core-attributed-string:has-text("{username}"))'
]

# Get usernames
with open('Username-Lists\\deviantart.txt', 'r') as file:
    deviantart_user_list = file.read().splitlines()

with open('Username-Lists\\youtube.txt', 'r') as file:
    youtube_user_list = file.read().splitlines()

# Write filter list
with open('Username-Lists\\username-filters.txt', 'w') as file:
    file.write("! Deviantart\n")
    for user in deviantart_user_list:
        file.write(deviantart_filter.format(username=user) + '\n')

    file.write("! YouTube\n")
    for filter in youtube_filter_list:
        for user in youtube_user_list:
            file.write(filter.format(username=user) + '\n')

    