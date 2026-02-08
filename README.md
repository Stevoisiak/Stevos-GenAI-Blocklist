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
- Press "Subscribe" to import the filter list.

#### Manual import
If the automatic import didn't work, (possibly due to multiple adblockers being installed), try the following:
- Install [uBlock Origin](https://ublockorigin.com/).
- Click the uBlock button in the toolbar and open Dashboard Settings (gear icon)
- Select the *Filter lists* tab
- Open the *Import...* section and paste `https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt`
- Click "Apply Changes"

If done correctly, you should see "_Stevo's GenAI Blocklist_" listed under "_Custom_".

### For Brave
- Open *Settings > Shields > Content filtering*.
- Under "Add custom filter lists", enter `https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt`
- Click *Add*.

### For Google Chrome
- Install [uBlock Origin Lite](https://chromewebstore.google.com/detail/ublock-origin-lite/ddkjiahejlhfcafbddmgiahcphecmpfh?hl=en)
- Download and save [`GenAI-Blocklist.txt`](https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt) (Right Click > Save link as...)
- Click the uBlock icon in your browser and hit the options button
- Go to "Custom Filters"
- At the bottom, click "Import/Export", then "Import and append..."
- Select the filter list file (`GenAI-Blocklist.txt`) you downloaded in step 2.

*Note: uBlock Origin Lite does not support automatically updating custom filter lists. If you want to update, you will need to clear the prior rules and re-import.*

### For Safari (iOS)

- Install [uBlock Origin Lite](https://apps.apple.com/us/app/ublock-origin-lite/id6745342698)
- Download and save [`GenAI-Blocklist.txt`](https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt) (Long press > Download Linked File)
- Open *Settings > Apps > Safari > Extensions > uBlock Origin Lite*
- Enable "Allow Extension"
  - (Optional) Enable "Allow in Private Browsing"
- Under "Permissions", click "All Websites" and select "Allow"
- Press the back arrow in the top left
- Select "Settings"
- Open the "Custom filters" tab
- Open "Import/Export", then press "Import and append..."
- Open "Downloads" folder and select `GenAI-Blocklist.txt`

*Note 1: You may need to wait a few minutes before filter rules take effect. (Possibly related to [rule conversion](https://github.com/user-attachments/assets/7d6419cd-a465-42c4-85db-803aeb8ab8f5))*

*Note 2: uBlock Origin Lite does not support automatically updating custom filter lists. If you want to update, you will need to clear the prior rules and re-import.*

### For Opera

Unfortunately, this filter list does not currently work in Opera.

Importing the filters had no effect when testing with both uBlock Origin and Opera's built in ad blocking. ([May be an issue with Opera](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/issues/64))

## Optional account blocklist
There is an additional optional filterlist [`GenAI-Account-Blocklist.txt`](https://github.com/Stevoisiak/Stevos-GenAI-Blocklist/blob/main/GenAI-Account-Blocklist.txt) that blocks accounts and subreddits that post AI generated content. This list is much less thorough and is still a work in progress.

These filters were previously part of the main blocklist, but it was split off as a separate list you can toggle on and off.

## Contributing guidelines

If you want to file an issue or submit a pull request for an item that isn't being blocked, please include the URL where the unblocked item appears and a screenshot of the page showing the unblocked item.

## Other AI blocking projects

* [uBlockOrigin Huge AI Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist) - Blocklist for search engines to remove AI generated images
* [Just the Browser](https://justthebrowser.com/) - Removes AI features, telemetry, and sponsored content from deskop web browsers
* [Soul Over AI](https://github.com/xoundbyte/soul-over-ai) - Index of AI-generated and AI-assisted music
* [Blocklist for AI music on YouTube](https://surasshu.com/blocklist-for-ai-music-on-youtube/) - Blocklist of AI music channels on YouTube for the Blocktube extension.
* [Spotify AI Band Blocker](https://github.com/Reginald-Gillespie/Spotify-AI-Band-Blocker) - Plugin for Spicetify to block AI artists on Spotify.
* [Spotiy AI Blocker](https://github.com/CennoxX/spotify-ai-blocker) - Userscript to block AI artists on Spotify
