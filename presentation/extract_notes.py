import textwrap
from pptx2txt2 import extract_text_per_slide
from pathlib import Path
import os

# find the odp file in the current directory
for filename in os.listdir("."):
    if filename.endswith(".odp"):
        odp_path = Path(filename)
        break
else:
    raise FileNotFoundError("No .odp file found in the current directory")


slide_data = extract_text_per_slide(odp_path)  # dict[int, str] per slide incl. notes
out_txt = Path("spin-liquids-notes.txt")

print(slide_data)
print(len(slide_data), "slides found. Writing to", out_txt)


def format_block(raw: str, width: int = 80) -> str:
    # collapse excessive whitespace, then wrap
    cleaned = " ".join(raw.split())
    return textwrap.fill(cleaned, width=width)


with out_txt.open("w", encoding="utf-8") as f:
    for slide_no, text in sorted(slide_data.items()):
        f.write(f"--- Slide {slide_no} ---\n\n")
        f.write(format_block(text))
        f.write("\n\n")




import zipfile

with zipfile.ZipFile(odp_path, "r") as zf:
    content_xml = zf.read("content.xml").decode("utf-8", errors="replace")

print(content_xml[:20000])
