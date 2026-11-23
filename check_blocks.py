"""Render all homepage blocks and check layout at phone, tablet and desktop sizes.

Usage:
  pip install playwright && playwright install chromium
  python tools/check_blocks.py

Checks: no sideways scrolling, no text under 12px, tap targets >= 24px on touch
screens, and that blocks reflow inside a narrow box on a wide screen (which is
how HighLevel's builder previews mobile).
"""
import asyncio, json, pathlib
from playwright.async_api import async_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
ORDER = ["top-bar", "hero", "proof-strip", "services", "how-we-work", "latest-posts",
         "case-studies", "testimonial", "instagram", "footer-content", "footer-bottom"]
BODY = "".join((ROOT / "blocks/homepage" / f"{n}.html").read_text() for n in ORDER)

def page(frame_width=None):
    inner = BODY if not frame_width else f"<div id='frame' style='width:{frame_width}px;margin:0 auto'>{BODY}</div>"
    return ("<!doctype html><meta name=viewport content='width=device-width,initial-scale=1'>"
            f"<body style='margin:0'>{inner}")

CHECK = """() => {
  const fr = document.getElementById('frame') || document.body;
  const box = fr.getBoundingClientRect(), out = {overflow: [], small: [], tap: []};
  document.querySelectorAll('body *').forEach(el => {
    const r = el.getBoundingClientRect(); if (!r.width) return;
    if (el.closest('.sgd-cases-track') && !el.classList.contains('sgd-cases-track')) return;
    if (r.right > box.right + 1 || r.left < box.left - 1) out.overflow.push(el.className || el.tagName);
    if ([...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) {
      const fs = parseFloat(getComputedStyle(el).fontSize); if (fs < 12) out.small.push(el.className + ':' + fs);
    }
    if (matchMedia('(pointer: coarse)').matches && (el.tagName === 'A' || el.tagName === 'BUTTON')
        && (r.height < 24 || r.width < 24)) out.tap.push(el.className);
  });
  for (const k in out) out[k] = [...new Set(out[k])].slice(0, 10);
  return out;
}"""

CASES = [
    ("phone 320", 320, 700, True, None), ("phone 375", 375, 800, True, None),
    ("phone 414", 414, 850, True, None), ("tablet portrait", 768, 1024, True, None),
    ("tablet landscape", 1180, 820, True, None), ("laptop 1280", 1280, 800, False, None),
    ("desktop 1440", 1440, 900, False, None), ("desktop 1920", 1920, 1080, False, None),
    ("HighLevel mobile preview", 1440, 900, False, 375),
    ("HighLevel tablet preview", 1440, 900, False, 768),
]

async def main():
    tmp = ROOT / "tools" / "_preview.html"
    failed = False
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for name, w, h, touch, frame in CASES:
            tmp.write_text(page(frame))
            ctx = await browser.new_context(viewport={"width": w, "height": h}, has_touch=touch, is_mobile=touch)
            pg = await ctx.new_page(); await pg.goto(tmp.as_uri()); await pg.wait_for_timeout(300)
            res = await pg.evaluate(CHECK)
            ok = not any(res.values())
            failed |= not ok
            print(("PASS " if ok else "FAIL ") + name, "" if ok else json.dumps(res))
            await ctx.close()
        await browser.close()
    tmp.unlink(missing_ok=True)
    raise SystemExit(1 if failed else 0)

asyncio.run(main())
