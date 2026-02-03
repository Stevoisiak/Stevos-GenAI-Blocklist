# Stevo's GenAI Blocklist

Set of uBlock Origin filters intended to block generative AI features on various websites.

## Image comparison

Before:

<img width="794" height="457" alt="image" src="https://github.com/user-attachments/assets/65f65ca9-7022-4455-99f2-4d1a44051a1d" />

After:

<img width="791" height="456" alt="image" src="https://github.com/user-attachments/assets/0698522f-54ed-4653-9fcc-ca847406ba3e" />

## Installation
### For Firefox, Edge, or Opera
- Install [uBlock Origin](https://ublockorigin.com/)
- Click [this link](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt&title=Stevo's%20GenAI%20Blocklist)
- Press "Subscribe" to import the filter list. 

### For Brave
- Open *Settings > Shields > Content filtering*.
- Under "Add custom filter lists", enter `https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt`
- Click *Add*.

### For Google Chrome
- Install [uBlock Origin Lite](https://chromewebstore.google.com/detail/ublock-origin-lite/ddkjiahejlhfcafbddmgiahcphecmpfh?hl=en)
- Download and save the [filter list](https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt) (Right Click, Save As)
- Click the uBlock icon in your browser and hit the options button
- Go to "Custom Filters"
- At the bottom, click "Import/Export", then "Import and append..."
- Select the saved filter list file

*Note: uBlock Origin Lite does not support automatically updating custom filter lists. If you want to update, you will need to clear the prior rules and re-import.*

### For Safari (iOS)
- Install [uBlock Origin Lite](https://apps.apple.com/us/app/ublock-origin-lite/id6745342698)
- Download and save the [filter list](https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt) (Long press link, Download Linked File)
- Open *Settings > Apps > Safari > Extensions > uBlock Origin Lite*
- Enable "Allow Extension"
  - (Optional) Enable "Allow in Private Browsing"
- Under "Permissions", click "All Websites" and select "Allow"
- Press the back arrow in the top left
- Select "Settings"
- Open the "Custom filters" tab
- Open "Import/Export", then press "Import and append..."
- Open "Downloads" folder and select "GenAI-Blocklist"

*Note: uBlock Origin Lite does not support automatically updating custom filter lists. If you want to update, you will need to clear the prior rules and re-import.*

## Examples of blocked content
* Boorus: Images tagged as AI generated
* Deviantart: DreamUp ads
* Facebook: AI chat
* GitHub: Copilot buttons
* Google: AI Summaries
* YouTube: Ask button & live chat summaries
* YouTube Studio: Inspiration tab
* X: Grok buttons

## Other AI blocking projects

* [uBlockOrigin Huge AI Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist) - Blocklist for search engines to remove AI generated images
* [Soul Over AI](https://github.com/xoundbyte/soul-over-ai) - Index of AI-generated and AI-assisted music
* [Blocklist for AI music on YouTube](https://surasshu.com/blocklist-for-ai-music-on-youtube/) - Blocklist of AI music channels on YouTube for the Blocktube extension.
* [Spotify AI Band Blocker](https://github.com/Reginald-Gillespie/Spotify-AI-Band-Blocker) - Plugin for Spicetify to block AI artists on Spotify.
* [Spotiy AI Blocker](https://github.com/CennoxX/spotify-ai-blocker) - Userscript to block AI artists on Spotify
