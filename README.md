# Stevo's GenAI Blocklist

A filter list for [uBlock Origin](https://github.com/gorhill/uBlock?tab=readme-ov-file#ublock-origin-ubo) and the [AdGuard Browser Extension](https://adguard.com/en/adguard-browser-extension/overview.html) that hides specific website features that use Generative AI or content labeled as AI generated.

Available for PC, ([Firefox](#firefox-microsoft-edge-or-waterfox-desktop), [Edge](#firefox-microsoft-edge-or-waterfox-desktop), [Chrome](#google-chrome-desktop), [Brave](#brave-desktop)), iOS ([Safari](#safari-ios), [Brave](#brave-browser-ios)), and Android ([Firefox](#firefox-android)).

## Examples of filtered content
* Google's AI Overviews
* YouTube's Ask button, video summaries, and Inspiration tab
* Copilot buttons on GitHub, Bing, Microsoft 365, and Azure Portal
* Amazon Rufus's product and review summaries
* Reddit Answers and recommended posts from AI subreddits
* DeviantArt's DreamUp ads
* Facebook's AI chat
* TikTok videos and Booru images tagged as AI generated
* X/Twitter's Grok buttons

## Image comparison

Before:

<img width="687" height="538" alt="Google homepage with AI" src="https://github.com/user-attachments/assets/248231e3-a107-40a5-a757-b5255decdc19" />

After:

<img width="687" height="359" alt="Google homepage without AI" src="https://github.com/user-attachments/assets/e9c84390-6702-4d9e-9e01-c18f4893c5fe" />

## Installation
### Firefox, Microsoft Edge, or Waterfox (Desktop)
- Install [uBlock Origin](https://github.com/gorhill/ublock#ublock-origin-ubo).
- Left-click [this link](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt&title=Stevo's%20GenAI%20Blocklist).
- Press "_Subscribe_" to import the filter list.

If the above instructions didn't work, (possibly due to multiple adblockers being installed), you can try importing manually:

- Install [uBlock Origin](https://github.com/gorhill/ublock#ublock-origin-ubo).
- Click the uBlock button in the toolbar and open Dashboard Settings (gear icon)
- Select the "_Filter lists_" tab
- Open the "_Import..._" section and paste [`https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt`](https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt)
- Click "_Apply Changes_"

### Google Chrome (Desktop)
- Install [AdGuard AdBlocker](https://chromewebstore.google.com/detail/adguard-adblocker/bgnkhhnnamicmpeenaelnjfhikgbkllg) for Chrome.
- Click the green AdGuard icon in Chrome then click the gear icon.
- Open the Filters tab, go to "Custom", and click the "extension settings" link.
- Enable "Allow User Scripts".
- Return to this page and left-click [this link](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist.txt&title=Stevo's%20GenAI%20Blocklist).
- Under "Add custom filter", hit "Next".
- (_Recommended_) Check the "Trusted" box.
- Click "Add".

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

## Optional extra blocklist
There is an additional optional filter list [`GenAI-Blocklist-Extra.txt`](https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist-Extra.txt) with additional blocks. These are more subjective or experimental blocks. They may be more prone to accidentally blocking non-AI content or content required for site functionality. These include:
* Reddit: Content from AI-focused subreddits. (Main filter only hides post recommendations)
* X: Posts made by @Grok.
* AI category section on news sites (Just the category, not posts covering AI).
* Customer support chatbots that must be used before you can contact human customer support.
* YouTube: Trusted filter to remove autodubbing when loading a video directly via URL, but causes visible page refresh even on videos without autodubbing.

## FAQ
### Which adblockers will this filter list work with?
These filters were developed for [uBlock Origin](https://github.com/gorhill/ublock#ublock-origin-ubo), but they should also work with [AdGuard](https://adguard.com/en/adguard-browser-extension/overview.html), [AdBlock](https://getadblock.com/), [Adblock Plus](https://adblockplus.org/), and [Brave's](https://brave.com) integrated adblocker.

### Will this remove sites that post AI generated content from search results?
No. If you want to block AI sites from search engines, try [laylavish's Huge AI Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist).

### Can I use these filters with [Pi-hole](https://pi-hole.net/)?
No. Pi-hole and uBlock Origin work differently. uBlock Origin allows filtering individual elements on pages, while Pi-hole blocks entire domains.

### Can I use these filters with [Opera](https://www.opera.com/)?
No. These filters do not work with Opera's built-in adblocker or uBlock Origin for Opera. The built-in adblocker doesn't allow importing custom filter lists via URL while uBlock Origin for Opera didn't filter correctly when testing. ([This may be an issue with Opera](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/issues/64))

### Why are AI Overviews still showing up on Google?
If you use AdBlock Plus, make sure "[Show acceptable ads](https://help.adblockplus.org/adblock-plus-help-center/what-are-acceptable-ads)" is [disabled in your settings](https://help.adblockplus.org/adblock-plus-help-center/block-all-ads).

### Why is AdGuard recommended for Google Chrome and iOS instead of uBlock Origin?
uBlock Origin is not available for Google Chrome and iOS.

While uBlock Origin Lite exists as an alternative, it [does not support custom filter lists](https://github.com/uBlockOrigin/uBOL-home/issues/167#issuecomment-2271471121). A previous version of this README suggested copying the GenAI filters into uBO Lite's custom filters as a workaround. However, filtering was unreliable, updating required [manually deleting the old filter rules](https://superuser.com/q/1934748/358766), and some filter rules were incompatible.

### Will this prevent AI summaries from being generated in the background of search engines?
Only sometimes. This filter list was created with the primary goal of hiding AI elements. A few network filters have been added to prevent content generation, but the coverage is not extensive.

### How many websites have filters for AI features?
Over 300.

### Where can I find a full list of filtered items?
Check [`GenAI-Blocklist.txt`](https://github.com/Stevoisiak/Stevos-GenAI-Blocklist/blob/main/GenAI-Blocklist.txt) and [`GenAI-Blocklist-Extra.txt`](https://github.com/Stevoisiak/Stevos-GenAI-Blocklist/blob/main/GenAI-Blocklist-Extra.txt).

### Why do some filters show "*Invalid filter: Filter requires trusted source*" in uBlock Origin?
A small number of filters use features that require trusted origin filters in uBlock Origin. Trusted filters are disabled by default in uBlock Origin for security reasons, as they allow directly executing code on webpages.

This list requires trust to:
* Replace "Search or ask a question" text on GitHub Docs and YouTube.
* Remove the "[AI sparkle](https://design.google/library/ai-sparkle-icon-research-pozos-schmidt)" from search icons.
* Remove automatic audio dubbing on YouTube videos if they were directly loaded from a URL. (in Extra filters, [see below FAQ entry](#why-do-youtube-videos-still-sometimes-play-ai-dubbed-audio-tracks)).

To be clear, ***if you use uBlock Origin, you do not need to mark this list as trusted to use a majority of the AI filters***. However, if you want to use the filters listed above, you can go to [uBlock Origin's advanced settings](https://github.com/gorhill/ublock/wiki/Advanced-settings) and add `https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/` to [`trustedListPrefixes`](https://github.com/gorhill/ublock/wiki/Advanced-settings#trustedListPrefixes).

### Why are trusted filters recommended in AdGuard but not uBlock Origin?
Some filters use [scriptlets](https://github.com/AdguardTeam/Scriptlets/blob/master/wiki/about-scriptlets.md) to block AI items. (YouTube autodubbing, TikTok videos with AI, etc). In uBlock Origin, trusted filters are only needed for scriptlets that start with `trusted-`. However, in AdGuard trusted filters [are required for all scriptlets](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3522#issuecomment-4441812031). Also, it's easier to enable trusted filters in AdGuard compared to uBlock Origin. 

### Why do YouTube videos still sometimes play AI dubbed audio tracks?
The filter for automatic dubbing on YouTube does not work when opening a video via direct URL. (IE: Entering the address directly in your browser's URL bar). It will work when clicking a video while already on YouTube, such as on YouTube's homepage, search results, or suggested videos.

The [extra filter list](https://raw.githubusercontent.com/Stevoisiak/Stevos-GenAI-Blocklist/refs/heads/main/GenAI-Blocklist-Extra.txt) has a filter that works when loading directly from URL, but it requires allowing trusted filters to run, ([see above FAQ entry](#why-do-some-filters-show-invalid-filter-filter-requires-trusted-source-in-ublock-origin)), and causes a visible page refresh whenever a video is loaded directly via URL.

## Contributing guidelines
If you want to [report an issue](https://github.com/Stevoisiak/Stevos-GenAI-Blocklist/issues) or submit a pull request for an item that isn't being blocked, please include the URL where the unblocked item appears and a screenshot of the page showing the unblocked item.

Commit messages use prefixes to indicate the type of change.
* A: Added a new filter
* M: Modified an existing filter
* R: Removed a filter
* C: Cosmetic "meta" change like editing comments or rearranging filters
* F: Fixed a filter (not working, blocking too much, typo, etc.)
* +: Filter applied to the "extra" list

## Other AI blocking projects
* [Just the Browser](https://justthebrowser.com/): Removes AI features, telemetry, and sponsored content from web browsers.
* [RemoveWindowsAI](https://github.com/zoicware/RemoveWindowsAI): Removes AI components in Windows.
* [AI uBlock Origin Blacklist](https://github.com/alvi-se/ai-ublock-blacklist): uBlock Origin filter list for AI content farms. 
* [uBlockOrigin Huge AI Blocklist](https://codeberg.org/just_a_husk/uBlockOrigin-AI-Blocklist): Filter list to remove sites with AI generated content from search engines.
* [CevvalYoutubeAIBlocklist](https://github.com/cevvalkoala/CevvalYoutubeAIBlocklist): Filter list for AI Music channels on YouTube for uBlock Origin.
* [Blocklist for AI music on YouTube](https://surasshu.com/blocklist-for-ai-music-on-youtube/): Blocklist of AI music channels on YouTube for the Blocktube extension.
* [Spotify AI Band Blocker](https://github.com/Reginald-Gillespie/Spotify-AI-Band-Blocker): Plugin for Spicetify to block AI artists on Spotify.
* [Spotify AI Blocker](https://github.com/CennoxX/spotify-ai-blocker): Userscript to block AI artists on Spotify.
* [AI warning for Steam](https://github.com/seeeeew/aiwarningforsteam): Browser extension to show popup warnings for Steam games with an AI content disclosure.
* [Fanboy's Anti-AI Suggestion List](https://github.com/easylist/easylist/blob/master/fanboy-addon/fanboy_ai_suggestions.txt): Another uBlock Origin filter list aimed at AI widgets. Used as a reference for a few of the filters on this list.
* [Is AI Profitable Yet](https://isaiprofitable.com/): Site that tracks the costs and revenue of AI companies.

## Feedback
If you want to report an AI widget that is unblocked, please [submit an issue](https://github.com/Stevoisiak/Stevos-GenAI-Blocklist/issues) and include the website URL and a screenshot of the unblocked item. 

If you have any feedback about this project, I can be reached on Bluesky at [@stevoisiak.bsky.social](https://bsky.app/profile/stevoisiak.bsky.social) or via email at Stevoisiak(at)gmail.com.
