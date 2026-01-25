#!/usr/bin/env python3
import os
import re

public_dir = "public"

# Pattern to find and remove the CSS that got inserted into JSON-LD
bad_css_pattern = r'\s*body::before\s*\{\s*content:\s*"";[^}]+\}\s*'

for filename in os.listdir(public_dir):
    if not filename.endswith('.html'):
        continue

    filepath = os.path.join(public_dir, filename)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Remove the bad CSS from inside JSON-LD blocks
    content = re.sub(bad_css_pattern, '', content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Fixed {filename}")

print("Done! Removed CSS from JSON-LD schemas")
