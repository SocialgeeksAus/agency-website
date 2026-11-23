# Social Geeks Digital website (HighLevel rebuild)

This repo holds the custom code blocks for the Social Geeks Digital website, which is built in HighLevel (GoHighLevel). Each file in `blocks/` is pasted into a Custom HTML/Javascript element in the HighLevel page builder. HighLevel is the live source; this repo is the working copy and history.

## How blocks work
- One file = one HighLevel Custom Code element. Each file must be self-contained: its own `<style>`, markup and any `<script>`.
- Every file is wrapped in `<div class="sgd-cq">` with `container-type: inline-size`. Layout changes use `@container (max-width: …)`, NOT `@media (max-width: …)`. HighLevel's mobile preview draws the page in a narrow box on a wide screen, so screen-width media queries don't fire there. Container queries respond to the block's own width.
- Font sizes that scale use `cqi` units, not `vw`, for the same reason.
- `@media (pointer: coarse)` is used to enlarge tap targets on any touch screen (including landscape iPads). `@media (prefers-reduced-motion)` is respected.
- Scope every CSS selector to the block's own class prefix (`.sgd-…`; the top bar still uses `.clone-top-bar…`). Never style bare elements.
- After any change, run `python tools/check_blocks.py`. All cases must pass.
- `python tools/preview.py` builds `tools/preview.html` with every homepage block stacked.

## Homepage block order (top to bottom)
1. `top-bar.html` (top bar)
2. Header: native HighLevel elements, not code (white logo, menu, outline "Book a call" button). Saved as a global section.
3. `hero.html`
4. `proof-strip.html`
5. `services.html` (id `services`; the hero's "See what we do" links to `#services`)
6. `how-we-work.html` + `latest-posts.html` (pasted together into one HighLevel element)
7. `case-studies.html`
8. "What makes us a special agency" block: NOT YET REBRANDED (still old AI-generated code in HighLevel)
9. `testimonial.html`
10. `instagram.html`
11. `footer-content.html`
12. `footer-bottom.html`

## Brand (v1.0, November 2026). Source: Social-Geeks-Digital-Brand-Pack in Google Drive
**Idea: "Glass House".** Nothing to hide: prices on the page, no lock-in contracts, ad accounts stay in the client's name.

**Name rule:** always "Social Geeks Digital" in full. Never "Social Geeks", "SG", "SGD", "the Geeks" or "Social Geeks Digital Agency". (Client quotes are kept verbatim, but choose excerpts that avoid the short forms.)

**Voice:** Direct, Transparent, Grounded, Down to earth. Lead with the answer. "Test, tweak, optimise." Never promise or guarantee results. Australian English. No buzzwords.

**Colours (only these):**
| Name | Hex | Use |
|---|---|---|
| Geek Navy | #0E1A2B | text, dark sections |
| Graph Paper | #F5F6F1 | light backgrounds |
| White | #FFFFFF | text on navy, alt background |
| Geek Red | #D42A22 | buttons only: one red moment per screen |
| Deep Red | #B8231C | button hover, small red text on light |
| Slate Grey | #5B6676 | secondary text on light |
| Mist | #C9CED6 | secondary text on navy |
| Line | #D9DCD3 | dividers |
| Blush | #FBE6E3 | soft panels (rarely used) |
On navy, red only for large shapes (buttons). Small text on navy is White or Mist.

**Type:** Bricolage Grotesque 800 headlines (tight tracking), 600 subheads. Inter 400 body (16–18px, 1.55), 600 buttons. JetBrains Mono for prices, stats and small labels. Sentence case for headings and buttons.

**Buttons:** Geek Red, white text, fully rounded (999px), Inter 600, sentence case. Secondary actions are underlined text links or navy outline buttons.

**Logos (HighLevel Media Storage):**
- White: https://files.leadconnectorhq.com/file/6aff8fe8898cec9ac772ec0e/sgd-logo-primary-white.svg
- Navy: https://files.leadconnectorhq.com/file/6afe9137898cec9ac7536a38/sgd-logo-primary-navy.svg
- Favicon 512: https://files.leadconnectorhq.com/file/6afe90852c68ebcf46f91170/sgd-favicon-512.png

## Hard rules for content
- Do not invent statistics, testimonials, client names, results, awards or guarantees. Use clearly marked placeholders instead.
- Remove anything the old AI build made up (fake Instagram reels, fake reviews, invented stats like "93% of purchases…").
- Keep placeholders exactly as written until real values are supplied.

## Key links
- Booking: https://links.socialgeeks.com.au/widget/bookings/sg-free-consult
- Client login: https://app.socialgeeks.io
- Case studies page: https://socialgeeks.com.au/portfolio-case-studies/
- Google Partner profile: https://www.google.com/partners/agency?id=9681577903
- Instagram: https://www.instagram.com/socialgeeks.io/

## Open items (see README for the full list)
- `[STARTING PRICE]` and `[NOTICE PERIOD]` in hero, how-we-work: real values needed.
- `BLOG_HOME_URL`, `POST_URL_1..3` in latest-posts and footer-content: fill after the WordPress blog is imported into HighLevel Blogs.
- Case studies cards 5–7: real titles and service labels needed (`[CASE STUDY TITLE]`, `[SERVICE]`).
- Facebook URL mismatch: top bar uses facebook.com/socialgeeksdigital, footer uses facebook.com/socialgeeks.io. Confirm which is correct.
- Confirm "300+ businesses" and "$20M+ ad spend" in proof-strip are accurate.
- Confirm `/about-us/`, `/contact/` and `/meta-ads` page addresses once those pages exist.
- Rebrand the "What makes us a special agency" block.
- Hero background is still a stock laptop photo; replace with a real photo of Kyle or a client dashboard.
