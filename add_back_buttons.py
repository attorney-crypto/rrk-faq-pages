#!/usr/bin/env python3
import os
import re

public_dir = "public"

# The back button HTML to add
back_button = """        <div style="margin-bottom: 20px;">
            <a href="/index.html" style="background-color: #D4AF37; color: #1a1a1a; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block;">← Back to Hub</a>
        </div>
"""

for filename in os.listdir(public_dir):
    if filename.endswith('.html') and filename not in ['index.html', 'all-faqs.html']:
        filepath = os.path.join(public_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if back button already exists
        if 'Back to Hub' in content:
            continue

        # Find <body> tag and add back button right after it
        content = re.sub(
            r'(<body>\s*)',
            r'\1' + back_button,
            content,
            count=1
        )

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Added back button to {filename}")

print("Done adding back buttons to all FAQ pages")
