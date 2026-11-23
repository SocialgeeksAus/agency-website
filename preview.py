"""Build tools/preview.html with every homepage block stacked, to open in a browser."""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
ORDER = ["top-bar", "hero", "proof-strip", "services", "how-we-work", "latest-posts",
         "case-studies", "testimonial", "instagram", "footer-content", "footer-bottom"]
body = "".join((ROOT / "blocks/homepage" / f"{n}.html").read_text() for n in ORDER)
out = ROOT / "tools" / "preview.html"
out.write_text("<!doctype html><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'>"
               f"<title>Homepage preview</title><body style='margin:0'>{body}")
print("Wrote", out)
