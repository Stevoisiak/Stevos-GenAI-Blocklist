# Stevo's GenAI Blocklist

Set of uBlock Origin filters intended to block generative AI features on various websites.

## Examples of blocked content
* Google's AI summaries
* YouTube's Ask button, AI summaries, & "Inspiration" tab
* GitHub's Copilot buttons
* X/Twitter's Grok buttons
* Microsoft 365's Copilot buttons
* Amazon Rufus's product and review summaries
* DeviantArt's DreamUp ads
* Facebook's AI chat
* Reddit Answers
* Booru images tagged as AI generated

## Image comparison

Before:

<img width="794" height="457" alt="image" src="https://github.com/user-attachments/assets/65f65ca9-7022-4455-99f2-4d1a44051a1d" />

After:

<img width="791" height="456" alt="image" src="https://github.com/user-attachments/assets/0698522f-54ed-4653-9fcc-ca847406ba3e" />

## Installation
### For Firefox or Microsoft Edge
#### Automatic import
- Install [uBlock Origin](https://ublockorigin.com/).
- Left-click [this link](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt&title=Stevo's%20GenAI%20Blocklist).
- Press "_Subscribe_" to import the filter list.

#### Manual import
If the automatic import didn't work, (possibly due to multiple adblockers being installed), try the following:
- Install [uBlock Origin](https://ublockorigin.com/).
- Click the uBlock button in the toolbar and open Dashboard Settings (gear icon)
- Select the "_Filter lists_" tab
- Open the "_Import..._" section and paste `https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt`
- Click "_Apply Changes_"

If done correctly, you should see "**_Stevo's GenAI Blocklist_**" listed under "**_Custom_**".

### For Brave
- Open _Settings > Shields > Content filtering_.
- Under "_Add custom filter lists_", enter `https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt`
- Click _Add_.

### For Google Chrome
- Install [uBlock Origin Lite](https://chromewebstore.google.com/detail/ublock-origin-lite/ddkjiahejlhfcafbddmgiahcphecmpfh?hl=en)
- Open [`GenAI-Blocklist.txt`](https://github.com/Stevoisiak/Stevos-GenAI-Blocklist/blob/main/GenAI-Blocklist.txt)
- Click the "Copy raw file" button (⮺). ([screenshot](https://github.com/user-attachments/assets/e8e8c75a-2718-431e-b48b-1bb8b1ba418e))
- Click the uBlock icon in Chrome and click the gear icon ([screenshot](https://github.com/user-attachments/assets/6d8a4ee7-e986-417a-a164-07e66a14f31e))
- Go to "_Custom filters_"
- At the bottom, click "_Import/Export_" to open the filter box ([screenshot](https://github.com/user-attachments/assets/fad4141f-1008-44ac-919f-1a5c58f322c2))
- Right click the filter box and hit "_Paste_"
- Click the "_Add_" button

*Note: uBlock Origin Lite does not support automatically updating custom filter lists. If you want to update, you will need to clear the prior rules and re-import.*

### For Safari (iOS)

- Install [uBlock Origin Lite](https://apps.apple.com/us/app/ublock-origin-lite/id6745342698)
- Open [`GenAI-Blocklist.txt`](https://github.com/Stevoisiak/Stevos-GenAI-Blocklist/blob/main/GenAI-Blocklist.txt)
- Press the action menu button (⋯) and select "_Copy_" 
- From your homescreen, open _Settings > Apps > Safari > Extensions > uBlock Origin Lite_
- Enable "_Allow Extension_" ([screenshot](https://github.com/user-attachments/assets/942b6e12-f6ca-4eb3-8557-44c75590c7d6))
  - (Optional) Enable "_Allow in Private Browsing_"
- Under "_Permissions_", click "_All Websites_" and select "_Allow_"
- Press the back arrow in the top left, then select "_Settings_"
- Open the "_Custom filters_" tab
- Scroll to the bottom and tap "_Import/Export_"
- Tap the filter box twice and select "_Paste_"
- Tap the "_Add_" button

*Note 1: You may need to wait a few minutes before filter rules take effect. (Possibly related to [rule conversion](https://github.com/user-attachments/assets/af249ccb-fa8e-441c-b518-acc9bd1875df))*

*Note 2: uBlock Origin Lite does not support automatically updating custom filter lists. If you want to update, you will need to clear the prior rules and re-import.*

*Note 3: The filter list was primarilly designed for the base uBlock Origin and may not always work on the Lite version. For example, AI elements may appear on a site, only to dissapear after refreshing*

### For Opera

Unfortunately, this filter list does not currently work in Opera.

Importing the filters had no effect when testing with both uBlock Origin and Opera's built in ad blocking. ([May be an issue with Opera](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/issues/64))

## Optional extra blocklist
There is an additional optional filterlist [`GenAI-Blocklist-Extra.txt`](https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist-Extra.txt) with additional blocks. These are more subjective blocks and may be more prone to accidentally blocking some non-AI content. These include:
* DeviantArt: Images from accounts that have posted AI images
* Reddit: Posts from AI-focused subreddits 
* X: Any post from Grok account

These filters were previously part of the main blocklist, but it was split off as a separate list you can toggle on and off.

## Contributing guidelines

If you want to file an issue or submit a pull request for an item that isn't being blocked, please include the URL where the unblocked item appears and a screenshot of the page showing the unblocked item.

## Other AI blocking projects

* [uBlockOrigin Huge AI Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist) - Blocklist for search engines to remove AI generated images
* [Just the Browser](https://justthebrowser.com/) - Removes AI features, telemetry, and sponsored content from deskop web browsers
* [Soul Over AI](https://github.com/xoundbyte/soul-over-ai) - Index of AI-generated and AI-assisted music
* [Blocklist for AI music on YouTube](https://surasshu.com/blocklist-for-ai-music-on-youtube/) - Blocklist of AI music channels on YouTube for the Blocktube extension.
* [Spotify AI Band Blocker](https://github.com/Reginald-Gillespie/Spotify-AI-Band-Blocker) - Plugin for Spicetify to block AI artists on Spotify.
* [Spotify AI Blocker](https://github.com/CennoxX/spotify-ai-blocker) - Userscript to block AI artists on Spotify
* 
## Feedback

If you want to report an AI widget that is unblocked, please [submit an issue](https://github.com/Stevoisiak/Stevos-GenAI-Blocklist/issues) and include the website URL and a screenshot of the unblocked item. 

If you have any feedback about this project, I can be reached on Bluesky at [@stevoisiak.bsky.social](https://bsky.app/profile/stevoisiak.bsky.social).
