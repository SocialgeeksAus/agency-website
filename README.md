# Social Geeks Digital website blocks

Custom code blocks for the Social Geeks Digital website in HighLevel. See `CLAUDE.md` for brand rules, block order and how the blocks are built.

## Updating a block in HighLevel
1. Edit the file in `blocks/homepage/`.
2. Run `python tools/check_blocks.py` and make sure everything passes.
3. In the HighLevel builder, select the matching Custom Code element, click **Open Code Editor**, select all, paste the whole file (it starts with `<div class="sgd-cq">` and ends with `</div>`), and save the page.

## Setup for the checks
```
pip install playwright
playwright install chromium
python tools/check_blocks.py
```

## Before launch
- [ ] Fill `[STARTING PRICE]` and `[NOTICE PERIOD]`
- [ ] Import WordPress blog posts into HighLevel Blogs (before switching the domain), then fill `BLOG_HOME_URL` and `POST_URL_1..3`
- [ ] Set up 301 redirects from old WordPress URLs
- [ ] Real titles for case study cards 5–7
- [ ] Confirm the Facebook page URL and the proof-strip numbers
- [ ] Rebrand "What makes us a special agency"
- [ ] Replace the hero stock photo
- [ ] Rebrand the Google Ads, Meta Ads and Google Ads Clone pages (and decide what the Clone page is for)
- [ ] Check every page in HighLevel's mobile preview and on a real phone
