#!/usr/bin/env python3
import os
import re

public_dir = "public"

# Replace mustard gold #D4AF37 with clean light gray/silver #BDBDBD
old_color = "#D4AF37"
new_color = "#BDBDBD"

# Also try the lowercase version and c9a227 (darker gold)
replacements = [
    ("#D4AF37", "#BDBDBD"),
    ("#d4af37", "#BDBDBD"),
    ("#c9a227", "#A8A8A8"),
]

for filename in os.listdir(public_dir):
    if filename.endswith('.html'):
        filepath = os.path.join(public_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        for old, new in replacements:
            content = content.replace(old, new)

        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated colors in {filename}")

print("Done replacing mustard gold with clean silver/gray")
