#!/usr/bin/env python3
import os
import re

public_dir = "public"

# The CSS to find and replace
old_body_css = r"body \{\s*font-family: Arial, sans-serif;\s*line-height: 1\.6;\s*background-color: #555759;"

new_body_css = """body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background: url('rrk-law-building.png') no-repeat center center fixed;
            background-size: cover;
            position: relative;"""

# The overlay CSS to add after body closing brace
overlay_css = """        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(26, 26, 26, 0.85);
            z-index: -1;
        }"""

for filename in os.listdir(public_dir):
    if filename.endswith('.html') and filename != 'index.html':
        filepath = os.path.join(public_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace body background
        content = re.sub(
            r'background-color: #555759;',
            "background: url('rrk-law-building.png') no-repeat center center fixed;\n            background-size: cover;\n            position: relative;",
            content
        )

        # Add overlay if not already present
        if 'body::before' not in content:
            # Find the closing brace of body style and add overlay after it
            content = re.sub(
                r'(        body \{[^}]+\})',
                r'\1\n' + overlay_css,
                content,
                count=1
            )

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated all FAQ pages with RRK Law building background")
