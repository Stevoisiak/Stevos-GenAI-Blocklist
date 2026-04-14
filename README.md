# Stevo's GenAI Blocklist

A filter list for [uBlock Origin](https://github.com/gorhill/uBlock?tab=readme-ov-file#ublock-origin-ubo) and [AdGuard](https://adguard.com/en/adguard-browser-extension/overview.html) that hides specific website features that use or promote Generative AI.

Available for PC, ([Firefox](https://github.com/Stevoisiak/Stevos-GenAI-Blocklist?tab=readme-ov-file#firefox-microsoft-edge-or-waterfox-desktop), [Edge](https://github.com/Stevoisiak/Stevos-GenAI-Blocklist?tab=readme-ov-file#firefox-microsoft-edge-or-waterfox-desktop), [Chrome](https://github.com/Stevoisiak/Stevos-GenAI-Blocklist?tab=readme-ov-file#google-chrome-desktop), [Brave](https://github.com/Stevoisiak/Stevos-GenAI-Blocklist?tab=readme-ov-file#brave-desktop)), iOS ([Safari](https://github.com/Stevoisiak/Stevos-GenAI-Blocklist?tab=readme-ov-file#safari-ios), [Brave](https://github.com/Stevoisiak/Stevos-GenAI-Blocklist#brave-browser-ios)), and Android ([Firefox](https://github.com/Stevoisiak/Stevos-GenAI-Blocklist/tree/main?tab=readme-ov-file#firefox-android)).

## Examples of filtered content
* Google's AI summaries
* YouTube's Ask button, AI summaries, & "Inspiration" tab
* Copilot buttons on GitHub, Microsoft 365, and Azure Portal
* X/Twitter's Grok buttons
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
### Firefox, Microsoft Edge, or Waterfox (Desktop)
- Install [uBlock Origin](https://ublockorigin.com/).
- Left-click [this link](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt&title=Stevo's%20GenAI%20Blocklist).
- Press "_Subscribe_" to import the filter list.

If the above instructions didn't work, (possibly due to multiple adblockers being installed), you can try importing manually:

- Install [uBlock Origin](https://ublockorigin.com/).
- Click the uBlock button in the toolbar and open Dashboard Settings (gear icon)
- Select the "_Filter lists_" tab
- Open the "_Import..._" section and paste [`https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt`](https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt)
- Click "_Apply Changes_"

### Google Chrome (Desktop)

- Install [AdGuard Adblocker](https://chromewebstore.google.com/detail/adguard-adblocker/bgnkhhnnamicmpeenaelnjfhikgbkllg) for Chrome.
- Click the green AdGuard icon in Chrome then click the gear icon.
- Open the Filters tab, go to "Custom", and click the "extension settings" link.
- Enable "Allow User Scripts".
- Return to this page and left-click [this link](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt&title=Stevo's%20GenAI%20Blocklist).
- Under "Add custom filter", hit "Next" then "Add"

### Brave (Desktop)
- Open _Settings > Shields > Content filtering_.
- Under "_Add custom filter lists_", enter [`https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt`](https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt)
- Click _Add_.

### Firefox (Android)

- Open Firefox
- Tap the action menu (⋮) and select "_Extensions_"
- Click the plus (+) next to _uBlock Origin_ and install it
- Close and reopen the _Extensions_ menu
- Tap _uBlock Origin_ and select _Settings_
- Open the "_Filter lists_" tab
- Scroll to the bottom and tap "_Import..._"
- Paste in the link [`https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt`](https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt)
- Tap "_Apply Changes_"

### Safari (iOS)

- Install [AdGuard Ad Blocker for Safari](https://apps.apple.com/us/app/adguard-ad-blocker-for-safari/id1047223162)
- From your homescreen, Open *Settings > Apps > Safari > Extensions*
- Tap *AdGuard — Custom* and enable *Allow Extension*
  - (Optional) Enable "_Allow in Private Browsing_"
  - (Optional) Allow other AdGuard filters
- Open the *AdGuard* app and go through initial setup
- Tap the shield icon to open the Protection screen
- Tap *Safari Protection > Filters > Custom* (Tap the text itself, not the on-off icon)
- Tap *Add a filter*
- Paste the URL [`https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt`](https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt)
- Tap *Next > Add*.
- Change the toggle for custom filters from "Disabled" to "Enabled"

### Brave Browser (iOS)

* Install [Brave Browser](https://apps.apple.com/us/app/brave-browser-search-engine/id1052879175).
* Open Brave and tap *... > Shields and Privacy > Content Filtering > Add Filter by URL...*
* Paste in the URL [`https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt`](https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt)
* Press *Add*.

### Opera

Unfortunately, this filter list does not currently work in Opera.

Importing the filters had no effect when testing with both uBlock Origin and Opera's built in ad blocking. ([May be an issue with Opera](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/issues/64))

## Optional extra blocklist
There is an additional optional filter list [`GenAI-Blocklist-Extra.txt`](https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist-Extra.txt) with additional blocks. These are more subjective blocks and may be more prone to accidentally blocking some non-AI content or content that may be required for site functionality. These include:
* DeviantArt: Images from accounts that have posted AI images.
* Reddit: Posts from AI-focused subreddits.
* X: Posts made by @Grok.
* AI category section on news sites (Just the category, not posts covering AI).
* Customer support chatbots that are must be used before you can contact human customer support.

## FAQ
### Will this work with [AdBlock](https://getadblock.com/en/) or [Adblock Plus](https://adblockplus.org/)?
No. The list can be added, but it does not work for some unknown reason.

### Will this work with [AdGuard](https://adguard.com/en/adguard-browser-extension/overview.html)?
Yes. If you are using Google Chrome, you will need to enable "Allow User Scripts" in the settings.

### Will this work with [Pi-hole](https://pi-hole.net/)?
No. Pi-hole and uBlock Origin work differently. uBlock Origin allows filtering individual elements on pages, while Pi-hole blocks entire domains.

### Will this remove search results from sites that post AI generated content?
No. If you want to block sites from search engines, try [laylavish's Huge AI Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist).

### Why is AdGuard recommended for Google Chrome and iOS instead of uBlock Origin or uBlock Origin Lite?
uBlock Origin is not available for Google Chrome and iOS. While uBlock Origin Lite exists as an alternative, it [does not support custom filter lists](https://github.com/uBlockOrigin/uBOL-home/issues/167#issuecomment-2271471121). A previous version of this README suggested copying the GenAI filters into uBO Lite's custom filters as a workaround. However, filtering was unreliable, updating required [manually deleting the old filter rules](https://superuser.com/q/1934748/358766), and some filter rules were incompatible.

Due to these limitations, AdGuard is recommended over uBlock Origin Lite.

### Does this prevent AI content from being generated in the background?
Sometimes, but not always.

These filters work by hiding the AI elements. In some cases this may stop the generation. For example, if you load [this Google Search page](https://www.google.com/search?q=SQL+What+percentage+of+users+have+accessed+a+group) with filters on, then toggle "cosmetic filtering" off in uBlock Origin, you can see the AI overview won't generate until after it gets unhidden. However, AI content may still be generated in the background on other webpages.

## Contributing guidelines

If you want to [report an issue](https://github.com/Stevoisiak/Stevos-GenAI-Blocklist/issues) or submit a pull request for an item that isn't being blocked, please include the URL where the unblocked item appears and a screenshot of the page showing the unblocked item.

Commit messages use prefixes to indicate the type of change.
* A: Added a new filter
* M: Modified an existing filter
* R: Removed a filter
* C: Cosmetic "meta" change like editing comments or rearranging filters
* F: Fixed a filter (not working, blocking too much, typo, etc)
* +: Filter applied to the "extra" list

## Other AI blocking projects

* [uBlockOrigin Huge AI Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist): Blocklist for search engines to remove AI generated images
* [Just the Browser](https://justthebrowser.com/): Removes AI features, telemetry, and sponsored content from deskop web browsers
* [RemoveWindowsAI](https://github.com/zoicware/RemoveWindowsAI): Removes AI components in Windows
* [Fanboy's Anti-AI Suggestion List](https://github.com/easylist/easylist/blob/master/fanboy-addon/fanboy_ai_suggestions.txt): Another uBlock Origin filterlist aimed at AI widgets. Used as a reference for a few of the filters on this list.
* [CevvalYoutubeAIBlocklist](https://github.com/cevvalkoala/CevvalYoutubeAIBlocklist): Filter list for AI Music channels on YouTube for uBlock Origin.
* [Blocklist for AI music on YouTube](https://surasshu.com/blocklist-for-ai-music-on-youtube/): Blocklist of AI music channels on YouTube for the Blocktube extension.
* [Spotify AI Band Blocker](https://github.com/Reginald-Gillespie/Spotify-AI-Band-Blocker): Plugin for Spicetify to block AI artists on Spotify.
* [Spotify AI Blocker](https://github.com/CennoxX/spotify-ai-blocker): Userscript to block AI artists on Spotify.
* [Soul Over AI](https://github.com/xoundbyte/soul-over-ai): Index of AI-generated and AI-assisted music.
* [AI warning for Steam](https://github.com/seeeeew/aiwarningforsteam): Browser extension to show popup warnings for Steam games with an AI content disclosure.  

## Feedback

If you want to report an AI widget that is unblocked, please [submit an issue](https://github.com/Stevoisiak/Stevos-GenAI-Blocklist/issues) and include the website URL and a screenshot of the unblocked item. 

If you have any feedback about this project, I can be reached on Bluesky at [@stevoisiak.bsky.social](https://bsky.app/profile/stevoisiak.bsky.social) or via email at Stevoisiak(at)gmail.com.
